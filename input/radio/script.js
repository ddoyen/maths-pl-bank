{% if inputmode == 'retry' or inputmode == 'final' %}

var answer = {{answer | safe}};

for (var i = 0; i < {{ choices|length }}; i++) {
    if ('{{name}}_'+i.toString() in answer) {
        document.getElementById('form_{{name}}_'+i.toString()).checked = true;
    }
}

{% endif %}

{% if inputmode == 'final' %}

document.getElementById('label_{{name}}_{{numsol}}').className ="text-success";

{% endif %}

