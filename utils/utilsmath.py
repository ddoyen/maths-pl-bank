from plrandom import rd
import sympy as sp
import sympy.parsing.sympy_parser as prs
from sympy.printing.latex import LatexPrinter as LatexPrinter0

#############################################################################
# Latex
#############################################################################

class CustomLatexPrinter(LatexPrinter0):
    
    _default_settings = {
        "order": None,
        "mode": "plain",
        "itex": False,
        "fold_frac_powers": False,
        "fold_func_brackets": False,
        "fold_short_frac": None,
        "long_frac_ratio": None,
        "mul_symbol": None,
        "inv_trig_style": "abbreviated",
        "mat_str": None,
        "mat_delim": "[",
        "symbol_names": {},
        "ln_notation": True,
        "interv_rev_brack": True,
    }
    
    def _print_Interval(self, i):
        
        if i.start == i.end:
            return r"\left\{%s\right\}" % self._print(i.start)
            
        else:
            if i.left_open:
                if self._settings["interv_rev_brack"]:
                    left = ']'
                else:
                    left = '('
            else:
                left = '['
    
            if i.right_open:
                if self._settings["interv_rev_brack"]:
                    right = '['
                else:
                    right = ')'
            else:
                right = ']'
    
            return r"\left%s%s, %s\right%s" % \
                    (left, self._print(i.start), self._print(i.end), right)


LatexPrinter=CustomLatexPrinter()

def latex(expr):
    return LatexPrinter.doprint(expr)

#############################################################################
# Basic
#############################################################################

def sympy_expr(s):
    """
    Convert a string to a sympy expression without mathematical simplifications.

    >>> sympy_expr("x+3+2x")
    x + 2*x + 3
    
    >>> sympy_expr("2^3")
    2**3
    
    >>> sympy_expr("sin 2pi")
    sin(2*pi)
    
    >>> sympy_expr("3!")
    factorial(3)
    """
    transformations=prs.standard_transformations + (prs.implicit_multiplication_application,prs.convert_xor)
    with sp.evaluate(False):
        return prs.parse_expr(s,transformations=transformations,evaluate=False)
        
def is_equal(a, b):
    """
    Check if two sympy expressions are equal after simplifications.
    """
    return sp.simplify(a-b) == 0

def _list_rand0(n,items,replace,removed_values):
    """
    Generate a list of random items selected from a list.
    """
    if replace==True:
        lst=[]
        while len(lst)<n:
            item=rd.choice(items)
            if item not in removed_values:
                lst.append(item)
    elif replace==False:
        m=len(removed_values)
        lst=rd.sample(items,n+m)
        if m>0:
            lst=[x for x in lst if x not in removed_values]
            lst=lst[0:n]
    else:
        raise ValueError
    return lst

def list_randint(n,a,b,removed_values=[]):
    """
    Generate a list of random integers with replacements.
    """
    return _list_rand0(n,range(a,b+1),True,removed_values)
    
def list_randitem(n,items,removed_values=[]):
    """
    Generate a list of random items selected from a list with replacements.
    """
    return _list_rand0(n,items,True,removed_values)
    
def list_randint_norep(n,a,b,removed_values=[]):
    """
    Generate a list of random integers without replacements.
    """
    return _list_rand0(n,range(a,b+1),False,removed_values)
    
def list_randitem_norep(n,items,removed_values=[]):
    """
    Generate a list of random items selected from a list without replacements.
    """
    return _list_rand0(n,items,False,removed_values)

#############################################################################
# Numbers
#############################################################################

def ans_number(strans,sol):
    """
    Analyze an answer of type number
    """
    try:
        ans=sympy_expr(strans)
        if not isinstance(ans,sp.Number):
            score=-1
            numerror=2
            texterror="Votre réponse n'est pas un nombre valide."
        elif ans!=sol:
            score=0
            numerror=1
            texterror=""
        else:
            score=100
            numerror=0
            texterror=""
    except:
        score=-1
        numerror=2
        texterror="Votre réponse n'est pas un nombre valide."
    return score,numerror,texterror


#############################################################################
# Fractions
#############################################################################


def is_frac(expr):
    """
    Check if a sympy expression is a fraction of integers.
    """
    f = sp.fraction(expr)
    return f[0].is_Integer and f[1].is_Integer and f[1]!=0

def is_frac_irred(expr):
    """
    Check if a sympy fraction of integers is irreducible.
    """
    f = sp.fraction(expr)
    return sp.gcd(f[0],f[1])==1 and f[1]>0
    
def ans_frac(strans,sol):
    """
    Analyze an answer of type fraction.
    """
    try:
        ans=sympy_expr(strans)
        if not is_frac(ans):
            score=-1
            numerror=3
            texterror="Votre réponse n'est pas une fraction d'entiers ou un entier."
        elif not is_frac_irred(ans):
            score=0
            numerror=2
            texterror="Votre réponse n'est pas une fraction irréductible."
        elif not is_equal(ans,sol):
            score=0
            numerror=1
            texterror=""
        else:
            score=100
            numerror=0
            texterror=""
    except:
        score=-1
        numerror=3
        texterror="Votre réponse n'est pas une fraction d'entiers ou un entier."
    return score,numerror,texterror

#############################################################################
# Intervals
#############################################################################

    
def interval(s,kw_empty_set=['empty'],kw_infinity=['infty','inf','infinity']):
    """
    Convert a string to a sympy interval or singleton.
    
    >>> interval("]0,2]")
    Interval.Lopen(0, 2)
    
    >>> interval("]0,inf[")
    Interval.open(0, oo)
    """
    s=s.strip()
    if s in kw_empty_set:
        return sp.EmptySet
    
    local_dict = {kw:S.Infinity for kw in kw_infinity}
    transformations=prs.standard_transformations + (prs.implicit_multiplication_application,prs.convert_xor)
    with sp.evaluate(False):
        a=prs.parse_expr(s[1:-1],local_dict=local_dict,transformations=transformations,evaluate=False)
    if s[0]=='[' and s[-1]==']':
        return sp.Interval(*a)
    elif s[0]=='[' and s[-1]=='[':
        return sp.Interval(*a,right_open=True)
    elif s[0]==']' and s[-1]==']':
        return sp.Interval(*a,left_open=True)
    elif s[0]==']' and s[-1]=='[':
        return sp.Interval(*a,left_open=True,right_open=True)
    elif s[0]=='{' and s[-1]=='}':
        return sp.FiniteSet(a)
    else:
        raise ValueError('cannot convert string to an interval')

def rand_interval_type(a,b):
    """
    Generate a random sympy interval.
    """
    bl=rd.choice([True,False])
    br=rd.choice([True,False])
    return sp.Interval(a,b,left_open=bl,right_open=br)

def ans_interval(strans,sol,kw_empty_set=['empty'],kw_infinity=['infty','inf','infinity']):
    """
    Analyze an answer of interval type.
    """
    try:
        ans=interval(strans,kw_empty_set,kw_infinity)
        if ans!=sol:
            score=0
            numerror=1
            texterror=""
        else:
            score=100
            numerror=0
            texterror=""
    except:
        score=-1
        numerror=2
        texterror="Votre réponse n'est pas un ensemble valide."
    return score,numerror,texterror


#############################################################################
# Matrices
#############################################################################


def rand_int_matrix(n,p,bound):
    """
    Generate a sympy matrix with random integer entries.
    """
    entries=list_randint(n*p,-bound,bound)
    return sp.Matrix(n,p,entries)

def rand_int_matrix_invertible(n,bound):
    """
    Generate an invertible random sympy matrix with integer entries.
    """
    while True:
        M=rand_int_matrix(n,p,bound)
        if M.det()!=0:
            return M


