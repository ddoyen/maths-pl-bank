*This document describes various so-called `template tags`  one may use in a `pl` math exercise, and the way they work from the point of view of one who writes the exercise. These `template tags` allow to insert complex `html` content in the `form` or `text` tag of the exercise.*

`exercise.pl`refers to the file of the exercise being written.

# Drag and drop type fields

They require the template `mathdragdrop.pl` to be loaded, the first line of `exercise.pl` should thus be 

~~~~
extends = /template/mathdragdrop.pl
~~~~

The fields need to be declared in the  `before` tag of `exercise.pl` in two lists named `drag_tags` and `drop_tags` as follows:

~~~~
before==
style = 'width: 3em; height: 2em'

drag_tags = [
    {'name':'papa', 'display':'$$\in$$', 'style': style},
    {'name':'maman', 'display':'$$\subset$$', 'style':style},
    {'name':'smiley', 'display':'😍', 'style':style}
]
drop_tags = [
  {'name':'papa', 'display':'אבא', 'style':style}, 
  {'name':'maman', 'display':'ماما', 'style':style}
]
==
~~~~

Drag elements are web page elements which can be moved around using the mouse or track pad, while drop  elements  are the page elements on which the drag elements may be dropped. 

Our implementation of the drag/drop scheme can be described as follows:
  - The information about which element was dropped where is contained in the dictionary `answer` with one field for each *drag* element. To each such element, whose name is `name` corresponds `answer['input_drag_name']` which, if it was dropped on the drop-element named `othername` holds as value the string `'drop_othername'`.
  - Drag elements can be dropped on drop elements, but can then be dragged back to their original location, or to another free drop location. 
  - Drag elements, as well as drop elements, are displayed as boxes (one color for drag  elements and another one for drop elements). Moreover they can display content which may be any html content including images, or Latex equations, etc... The boxes can be styled as in the above example by providing a list of `css` properties. These can be used to specify size, color, text style, etc...
  - The `style` and `display` fields in the description of a tag are optional, they both default to the empty string if they are not provided.
  - Drag and drop elements are inserted in the `form` or `text` tag of `exercise.pl` as in the example below.
  
~~~~
form==
Drag the appropriate symbol : {{ input_drag_smiley | safe }} {{ input_drag_maman | safe }}
{{ input_drag_papa | safe }}
<br>
On each of the following boxes : {{ input_drop_papa | safe }} {{ input_drop_maman | safe }}
==
~~~~  

The  `safe` filter for the tags is needed to prevent escaping of `html` content, as people familiar with  `jinja2` templates know.

Then an evaluator for `exercise.pl` could be as follows:

~~~~
evaluator ==
if (answer['drag_maman'] == 'drop_maman') and  (answer['drag_papa'] == 'drop_papa'): 
    score = 100
    numerror = 0
else : 
    score = 0
    numerror = 1
==
~~~~


# Resizable matrix input fields

They require the template `mathresizablematrix.pl` to be loaded, the first line of `exercise.pl` should thus be 

~~~~
extends = /template/mathresizablematrix.pl
~~~~

The resizable-matrix fields need to be declared in the  `before` tag of `exercise.pl` in a list named `resizable_matrix_tags` as in the following example, where the list holds a single tag description:

~~~~
before==
resizable_matrix_tags = [
{
    'name':'matrice',
    'max_rows':5,
    'max_cols':5,
    'cell_width':'3em',
    'cell_height':'2em',
    'input_style':'width:2em'
}]
==
~~~~

Resizable matrices are web page elements  consisting  of an array of `html` input fields surrounded by brackets. Moreover a hand tool allows to resize the array. They are used when a matrix is required as input from the user, but he also needs to set the right size for the matrix. 

In our implementation of resizable matrices:
  - The initial size of the matrix is 2 by 2. For the moment this is not parametrizable, nor are the minimum number of rows and columns.
  - The fields `max_rows` and `max_cols` specify to which dimensions the matrix is allowed to grow. The value of `max_rows` defaults to 5, while the value of `max_cols` defaults to that of `max_rows` if the latter is specified, and 5 otherwise.
  - The fields `cell_width` and `cell_height` hold the dimensions of each cell of the matrix. They default to reasonable values if they are not specified.
  - The field `input_style` is used to provide a list of `css` properties for the input field, whose dimensions should of course be smaller than those of the cell. These properties can be used to specify size, color, text style, etc... It defaults to the empty string.
  - For now a initial array of values may not be provided for the matrix. 
  - The values entered by the user in the input fields of the matrix with name `name` are returned in `answer['resizable_matrix_name']`. This is a python double list whose entries are thus accessed as `answer['resizable_matrix_name'][i][j]`, moreover indices run from 0, not 1. Each entry is a string, which therefore should be converted to be evaluated, if the expected input is an integer or sympy expression for instance. 
  named `othername` holds as value the string `'drop_othername'`.
  - Resizable matrix elements are inserted in the `form` tag of `exercise.pl` as in the example below.
  
~~~~
text==
Enter a 4 by 4 antisymmetric matrix $% A %$ with determinant equal to 1 below. 
form==
<div style="text-align:center">
$% A =%$  {{ input_resizable_matrix_A | safe }}
</div>
==
~~~~  

The  `safe` filter for the tags is needed to prevent escaping of `html` content, as people familiar with  `jinja2` templates know.

Then an evaluator for `exercise.pl` could be as follows:

~~~~
evaluator ==
A = answer['resizable_matrix_A']

score = 100
numerror = 0

m = len(A)
n = len(A[0])

for i in range(m):
    for j in range(n):
        A[i][j] = sympify(A[i][j])
A = Matrix(A)

if m != n : 
    score = 0
    numerror = 1
elif A != M.T:
    score = 0
    numerror = 1
elif A.det() != 1:
    score = 0
    numerror = 1
==
~~~~
