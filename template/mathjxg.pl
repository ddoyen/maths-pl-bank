extends = /template/mathbasic3.pl

jsxgraph_container =@ /input/jsxgraph/container.html
jsxgraph_script =@ /input/jsxgraph/script.js
jsxgraph_links =@ /input/jsxgraph/links.html


maxattempt = 1

form ==
{{input_1 | safe}}
==

input.1.type = jsxgraph

input.1.style = width:400px; height:400px; margin: 0 auto;

input.1.boardname = board






