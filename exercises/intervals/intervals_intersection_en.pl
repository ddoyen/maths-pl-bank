extends = /exercises/intervals/intervals_intersection.pl

title = Intersection of intervals

lang = en

param = {"interv_rev_brack": False}

text == 
Consider the $% A= {{latexA}} %$ et $% B={{latexB}}.%$ Déterminer $% A\cap B%$.
==

evaluator ==
sol=sp.sympify(strsol)
score,numerror,texterror=ut.ans_interval(response['answer'],sol,kw_empty_set=['vide'],kw_infinity=['infini','inf'])
feedback=fb.msg_analysis(score,texterror,lang)
==





