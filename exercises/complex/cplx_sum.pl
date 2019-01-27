extends = /exercises/templates/basicmath.pl

title = Somme de deux nombres complexes

builder_main ==
z1=ut.rand_complex_int(5)
z2=ut.rand_complex_int(5)
sol=z1+z2
strsol=str(sol)
==

builder_statement ==
text = """On considère les nombres complexes $% z_1= {} %$ et $% z_2= {} %$. Calculer $% z_1+z_2 %$.""".format(ut.latex(z1),ut.latex(z2))
==

eval_param ==
imaginary_unit='i'
==

eval_main==
sol=sp.sympify(strsol)
score,numerror,texterror=ut.ans_complex_cartesian(response['answer'],sol,imaginary_unit)
feedback=texterror
==


