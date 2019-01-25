extends = /exercises/templates/basicmath.pl

title = Intersection d'intervalles

builder_param ==
ut.LatexPrinter._settings.update({'interv_rev_brack': True})
==

builder_main ==
val=ut.list_randint_norep(4,-10,10)
val.sort()
interv=[ut.rand_interval_type(val[0],val[2]),ut.rand_interval_type(val[1],val[3])]
rd.shuffle(interv)
A,B=interv
sol=sp.Intersection(A,B)
strsol=str(sol)
==

builder_statement ==
text = """On considère les intervalles $% A= {} %$ et $% B={}.%$ Déterminer $% A\cap B%$.""".format(ut.latex(A),ut.latex(B))
==

form_help ==
Pour désigner l'ensemble vide, écrire &laquo; vide &raquo;.
==

eval_param ==
ut.LatexPrinter._settings.update({'interv_rev_brack': True})
kw_empty_set=['vide']
kw_infinity=['infini','inf']
==

eval_main==
sol=sp.sympify(strsol)
score,numerror,texterror=ut.ans_interval(response['answer'],sol,kw_empty_set,kw_infinity)
==

eval_feedback==
feedback=texterror
#""" La réponse correcte est $${}$$.""".format(ut.latex(sol))
==





