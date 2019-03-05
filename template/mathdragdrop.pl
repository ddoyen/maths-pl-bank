extends = /template/mathbasic.pl

footerbefore ==
_strsympyvar={}
for _namevar in list(locals().keys()):
    if isinstance(locals()[_namevar],(Basic,Matrix)):
        _strsympyvar[_namevar]=str(locals()[_namevar])

def toy_render_template(html_string, dic):
	for key in dic:
		html_string = html_string.replace('{{ '+ key +' }}', dic[key])
	return html_string

html_drop_element =  """
    <div class = 'target'
		id = '{{ name }}'
		ondrop="drop(event, '{{ name }}')"
		ondragover='allowDrop(event)'
		style ='{{ style }}'>
		<span ondrop="drop(event, '{{ name }}')" ondragover='allowDrop(event)'> 
			{{ display }} 
		</span> 
	</div>
"""
html_drag_element =  """
    <div class = 'source'
		id = 'drag_{{ name }}'
		ondrop="drop(event, 'drag_{{ name }}')"
		ondragover='allowDrop(event)'
		style = '{{ style }}'>
		<div class = 'drag-display' id='display_{{ name }}' draggable='true' ondragstart='drag(event)'> 
			{{ display }} 
		</div>
	</div>
	<input type=hidden  id='form_drag_{{ name }}'>
"""

try:
  drop_tags
except NameError:
	drop_elements = []
else:
    drop_elements = [toy_render_template(html_drop_element, tag) for tag in drop_tags]


try:
  drag_tags
except NameError:
  drag_elements = []
else:
  drag_elements = [toy_render_template(html_drag_element, tag) for tag in drag_tags]
==


style==
	.target, .source, .drag-display {
	border : 2px solid Black;
	border-radius:6px;
	color:black;
	z-index:10;
	}

    div.target, div.source { /* les divs qui contiennent les champs drag-drop */
    display: inline-flex;
    border:none;
	margin : 6px;
	width : 3em;
	height : 2em;
    vertical-align:middle;
	text-align:center;
	justify-content: center;
	align-items: center;
}
div.target  {
	background:AntiqueWhite;
}
div.source  {
	background:Burlywood;
}
.drag-display {
	display:flex;
    position:absolute;
	background:inherit;
	height:inherit;
	width:inherit;
	justify-content: center;
	align-items: center;
	text-align:center;
	font-size: 1em;
	overflow:hidden;
}
==

script==
	function allowDrop(ev) {
	    ev.preventDefault();
	}
	function drag(ev) {
	    ev.dataTransfer.setData("text", ev.target.id);
	}
	function drop(ev, target) { // target est l'id de la source du drop{
		ev.preventDefault();

		if (!ev.target.getAttribute("ondrop")) return false;
		// data est l'id de la cible du drop
		var data=ev.dataTransfer.getData("text");
		// Le drop
		document.getElementById(target).appendChild(document.getElementById(data));
		var input_ajax=document.getElementById('form_drag_' + data.substring(8));// on enlève le "display_" du nom 
		if (target != undefined) input_ajax.value = target;
		if (target == undefined) input_ajax.value = '';
	}
== 

text==

==













