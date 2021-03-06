(function(){

	var choices = document.querySelectorAll(".choice");

	for (var i=0; i < choices.length; ++i) {
		choices[i].addEventListener('click', loadPage, false);
	}

	function loadPage(e){
		var page_id = e.target.getAttribute("data-page-id");

		$.ajax({
    		type: 'GET',
        	url: page_id,
        	dataType: 'html', 
        	data: page_id,
        	success: function(data) {
        		$('#page').html(data);
            	}
    	});
	}
})();