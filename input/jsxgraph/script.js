var {{boardname}} = JXG.JSXGraph.initBoard('jxg_{{name}}',{{attributes |safe}});
{{ script.main | safe }}

{% if inputmode == 'retry' %}

var data = {{answer | safe}};

for (obj of board.objectsList){
    if (JXG.isPoint(obj) && obj.name != "") {
        obj.setPosition(JXG.COORDS_BY_USER,[parseFloat(data[obj.name+'_x']),parseFloat(data[obj.name+'_y'])]);
    }
}

{{boardname}}.fullUpdate();

{% endif %}

{% if inputmode == 'final' %}

var data = {{answer | safe}};

for (obj of board.objectsList){
    if (JXG.isPoint(obj) && obj.name != "") {
        obj.setPosition(JXG.COORDS_BY_USER,[parseFloat(data[obj.name+'_x']),parseFloat(data[obj.name+'_y'])]);
        obj.setAttribute({fixed: true});
    }
}

{{boardname}}.fullUpdate();

{{ script.solution | safe }}

{{boardname}}.removeEventHandlers();

{% endif %}



points=[]
for (obj of board.objectsList){
    if (JXG.isPoint(obj) && obj.name != "") {
        points.push(obj);
    }
}

for (obj of points){
    var inputx = document.createElement("input");
    inputx.id="form_"+obj.name+"_x";
    inputx.type = "hidden";
    document.getElementById('input').appendChild(inputx);  
    var inputy = document.createElement("input");
    inputy.id="form_"+obj.name+"_y";
    inputy.type = "hidden";
    document.getElementById('input').appendChild(inputy); 
}

function jxg_{{name}}_updateInput(){
    for (obj of points){
        document.getElementById("form_"+obj.name+"_x").value = obj.X();
        document.getElementById("form_"+obj.name+"_y").value = obj.Y();
    }

};

jxg_{{name}}_updateInput();

{{boardname}}.on('update',jxg_{{name}}_updateInput);





