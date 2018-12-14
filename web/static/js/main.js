$(function() {
    $('#search').bind('keypress',function(event){  
        if(event.keyCode == "13"){
            window.location.href = "/searchpage?keyword="+event.target.value;
        }  
    });
    $.get('')
    $( "#search" ).autocomplete({
        source: function(request, response) {
            $.get('/search?keyword='+request.term,function(books){
                response(books)
            })
        },
        appendTo: '#result',
        open: function() { $('#result .ui-menu').width(300) } 
    });
  });