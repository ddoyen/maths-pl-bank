extends = /template/mathbasic3.pl
mathexpr_container =@ /input/mathexpr/container.html
mathexpr_script =@ /input/mathexpr/script.js
mathexpr_links =@ /input/mathexpr/links.html


maxattempt = 2

form ==
{{input_1 | safe}}
==

input.1.type = mathexpr

input.1.virtualKeyboardMode = manual

input.1.virtualKeyboardMode = elementary





