$(document).ready(function(){
	$("#btnBack").click(function(){
		navigator.app.backHistory();
	});

	$("#btnHome").click(function(){
		window.location.replace("main.html");
	});
});