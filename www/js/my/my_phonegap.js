$(document).ready(function(){

	document.addEventListener("deviceready", onDeviceReady, false);

});

function onDeviceReady() {
		document.addEventListener("backbutton", ShowExitDialog, false);
}

function ShowExitDialog() {
	navigator.notification.confirm(
	("종료할까요?"), // message
	alertexit, // callback
	'Phone Cooker', // title
	'예,아니요' // buttonName
	);

}

function alertexit(button){
	if(button=="1" || button==1)
	{

	navigator.app.exitApp();
	}
}