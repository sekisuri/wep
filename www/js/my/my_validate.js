$(document).ready(function(){
	$("#btnModal").click(function(){

		var getTelecom = $("#selectTelecom option:selected").val();
		var getType = $("#selectType option:selected").val();
		var getModel = $("#selectModel option:selected").val();
		var getCharge = $("#selectCharge").val();
		var getInstalment = $("#selectInstalment").val();

		if(getTelecom == "" || getTelecom == "none")
		{
			alert("통신사를 선택해주세요.");
			return false;
		}
		if(getType == "" || getType == "none")
		{
			alert("유형을 선택해주세요.");
			return false;
		}
		if(getModel == "" || getModel == "none")
		{
			alert("휴대폰을 선택해주세요.");
			return false;
		}
		if(getCharge == "" || getCharge == "none")
		{
			alert("요금제를 선택해주세요.");
			return false;
		}
		if(getInstalment == "" || getInstalment == "none")
		{
			alert("할부개월을 선택하세요.");
			return false;
		}


	});
});