extends = /exercises/templates/basicmath.pl

title = Simplification d'une fraction

lang = fr

before ==
c=rd.choice([2,3,4,5,6])
a=2
b=3
p=c*a
q=c*b
sol=sp.Rational(a,b)
strsol=str(sol)
==


text = Simplifier la fraction $%{{p}} / {{q}}.%$

evaluator==
sol=sp.sympify(strsol)
score,numerror,texterror=ut.ans_frac(response['answer'],sol)
feedback=fb.msg_analysis(score,texterror,lang)
==

