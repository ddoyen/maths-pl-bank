extends = /exercises/templates/basicmath.pl

title = Trace d'une matrice

lang = fr

matsize = 3

coeffbound = 5

before ==
A=ut.rand_int_matrix(int(matsize),int(matsize),int(coeffbound))
sol=sp.trace(A)
latexA=ut.latex(A)
==

text ==
On considère la matrice $$ A= {{latexA}}. $$ Calculer la trace de cette matrice.
==

evaluator ==
score,numerror,texterror=ut.ans_number(answer['1'],sol)
feedback=fb.msg_analysis(score,texterror,lang)
==











