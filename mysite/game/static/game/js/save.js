choices = document.querySelectAll(".choice");

	for (var i=0; i < choices.length; ++i) {
		choices[i].addEventListener('click', save, false);
	}