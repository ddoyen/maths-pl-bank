*This document describes various input fields one may insert in the `form` tag of a `pl` math exercise, and the way they work from the point of view of one who writes an exercise*

`exercise.pl`refers to the file of the exercise being written.

# Drag and drop type fields

They require the template `mathdragdrop.pl` to be loaded, the first line of `exercise.pl` should thus be 

~~~~
extends = /template/mathdragdrop.pl
~~~~

The fields need to be declared in the  `before` tag of `exercise.pl` in two dictionaries named `drag_tags` and `drop_tags` as follows:

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
  - Drag and drop elements are inserted in the `form` tag of `exercise.pl` as in the example below.
  
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
