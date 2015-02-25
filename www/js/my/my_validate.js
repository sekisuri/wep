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

		clickModal();

	});
	$("#btn_closeModal").click(function(){
		$("#myModal").modal('hide');
		$("#selectTelecom").val("none");
		$("#selectType").val("none");
		$("#selectModel").val("none");
		$("#selectCharge").val("none");
		$("#phone_modelcode").html(""); // sekisuri 시진텍스트 초기화
		$("#inputCode").html("");
		$("#inputCode").attr("placeholder", "판매사 코드입력");
		$("#phone_modelcode").html("");	
		$("#phone_image").html("");//sekisuri 2015/01/13 사진밑에 모델명 최기화""
		
		//가격 리셋 
		$("#origin_price").val("");
		$("#support_charge").val("");
		$("#final_price").val("");
		$("#add_support").val("");
		$("#add_support").attr("placeholder", "0");
		$("#selectInstalment").val("none");

	});
});