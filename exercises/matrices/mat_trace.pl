extends = /exercises/templates/basicmath.pl

title = Trace d'une matrice

builder_param ==
matsize=3
coeffbound=5
==

builder_main ==
A=ut.rand_int_matrix(matsize,matsize,coeffbound)
sol=sp.trace(A)
==

builder_statement ==
text = """
On considère la matrice
$$ A= {} $$
Calculer la trace de cette matrice
""".format(ut.latex(A))
==

eval_main==
score,numerror,texterror=ut.ans_number(response['answer'],sol)
feedback=texterror
==



