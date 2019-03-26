extends = /template/mathbasic3.pl
matrix_container =@ /input/matrix/container.html
matrix_build =@ /input/matrix/buildcontext.py

matrix_script =
matrix_links =@ /input/matrix/links.html

text =
before =

form ==
{{input_1 | safe}}
==

input.1.type = matrix
input.1.style = margin: 0 auto;
input.1.num_rows = 5
input.1.num_cols = 2
input.1.cell_width = 3em
input.1.cell_height = 3em
input.1.input_style = width:2em

