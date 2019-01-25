extends = /exercises/templates/basicmath.pl

title = Simplification d'une fraction


builder_main ==
c=rd.choice([2,3,4,5,6])
a=2
b=3
p=c*a
q=c*b
sol=sp.Rational(a,b)
strsol=str(sol)
==

builder_statement ==
text = """Simplifier la fraction $%{} / {}.%$""".format(p,q)
==

eval_main==
sol=sp.sympify(strsol)
score,numerror,texterror=ut.ans_frac(response['answer'],sol)
feedback=texterror
==
