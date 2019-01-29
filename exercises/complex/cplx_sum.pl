extends = /exercises/templates/basicmath.pl

title = Somme de deux nombres complexes

lang=fr

imaginary_unit='i'

before ==
z1=ut.rand_complex_int(5)
z2=ut.rand_complex_int(5)
sol=z1+z2
strsol=str(sol)
latexz1=ut.latex(z1)
latexz2=ut.latex(z2)
==

text = On considère les nombres complexes $% z_1= {{latexz1}} %$ et $% z_2= {{latexz2}} %$. Calculer $% z_1+z_2 %$.

evaluator==
sol=sp.sympify(strsol)
score,numerror,texterror=ut.ans_complex_cartesian(response['answer'],sol,imaginary_unit)
feedback=fb.msg_analysis(score,texterror,lang)
==



