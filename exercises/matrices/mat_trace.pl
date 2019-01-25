extends = /exercises/templates/basicmath.pl

title = Trace d'une matrice

builder_param ==
matsize=2
coeffbound=5
==

builder_main ==
A=ut.rand_int_matrix(matsize,matsize,coeffbound)
==

builder_statement ==
text = """On considère la matrice 
    $% A= {} %$
Calculer la trace de cette matrice
""".format(ut.latex(A))
sol=sp.trace(A)
==


eval_param ==

==

eval_main==
if sol==ans:
    score=100
else:
    score=0
==

eval_feedback==

==
