extends = /template/mathexpr.pl

title = Ensemble de définition (racine carrée 1)

lang = fr

virtualKeyboards = sets

before ==
a=ut.randint(-6,6,removed_values=[0,1,-1])
b=ut.randint(-6,6,removed_values=[0])
x=sp.symbols('x')
f=sp.sqrt(a*x+b)
latexf=ut.latex(f)
from sympy.solvers.inequalities import solve_univariate_inequality
sol = solve_univariate_inequality(a*x+b >= 0, x, relational=False)
==

text ==
Déterminer l'ensemble de définition de la fonction $%f : x \mapsto {{latexf}}%$.
==

evaluator==
score,_,texterror=ut.ans_interval(answer['1'],sol)
feedback=fb.msg_analysis(score,texterror,lang)
==
