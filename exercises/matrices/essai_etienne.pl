extends = /template/mathexpr.pl

title = Trace d'une matrice

lang = fr

matsize = 3

coeffbound = 5

before ==
M = Matrix([[1, -1], [3, 4], [0, 2]])
==

text ==
==

form ==
$% M = %$ <input id='form_M'></input>
==


evaluator ==
score,_,feedback=ans_number(answer['M'],43)
latexM = latex(M)
==

solution ==
$% M = {{ latexM }} %$
==


