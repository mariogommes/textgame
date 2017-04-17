(function(){

	choices = document.querySelectorAll(".choice");

	for (var i=0; i < choices.length; ++i) {
		choices[i].addEventListener('click', loadPage, false);
	}

	function loadPage(e){
		page_id = e.target.getAttribute("data-page-id");
		console.log(page_id);

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