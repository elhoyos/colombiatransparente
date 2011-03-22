/* 
 * ColombiaTransparente
 *
 * Requiere: 
 * - jQuery 1.5.1
 * - jQuery UI 1.8.9 (customized with Autocomplete widget)
 * 
 * Author: elhoyos - juan.hoyosr@gmail.com
 */

var CT = function() {
    var private_var;

    function private_method() {

    }

    return {
        
    }
}();


$(function(){

    CT.search = function() {
	    var SearchData = [];
	    var defaultText = "Busca varias etiquetas y personajes";
	    var $btnSearch = $("#do_search");
    
	
        function split(val) {
            return val.split(/,\s*/);
        }
        
        function extractLast(term) {
            return split(term).pop();
        }
	
        function extractFirst(term) {
            return split(term)[0];
        }
        
        // devuelve una url sin par�metros
        function getUrlWithoutParams(url) {
            if (url && url.length > 0)
                return url.split(/\?/)[0];
        }
        
        function bindFocusEvents($autocomplete) {
            $autocomplete.focusin(function() {
                $(this).val("");
            }).blur(function() {
                $(this).val(defaultText);
            })
        }
        
        function unbindFocusEvents($autocomplete) {
            $autocomplete.unbind()
        }
	
	
        /* Manejo de eventos */
	
        // regalemosle un autocomplete a la caja de b�squeda
        $("#search").bind("keydown", function(event) {
            // evitemos que la caja de b�squeda pierda el foco cuando se 
            // presione tab al seleccionar un elemento
            if (event.keyCode === $.ui.keyCode.TAB &&
            $(this).data("autocomplete").menu.active) {
                event.preventDefault();
            }
        }).bind("keyup", function(event) {
            if (event.keyCode === $.ui.keyCode.ENTER)
                SearchPromise();
        }).autocomplete({
            source: function(request, response) {
                $.getJSON("/api/buscar_tags.json", {
                    q: extractLast(request.term)
                }, response);
            },
            search: function() {
                // cantidad m�nima de caracteres para empezar a buscar
                var term = extractLast(this.value);
                if (term.length < 1) {
                    return false;
                }
                
                
            },
            focus: function() {
                // evitamos que se inserte el valor al seleccionarlo
                return false;
            },
            select: function(event, ui) {
                var terms = split(this.value);
                // quita el �ltimo elemento
                terms.pop();
                // adicional el elemento selccionado
                terms.push(extractFirst(ui.item.value));
                // a�ade un "placeholder" para luego incluir la coma y el 
                // espacio al final
                terms.push("");
                
                // agrega el tag seleccionado al SearchData que ser� 
                // enviado luego
                SearchData.push(
                    {
                     tipo: ui.item.tipo,
                     id: ui.item.id
                    }
                );
                            
                this.value = terms.join(", ");
                return false;
            }
        });
	
        // eventos para enviar la solicitud de b�squeda de promesas
        $("#do_search").click(function() {
            SearchPromise();
        });
        
        // busca promesas con los t�rminos dados
        function SearchPromise() {
            // evitamos multiples clicks
            $btnSearch.attr("disabled", true)
        
            $.get('/api/buscar_promesas/', {
                q: JSON.stringify(SearchData)
            }, function(data) {
                $("#promesas").html(data);
            });
        }
        
        // definimos lo que hay que hacer al terminar cada petici�n ajax
        $("body").ajaxComplete(function(e, xhr, settings) {
            // b�squeda de promesas
            if (getUrlWithoutParams(settings.url) == '/api/buscar_promesas/') {
                // habilitamos el bot�n
                $btnSearch.attr("disabled", false);
            }
        })
    }();


    // captura y env�o de los eventos del bot�n 'Like' de Facebook
    CT.like = function() {
        // objeto que encapsula los datos del evento
        var event = {
            // id del elemento
            id: $("#element_id").val(),

            // 0:promesa, 1:personaje: 2: etiqueta
            type: $("#element_type").val(), 
            
            // true para 'like' o false 'unlike'
            like: true
        };

        return {
            // enviamos el evento al servidor
            sendEvent: function(like) {
                if (typeof like != "boolean")
                    return;

                event.like = like;

                $.post("/api/registrar_evento_likebtn.json", event);
            }
        }
    }();
});
