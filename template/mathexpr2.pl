extends = /template/mathbasic.pl

html_mathexpr_tag =@ /inclusion_tags/mathexpr_tag.html


footerbefore ==
from jinja2 import Template

_strsympyvar={}
for _namevar in list(locals().keys()):
    if isinstance(locals()[_namevar],(Basic,Matrix)):
        _strsympyvar[_namevar]=str(locals()[_namevar])

def render_mathexpr_tag(dic):
	context = {'name':dic['name']}
	if 'style' in dic:
	    context['style'] = dic['style']
	else: 
		context['style'] = ''
	if 'display' in dic:
	    context['display'] = dic['display']
	else: 
		context['display'] = ''
    return Template(html_mathexpr_tag).render(context)

try:
  mathexpr_tags
except NameError:
	pass
else:
	for tag in mathexpr_tags:
    	locals()['input_mathexpr_'+tag['name']] = render_mathexpr_tag(tag)
==


style==
.mathfield {
    border: 1px solid #ddd;
    padding:5px;
    margin: 10px 0 10px 0;
    border-radius:5px;
    font-size: large;
    background-color: #fff;
}
#output {
    padding:5px;
    border: 1px solid #000;
}
==

