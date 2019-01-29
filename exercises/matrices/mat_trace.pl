extends = /exercises/templates/basicmath.pl

settings.allow_reroll = true

title = Trace d'une matrice

lang = fr

matsize = 3

coeffbound = 5

before ==
A=ut.rand_int_matrix(int(matsize),int(matsize),int(coeffbound))
sol=sp.trace(A)
strsol=str(sol)
latexA=ut.latex(A)
==

text ==
On considère la matrice $$ A= {{latexA}}. $$ Calculer la trace de cette matrice.
==

evaluator ==
sol=sp.sympify(strsol)
score,numerror,texterror=ut.ans_number(response['answer'],sol)
feedback=fb.msg_analysis(score,texterror,lang)
==









