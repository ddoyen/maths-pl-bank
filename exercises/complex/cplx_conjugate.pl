extends = /exercises/templates/basicmath.pl

title = Conjugué d'un nombre complexe

lang = fr

imaginary_unit= i

before ==
z=ut.rand_complex_int(5)
latexz=ut.latex(z)
sol=sp.conjugate(z)
==

text = Quel est le conjugué du nombre complexe $%z ={{latexz}}%$ ?

evaluator ==
score,numerror,texterror=ut.ans_complex(answer['1'],sol,imaginary_unit)
feedback=fb.msg_analysis(score,texterror,lang)
==

