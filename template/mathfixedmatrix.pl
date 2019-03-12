extends = /template/mathbasic.pl

html_fixed_matrix_tag =@ /inclusion_tags/fixed_matrix_tag.html

footerbefore ==
from jinja2 import Template

_strsympyvar={}
for _namevar in list(locals().keys()):
    if isinstance(locals()[_namevar],(Basic,Matrix)):
        _strsympyvar[_namevar]=str(locals()[_namevar])

def render_fixed_matrix_tag(dic):
	context = {'name':dic['name']}

	if 'input_style' in dic:
	    context['input_style'] = dic['input_style']
	else: 
		context['input_style'] = 'width: 2em'

	if 'num_rows' in dic:
	    context['num_rows'] = dic['num_rows']
	else: 
		context['num_rows'] = 2

	if 'num_cols' in dic:
	    context['num_cols'] = dic['num_cols']
	else: 
		context['num_cols'] = 2

    if 'cell_width' in dic:
	    context['cell_width'] = dic['cell_width']
	else: 
		context['cell_width'] = '3em'

	if 'cell_height' in dic:
	    context['cell_height'] = dic['cell_height']
	else: 
		context['cell_height'] = '2em'

    matrix = []

    for i in range(context['num_rows']):
        matrix.append([])
        # each matrix entry is a couple, the first item is a string describing the position of the entry
        # the second item is the value displayed in the form, equal to True for an input field
        # or a provided value
        for j in range(context['max_cols']): 
            if 'mask' in dic:
	            entry_value = dic['mask'][i][j]
	        else: 
                entry_value = True
		    matrix[i].append([str(i)+str(j), entry_value])
    context['matrix']=matrix

    return Template(html_fixed_matrix_tag).render(context)

try:
    fixed_matrix_tags
except NameError:
	pass
else:
	for tag in fixed_matrix_tags:
    	locals()['input_fixed_matrix_'+tag['name']] = render_fixed_matrix_tag(tag)
==

headevaluator==
from sympy import Basic, Matrix
from sympy import sympify
from sympy import ln, sqrt
from sympy import trace
from sympy import evaluate
from utilsmath import *
if 'latexparam' in locals():
    LatexPrinter._settings.update(eval(latexparam))
for _namevar in list(_strsympyvar.keys()):
    with evaluate(False):
        locals()[_namevar]=sympify(_strsympyvar[_namevar])



# Construct a matrix from the form data, ie fixed_matrix_name_rows, fixed_matrix_name_cols 
# and the entries fixed_matrix_name_ij

try:
    fixed_matrix_tags
except NameError:
    pass
else:
    for tag in fixed_matrix_tags:
        matrix_name = 'fixed_matrix_'+tag['name']
        num_rows = int(answer[matrix_name+'_rows'])
        num_cols = int(answer[matrix_name+'_cols'])
        temp_matrix = []
        for i in range(num_rows):
            temp_matrix.append([])
            for j in range(num_cols):
                temp_matrix[i].append(answer[matrix_name+'_'+str(i)+str(j)])
        answer[matrix_name] = temp_matrix
==


style==
.matrix-input {
	border : none;
	border-radius:4px;
	text-align: center;
	font-style: italic;
	font-size: 12pt;
	color:black;
	background-color: LightGrey;
	z-index:10;
}

.absolute-center{
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.matrix{
    display:inline-block;
    position: relative;
    margin: 5px;
    vertical-align: middle;
}
.matrix:before, .resizable-matrix:after {
    content: "";
    position: absolute;
    top: 0;
    border: 2px solid #000;
    width: 6px;
    height: 100%;
}
.matrix:before {
    left: -6px;
    border-right: 0;
}
.matrix:after {
    right: -6px;
    border-left: 0;
}
    
.matrix-container {
    display: inline-block;
    overflow: hidden;
}
.resizable-matrix-table {
    table-layout:fixed;
}
.matrix-cell {
    margin:0;
    position:relative;
}
==

text==

==

