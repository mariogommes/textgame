choices = document.querySelectorAll(".choice");

for (var i=0; i < choices.length; ++i) {
	choices[i].addEventListener('click', save, false);
}

function  save(e){

	var karma = e.target.getAttribute("data-karma");
	var consequence	= e.target.getAttribute("data-conseq");
	var skill = e.target.getAttribute("data-skill");

	if ((karma != 0)  && (karma == 1)) { 
		localStorage.setItem("karma", localStorage.getItem("karma") + karma);
	 }

	 //continuar ...

	/* Example 

	// Store
		localStorage.setItem("lastname", "Smith");
	// Retrieve
		document.getElementById("result").innerHTML = localStorage.getItem("lastname");


	*/	
}