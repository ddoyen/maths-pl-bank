extends = /template/input/mathexpr.pl

title = Ensemble de définition (logarithme 1)

lang = fr

virtualKeyboards = sets

before ==
a=randint(-6,6,[0,1,-1])
b=randint(-6,6,[0])
x=symbols('x')
f=ln(a*x+b)
latexf=latex(f)
from sympy.solvers.inequalities import solve_univariate_inequality
sol = solve_univariate_inequality(a*x+b > 0, x, relational=False)
==

text ==
Déterminer l'ensemble de définition de la fonction $%f : x \mapsto {{latexf}}%$.
==

evaluator==
score,_,feedback=ans_interval(answer['1'],sol)
==

