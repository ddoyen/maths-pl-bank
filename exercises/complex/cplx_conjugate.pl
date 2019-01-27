extends = /exercises/templates/basicmath.pl

title = Conjugué d'un nombre complexe

builder_main ==
z=ut.rand_complex_int(5)
sol=sp.conjugate(z)
strsol=str(sol)
==

builder_statement ==
text = """Quel est le conjugué du nombre complexe $%z ={}%$ ?""".format(ut.latex(z))
==

eval_param ==
imaginary_unit='i'
==

eval_main==
sol=sp.sympify(strsol)
score,numerror,texterror=ut.ans_complex(response['answer'],sol,imaginary_unit)
feedback=texterror
==
