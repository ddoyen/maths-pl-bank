# Modèle `mathexpr`

## Résumé

Ce modèle d'exercice offre un champ de réponse adapté à la saisie d'expressions mathématiques (nombres, expressions algébriques, fonctions, ensembles, etc.) La saisie se fait avec le clavier usuel ou avec un clavier virtuel attaché au champ de réponse et contenant les symboles mathématiques nécessaires. La saisie est automatiquement mise en forme en MathML.

Par ailleurs, ce modèle d'exercice permet l'utilisation de scripts Python pour la génération des données de l'exercice et l'évaluation de la réponse.

* **Inclusion :** `extends = /template/mathexpr.pl`

* **Dépendances :**
    * `extends = /template/mathbasic.pl`
    * `form =@ /form/form_MathLive.html`

* **Clés utilisées**: 
___


## Clés

`virtualKeyboards`

Définit les couches du clavier virtuel attaché au champ de réponse.

`before`

Script Python exécuté avant l'affichage de l'exercice. 

Un certain nombre de classes et de fonctions sont chargées par défaut :
- les principales classes et fonctions du module de calcul symbolique SymPy (https://docs.sympy.org) ;
- des fonctions de génération aléatoire d'objets SymPy ;
- des fonctions de conversion des objets SymPy en LateX.

```
before ==
A=rand_int_matrix(3,3,5)
sol=trace(A)
latexA=latex(A)
==
```

`text`

Enoncé de l'exercice.

`evaluator`

Script Python exécuté après chaque validation de la réponse.

Un certain nombre de classes et de fonctions sont chargées par défaut :
- les principales classes et fonctions du module de calcul symbolique SymPy (https://docs.sympy.org) ;
- des fonctions de génération aléatoire d'objets SymPy ;
- une fonction de conversion des objets SymPy en LateX ;
- des fonctions d'analyse des réponses.


## Exemples

### simplify_fraction.pl

```
extends = /template/mathexpr.pl

title = Simplification d'une fraction

lang = fr

virtualKeyboards = elementary

before ==
lst=[[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],[8,1],[9,1],[3,2],[4,3],[5,4],[5,3],[5,2],[6,5],[7,6],[7,5],[7,4],[7,3],[7,2],[8,7],[8,5],[8,3]]
f=randitem(lst)
rd.shuffle(f)
c=randint(2,6)
a,b=c*f[0],c*f[1]
sol=Rational(a,b)
==

text ==
Simplifier la fraction $%\displaystyle \frac{ {{a}} }{ {{b}} }%$ en l'écrivant sous la forme d'un entier ou d'une fraction irréductible.
==

evaluator==
score,_,texterror=ans_frac(answer['1'],sol)
feedback=fb.msg_analysis(score,texterror,lang)
==
```
