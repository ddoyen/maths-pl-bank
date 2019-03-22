{%if inputmode == 'initial' or inputmode == 'retry' %}

var mathexpr_{{name}} = MathLive.makeMathField('mathexpr_{{name}}', {
onContentDidChange: mathfield => {
    document.getElementById('form_{{name}}').value = mathexpr_{{name}}.latex();
},
smartFence:false,
inlineShortcuts: { '*': '\\times'},
{% if  virtualKeyboardMode %}
virtualKeyboardMode: 'manual',
{% else %}
virtualKeyboardMode: '{{ virtualKeyboardMode }}',
{% endif %}
customVirtualKeyboardLayers: headVirtualKeyboardLayers,
customVirtualKeyboards: {
    'elementary': {
        label: 'Elémentaire',
        tooltip: 'Elémentaire',
        layer: 'elementary'
    },
    'sets': {
        label: 'Ensembles',
        tooltip: 'Ensembles',
        layer: 'sets'
    }
},
virtualKeyboards: '{{ virtualKeyboards }}'
}
);

{%if answer %}

var data = {{answer | safe}};
mathexpr_{{name}}.$insert(data['{{name}}']);
mathexpr_{{name}}.$perform('moveToMathFieldEnd');

{% endif %}

{% endif %}

{%if inputmode == 'final' %}

var data = {{answer | safe}};
document.getElementById('mathexpr_{{name}}').innerHTML = "$$" + data['{{name}}'] + "$$";
MathLive.renderMathInElement('mathexpr_{{name}}');

{% endif %}

