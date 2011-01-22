/* Author: 
 */
$(function(){

    /* Autocomplete */
	
	// The array of Search objects to populate and send
	var SearchData = [];
	
	var defaultText = "Busca varias etiquetas y personajes";
    
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
		source: function(request, response){
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
			
			// populate the selected tag as a Search object
            SearchData.push(
                {
			     value: ui.item.value,
			     type: ui.item.type,
				 id: ui.item.id
                }
			)
			 			
            this.value = terms.join(", ");
            return false;
        }
    });
	
	$("#do_search").click(function(){
        // prevent multiple click at once
        $(this).attr("disabled", true)
	
        $.post('/', JSON.stringify(SearchData), function(data){
            console.log(data);
			// do what you have to do
		   
            // allow clicking again
            $(this).attr("disabled", false);
	   });
	});
});





















