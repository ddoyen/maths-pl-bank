	function allowDrop(ev) {
	    ev.preventDefault();
	}
	function drag(ev) {
	    ev.dataTransfer.setData("text", ev.target.id);
	}
	function drop(ev, target) { // target est l'id de la cible du drop "drop_name" ou "drag_container_name"
		ev.preventDefault();

		if (!ev.target.getAttribute("ondrop")) return false;
		// data est l'id de l'élément qu'on drag "drag_name"
		var data=ev.dataTransfer.getData("text");
		// Le drop
		document.getElementById(target).appendChild(document.getElementById(data));
		var input_ajax=document.getElementById('form_' + data);// on cherche le champ 'form_drag_name'
		if (target != undefined) input_ajax.value = target;
		if (target == undefined) input_ajax.value = '';
	}

