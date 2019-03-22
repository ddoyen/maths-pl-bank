extends = /template/mathbasic2.pl

title = Relation de divisibilité

lang = fr

before ==
angle=randitem([Rational(1,2),1,Rational(3,2),Rational(1,4),Rational(3,4),Rational(5,4)])*sp.pi
valangle=float(angle.evalf())
latexangle=latex(angle)
a=4
b=2
numsol=0
==

text ==
Déplacer le point $% M %$ de sorte que l'angle $% (\overrightarrow{OA},\overrightarrow{OM}) %$ ait une mesure égale à $% \displaystyle {{ latexangle }}. %$
==

form ==
{{input_1}}
==

input.1.type = radio

input.1.choices ==
{{a}} est divisible par {{b}}
{{b}} est divisible par {{a}}
Pas de relation entre {{a}} et {{b}}
==

input.1.numsol = {{numsol}}

evaluator ==
score=100
feedback=answer
==

