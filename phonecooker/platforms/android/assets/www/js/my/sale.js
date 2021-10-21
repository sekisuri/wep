$(document).ready(function(){

	//$("#saleFail").hide();
	//$("#loading").hide();

//sekisuri_150130 월청구금액 버튼 모달   <START
/* my_validate.js 로 옴김
	$("#btnModal").click(function(){
		$("#myModal").modal('show');
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
*/
//sekisuri_150130 월청구금액 버튼 모달   <END

	//sekisuri_150129   <START

/*
	jQuery('#extendAddSupport').keyup(function () {     
	  this.value = this.value.replace(/[^0-9\.]/g,'');

	  var final_incentive = window.localStorage['판매_최종수수료'];
	  var getFinal = window.localStorage['판매_할부원금']; // 할부원금 --콤마 제거
	  getFinal = getFinal - this.value;
	  final_incentive = final_incentive - this.value;
	  window.localStorage['판매_할부원금'] = getFinal;
	  window.localStorage['판매_최종수수료'] = final_incentive;
	  $("#extendFinal").val($.number(getFinal)); // 할부원금
	  $("#extendIncentive").val($.number(final_incentive));

	  

	});
*/ 

	$("#btnReIncentive").click(function(){
		getAddIncentive = $("#extendAddSupport").val();
		getFinalIncentive = window.localStorage['판매_최종수수료'];
		reFinalIncentive =  Number(getFinalIncentive) - Number(getAddIncentive);
		$("#extendIncentive").val($.number(reFinalIncentive));
	});
	$("#btnCode").click(function(){
		var getModel = $("#selectModel option:selected").val(); // 모델
		var getTelecom = $("#selectTelecom option:selected").val(); // 통신사 
		var getCharge = $("#selectCharge option:selected").text();// 요금제이름 value에 공백문제땜시 선택된 텍스트로 가져옴  
		var getType = $("#selectType option:selected").val();
		var getTypeText = $("#selectType option:selected").text();
		var getMinus = getType + "_" + getCharge;
		var getCode = $("#inputCode").val();// 판매사 코드

		var getOriginPrice = window.localStorage['판매_출고가']; // 출고가 
		var getSupport = window.localStorage['판매_공시지원금']; // 지원금
		var getIncentive = window.localStorage['판매_수수료'];
		var getTelecomPrice = window.localStorage['판매_월통신기본요금'];
		var getFinal = window.localStorage['판매_할부원금']; // 할부원금 --콤마 제거
		var getAddSupport = window.localStorage['판매_추가지원금'];
		var is_IDcheck = false;
		console.log("click btnCode!!!");

		//sekisuri_150130  수수료 모드 <START
		$("#extendTelecom").val(getTelecom); //통신사
		$("#extendOrigin").val($.number(getOriginPrice)); //출고가격
		$("#extendType").val(getTypeText); //유형
		$("#extendSupport").val($.number(getSupport)); // 공시 지원금
		$("#extendModel").val(getModel); // 모델
		$("#extendAddSupport").val($.number(getAddSupport));//$("#extendAddSupport").val("0");// 추가 지원금
		$("#extendTelecomPrice").val(getCharge); //요금제
		$("#extendFinal").val($.number(getFinal)); // 할부원금
		//sekisuri_150130 수수료 모드   <END
		$.ajax({
			url:"http://rubicone.cafe24.com/phonecooker/q.php?qdata=user",
			dataType: 'jsonp',
			jsonpCallback:'callback',
			success:function(data){
				$.each(data,function(key,val){
					

					if(val.아이디 == getCode)
					{
						
						is_IDcheck = true;
						//return;
						
					}														
					else
					{
						//is_IDcheck = false;
					//	$("#inputColor").addClass("form-group has-error");
						//$("#inputCode").val('');
						//$("#inputCode").attr("placeholder", "판매사코드가 틀립니다.");
						
						//return false;
					}

				});
				if(is_IDcheck == true)
				{
					$.ajax({
						url:"http://rubicone.cafe24.com/phonecooker/q.php?qdata=minus",
						dataType: 'jsonp',
						//jsonpCallback:'mycall',
						success:function(data){
							$.each(data,function(key,val){
								if(val.모델명 == getModel)
								{
									var final_incentive = Number(getIncentive) - Number(val[getMinus]) - Number(getAddSupport);
									console.log("sale.js::43 getIncentive : " + getIncentive);
									console.log("sale.js::44 val[getMinus] : " + val[getMinus]);
									console.log("sale.js::45 final_incentive : " + final_incentive);
									$("#extendIncentive").val($.number(final_incentive));
									window.localStorage['판매_최종수수료'] = final_incentive;

								}
							//	console.log("sale.js::49 getMinus : " +getMinus);
							});
							$("#goMain").hide(); //월청구금액 버튼
							$("#goTotal").show(); //전체 수수료 버튼
							$('#modalMainContents').hide();
							$('#modalExtendTotal').hide();
							$('#modalExtendIncentive').show();

						}
					});
				}
				else
				{
					alert("판매사코드가 틀립니다.");
				}
			}
		});
	});
	//sekisuri_150129   <END

	

});
function btnClick()
{
	alert("준비중");
}