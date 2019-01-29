extends = /exercises/templates/basicmath.pl

title = Intersection d'intervalles

lang = fr

param = {"interv_rev_brack": True}

before ==
val=ut.list_randint_norep(4,-5,5)
val.sort()
interv=[ut.rand_interval_type(val[0],val[2]),ut.rand_interval_type(val[1],val[3])]
rd.shuffle(interv)
A,B=interv
sol=sp.Intersection(A,B)
strsol=str(sol)
latexA=ut.latex(A)
latexB=ut.latex(B)
==

text == 
On considère les intervalles $% A= {{latexA}} %$ et $% B={{latexB}}.%$ Déterminer $% A\cap B%$.
==

form_help ==
Pour désigner l'ensemble vide, écrire &laquo; vide &raquo;.
==





evaluator ==
sol=sp.sympify(strsol)
score,numerror,texterror=ut.ans_interval(response['answer'],sol,kw_empty_set=['vide'],kw_infinity=['infini','inf'])
feedback=fb.msg_analysis(score,texterror,lang)
==







