extends = /exercises/intervals/intervals_intersection.pl

title = Intersection of intervals

builder_param ==
ut.LatexPrinter._settings.update({'interv_rev_brack': False})
==

builder_statement ==
text = r"""Consider the intervals $% A= {} %$ and $% B={}.%$ Find $% A\cap B%$.""".format(ut.latex(A),ut.latex(B))
==

eval_param ==
ut.LatexPrinter._settings.update({'interv_rev_brack': False})
kw_empty_set=['empty']
kw_infinity=['infty','inf','infinity']
==




