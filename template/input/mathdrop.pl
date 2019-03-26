extends = /template/mathbasic3.pl
drop_container =@ /input/drop/container.html
drop_build =
drop_script =@ /input/drop/script.js
drop_links =@ /input/drop/links.html
drag_build =
drag_script =
drag_links =
drag_container =@ /input/drop/container.html
text ==
Compléter les propositions suivantes.
==

before == 

==

form ==
$% 1 %$ {{ input_1 | safe }} $%\{1,2,3\}%$
<br>
$% \{1\} %$ {{ input_2 | safe }} $%\{1,2,3\}%$

<br>
<br>
Symboles : {{ input_in | safe }} {{ input_subset | safe }}
==

input.1.type = drop
input.2.type = drop
input.1.style = width: 3em; height: 2em
input.2.style = width: 3em; height: 2em
input.1.display =
input.2.display =

input.in.type = drag
input.subset.type = drag
input.in.style = width: 3em; height: 2em
input.subset.style = width: 3em; height: 2em
input.in.display = $$\in$$
input.subset.display = $$\subset$$

evaluator ==
score=100
feedback=answer
==


