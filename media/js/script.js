/* Author: 
 */
$(function(){

    /* Autocomplete */
	
	var defaultText = "Busca varias etiquetas y personajes"
    
    var availableTags = [
        "ActionScript",
        "AppleScript",
        "Asp",
        "BASIC",
        "C",
        "C++",
        "Clojure",
        "COBOL",
        "ColdFusion",
        "Erlang",
        "Fortran",
        "Groovy",
        "Haskell",
        "Java",
        "JavaScript",
        "Lisp",
        "Perl",
        "PHP",
        "Python",
        "Ruby",
        "Scala",
        "Scheme"
    ];
    
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
    

    $("#search").bind("keydown", function(event){
        // don't navigate away from the field on tab when selecting an item
        if (event.keyCode === $.ui.keyCode.TAB &&
        $(this).data("autocomplete").menu.active) {
            event.preventDefault();
        }
    }).autocomplete({
		minLength: 0,
        source: function( request, response ) {
            // delegate back to autocomplete, but extract the last term
            response( $.ui.autocomplete.filter(
                availableTags, extractLast( request.term ) ) );
        },
        focus: function() {
            // prevent value inserted on focus
            return false;
        },
        select: function( event, ui ) {
            var terms = split( this.value );
            // remove the current input
            terms.pop();
            // add the selected item
            terms.push( ui.item.value );
            // add placeholder to get the comma-and-space at the end
            terms.push( "" );
            this.value = terms.join( ", " );
            return false;
        }
        /*source: function(request, response){
            $.getJSON("XXXXX", {
                term: extractLast(request.term)
            }, response);
        },
        search: function(){
            // custom minLength
            var term = extractLast(this.value);
            if (term.length < 2) {
                return false;
            }
        },
        focus: function(){
            // prevent value inserted on focus
            return false;
        },
        select: function(event, ui){
            var terms = split(this.value);
            // remove the current input
            terms.pop();
            // add the selected item
            terms.push(ui.item.value);
            // add placeholder to get the comma-and-space at the end
            terms.push("");
            this.value = terms.join(", ");
            return false;
        }*/
    });
});





















