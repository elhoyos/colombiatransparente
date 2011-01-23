/* 
 * Autocomplete para búsqueda de promesas
 * 
 * Author: elhoyos - juan.hoyosr@gmail.com
 * Requires: jQuery UI 1.8.9 (customized with Autocomplete widget)
 */
$(function(){
	
	// arreglo de objetos (tags) seleccionados para buscar promesas
	var SearchData = [];
	var defaultText = "Busca varias etiquetas y personajes";
    
	
	/* Utilidades */
	
	function split(val){
        return val.split(/,\s*/);
    }
    
    function extractLast(term){
        return split(term).pop();
    }
	
	function bindFocusEvents($autocomplete){
		$autocomplete.focusin(function(){
            $(this).val("");
	    }).blur(function(){
	        $(this).val(defaultText);
	    })
	}
	
	function unbindFocusEvents($autocomplete){
		$autocomplete.unbind()
	}
	
	
	/* Manejo de eventos */
	
    // regalemosle un autocomplete a la caja de búsqueda
    $("#search").bind("keydown", function(event){
		// evitemos que la caja de busqueda pierda el foco cuando se presione tab al
		// seleccionar un elemento
        if (event.keyCode === $.ui.keyCode.TAB &&
        $(this).data("autocomplete").menu.active) {
            event.preventDefault();
        }
    }).autocomplete({
		source: function(request, response){
            $.getJSON("/api/buscar_tag.json", {
				term: extractLast(request.term)
			}, response);
        },
        search: function(){
            // cantidad mínima de caracteres para empezar a buscar
            var term = extractLast(this.value);
            if (term.length < 2) {
                return false;
            }
        },
        focus: function(){
			// evitamos que se inserte el valor al seleccionarlo
            return false;
        },
        select: function(event, ui){
            var terms = split(this.value);
            // quita el último elemento
            terms.pop();
            // adicional el elemento selccionado
            terms.push(ui.item.value);
			// añade un "placeholder" para luego incluir la coma y el espacio al final
            terms.push("");
			
			// agrega el tag seleccionado al SearchData que será enviado luego
            SearchData.push(
                {
			     value: ui.item.value,
			     type: ui.item.type,
				 id: ui.item.id
                }
			);
			 			
            this.value = terms.join(", ");
            return false;
        }
    });
	
	// eventos para enviar la solicitud de búsqueda de promesas
	$("#do_search").click(function(){
		// evitamos multiples clicks
        //$(this).attr("disabled", true)
	
        $.get('/api/buscar_promesas.json', {
			terms: JSON.stringify(SearchData)
		}, function(data){
            console.log(data);
			// MISSING: afectar el DOM con las promesas retornadas
		   
            // habilitamos el botón
            //$(this).attr("disabled", false);
	   });
	}).ajaxError(function(e, xhr, settings, ex){
		// definimos lo que hay que hacer al terminar cada petición ajax
        if (settings.url == '/api/buscar_promesas.json') {
            alert(ex);
        }
    });
});