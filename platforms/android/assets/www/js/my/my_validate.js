$(document).ready(function(){
	$("#btnModal").click(function(){

		var getTelecom = $("#selectTelecom option:selected").val();
		var getType = $("#selectType option:selected").val();
		var getModel = $("#selectModel option:selected").val();
		var getCharge = $("#selectCharge").val();
		var getInstalment = $("#selectInstalment").val();

		if(getTelecom == "" || getTelecom == "none")
		{
			my_alert("통신사를 선택해주세요.");
			return false;
		}
		if(getType == "" || getType == "none")
		{
			my_alert("유형을 선택해주세요.");
			return false;
		}
		if(getModel == "" || getModel == "none")
		{
			my_alert("휴대폰을 선택해주세요.");
			return false;
		}
		if(getCharge == "" || getCharge == "none")
		{
			my_alert("요금제를 선택해주세요.");
			return false;
		}
		if(getInstalment == "" || getInstalment == "none")
		{
			my_alert("할부개월을 선택하세요.");
			return false;
		}
		clickModal();

	});
	$("#btn_closeModal").click(function(){
		$("#myModal").modal('hide');
		$("#selectTelecom").val("none");
		$("#selectType").val("none");
		$("#selectModel").val("none");
		$("#selectCharge").val("none");

		//가격 리셋 
		$("#origin_price").val("");
		$("#support_charge").val("");
		$("#final_price").val("");
		$("#selectInstalment").val("none");
	});
});