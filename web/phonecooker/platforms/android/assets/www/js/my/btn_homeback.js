$(document).ready(function(){
	$("#btnBack").click(function(){
		//navigator.app.backHistory();
		$('#header .leftButton').toggleClass('pressed');
		window.history.back();

	});

	$("#btnHome").click(function(){
		 $('#header .rightButton').toggleClass('pressed');
		window.location.replace("main.html");
		
	});
});

