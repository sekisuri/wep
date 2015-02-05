$(document).ready(function(){
	//sekisuri_150130 통신사 선택   <START
	$("#telecom_click").change(function(){
		var item_type = [];
		var getTelecom = $("#selectTelecom option:selected").val();
		item_type.push("<option value='none'>미선택</option>");
		item_type.push("<option value=신규>신규</option>");
		item_type.push("<option value=MNP>번호이동</option>");
		item_type.push("<option value=기변>기기변경</option>");

		$("#selectType").html(item_type.join(""));
		$("#selectModel").val("none");
		$("#selectCharge").val("none");
		$("#phone_modelcode").html("");	
		$("#phone_image").html("");

		/* 가격 리셋 */
		$("#origin_price").val("");
		$("#support_charge").val("");
		$("#final_price").val("");

		console.log("sale.js :: 20 Click #telecom_click")
	});
	//sekisuri_150130 통신사 선택   <END

	//sekisuri_150130 유형선택   <START
	$("#type_click").change(function(){
		var query = "http://rubicone.cafe24.com/phonecooker/q.php?qdata=model";
		var funType = "type_click";
		common_ajax(query,funType);
		
	});
	//sekisuri_150130 유형선택   <END

	//sekisuri_150130 모델선택   <START
	$("#model_click").change(function(){
		var query = "http://rubicone.cafe24.com/phonecooker/q.php?qdata=charge";
		var funType = "model_click";
		common_ajax(query,funType);
		var queryUrl = "http://rubicone.cafe24.com/phonecooker/q.php?qdata=incentive";
		incentiveAjax(queryUrl,funType);
	});
	//sekisuri_150130 모델선택  <END

	//sekisuri_150130  요금제 선택 <START
	$("#charge_click").change(function(){
		var query = "http://rubicone.cafe24.com/phonecooker/q.php?qdata=support";
		var funType = "charge_click";
		common_ajax(query,funType);
	});
	//sekisuri_150130  요금제 선택 <END
	

});

function common_ajax(queryUrl,clickType)
{
	var getTelecom = $("#selectTelecom option:selected").val(); // 통신사 
	var getType = $("#selectType option:selected").val(); // 유형
	var getModel = $("#selectModel option:selected").val(); // 모델
	var getModelText = $("#selectModel option:selected").text(); // 모델 펫네임
	var getCharge = $("#selectCharge option:selected").text();// 요금제이름 value에 공백문제땜시 선택된 텍스트로 가져옴 

	console.log("common_ajax :: 43 Click = " + clickType);
	console.log("common_ajax :: 44 url = " + queryUrl);
	console.log("common_ajax :: 45 getTelecom = " + getTelecom);
	console.log("common_ajax :: 46  getType = " + getType);
	console.log("common_ajax :: 47 getModel = " + getModel);
	console.log("common_ajax :: 48 getModelText = " + getModelText);
	console.log("common_ajax :: 49 getCharge = " + getCharge);

	var getOriginPrice = window.localStorage['판매_출고가']; // 출고가 
	console.log("sale.js :: 75 getOriginPrice = " + getOriginPrice);
//	var getSupport = $("#support_charge").val(); // 공시 지원금
	// 할부원
	var getSelectInstalment = $("#selectInstalment option:selected").val(); // 할부개월금

	var items = [];
	items.push("<option value='none'>미선택 </option>");

	$.ajax({
		url: queryUrl,
		dataType: 'jsonp',
		jsonpCallback: 'callback',
		success: function(data){
			
			$.each(data,function(key,val){

				switch(clickType)
				{
					case 'type_click':
					//sekisuri_150130 유형선택   <START
						if(val[getTelecom] != 0 || val[getTelecom] != "")
						{
							items.push("<option value=" + val.모델명 + ">" + val.펫네임 + "</option>");
							window.localStorage[val.모델명] = val[getTelecom];
							//  출고가격 로컬스토리지에 저장
						}

					//sekisuri_150130 유형선택   <END
					break;

					case 'model_click':
					//sekisuri_150130 모델선택   <START
						if(val.통신사 == getTelecom)
						{
							items.push("<option value=" + getTelecom + ">" + val.요금제명 + "</option>");
						}
					//sekisuri_150130 모델선택  <END
					break;

					case 'charge_click':
						if(val.모델명 == getModel)
						{
							
							var supportPrice = val[getCharge];
							var totalPrice = Number(getOriginPrice) - Number(val[getCharge]);
							console.log(clickType + "::supportPrice = " + supportPrice);
							console.log(clickType + "::totalPrice = " + totalPrice);
							console.log(clickType + "::val[getCharge] = " + val[getCharge]);
							console.log(clickType + "::getCharge = " + getCharge);
							console.log(clickType + "::getOriginPrice = " + getOriginPrice);

							window.localStorage['판매_공시지원금'] = supportPrice;
							window.localStorage['판매_할부원금'] = totalPrice;

							$("#origin_price").val($.number(getOriginPrice) + "원");
							$("#support_charge").val($.number(supportPrice) + "원");
							$("#final_price").val($.number(totalPrice) + "원");

						}
					break;

				}
				
			});

			switch(clickType)
			{
				case 'type_click':
				//sekisuri_150130 유형선택   <START
					$("#selectModel").html(items.join("")); // 모델 셀렉트 생성
					$("#selectCharge").val("none"); //상위선택시 하위 셀렉트 미선택으로
					$("#phone_modelcode").html("");	
					$("#phone_image").html("");

				//sekisuri_150130 유형선택   <END
				break;

				case 'model_click':
				//sekisuri_150130 모델선택   <START			
					$("#selectCharge").html(items.join(""));
					// sekisuri 2015/01/13 사진밑에 모델명 찍어줌 (후에 사진도 바꿔야 됨) START
					$("#phone_image").html("<img src=images/device/" + getModel + ".jpg width='100%' height='100% class='img-responsive>" );
					$("#phone_modelcode").html(getModel);	
					//sekisuri 2015/01/13 사진밑에 모델명 찍어줌 끝 END

					getOriginPrice = window.localStorage[getModel]; 
					//로컬 스토리지 출고가 
					console.log(clickType +" :: 159 getOriginPrice = " + getOriginPrice);
					window.localStorage['판매_출고가'] = getOriginPrice;
					//판매출고가 저장
					$("#origin_price").val($.number(getOriginPrice) + "원");
					//모델선택시 출고가 뿌려줌

					//하위 값 리셋 START
					$("#support_charge").val("");
					$("#final_price").val("");
					//하위 값 리셋 END
				//sekisuri_150130 모델선택  <END
				break;

			}
		
		},
		error: function(xhr){
			console.log('json Error',xhr);
		}


	});		

	console.log("----------function common_ajax()---------------");
	console.log("----------End---------------");

}

//sekisuri_   <START
function incentiveAjax(queryUrl,clickType)
{
	/* incentive json을 가져와 판매수익 저장하고 판매불가시 메시지 표시함 */
	var getTelecom = $("#selectTelecom option:selected").val(); // 통신사	
	var getType = $("#selectType option:selected").val();
	var getModel = $("#selectModel option:selected").val();
	var getIncenType = getTelecom + "_" + getType; 
	// sekisuri incentive.json:: 'SK + _ + 신규' SK예)SK_신규
	$.ajax({
		url: queryUrl,
		dataType: 'jsonp',
		//jsonpCallback: 'callback',
		success: function(data){
			$.each(data,function(key,val){
				if(val.모델명 == getModel)
				{
					console.log("sale.js::164 val.모델명 = " + val.모델명);
					console.log("sale.js::165 getIncenType = " +getIncenType);
					if(val[getIncenType] == "판매불가")
					{
						//$("#saleFail").show();
						//sekisuri_15130 판매불가 선택시 모델 출고가 초기화   <START
						alert("구입 및 판매불가");
						$("#selectModel").val("none");
						$("#origin_price").val("");
						//sekisuri_150130 판매불가 선택시 모델 출고가 초기화   <END
						$("#phone_modelcode").html("");	
						$("#phone_image").html("");
						//sekisuri 2015/01/13 사진밑에 모델명 최기화""

					}
					else
					{
						window.localStorage['판매_수수료'] = val[getIncenType];
						console.log("sale.js::173 판매수수료 = " + val[getIncenType]);
					}
				}
			});
		},
		error: function(xhr){
			console.log('json Error',xhr);
		}


	});
}
//sekisuri_   <END

//sekisuri_   <START
function clickModal()
{
	
	var getTelecom = $("#selectTelecom option:selected").val(); // 통신사 
	var getType = $("#selectType option:selected").val(); // 유형
	var getTypeText = $("#selectType option:selected").text(); // 유형 텍스트
	var getModel = $("#selectModel option:selected").val(); // 모델
	var getModelText = $("#selectModel option:selected").text(); // 모델 펫네임
	var getCharge = $("#selectCharge option:selected").text();// 요금제이름 value에 공백문제땜시 선택된 텍스트로 가져옴 

	var getOriginPrice = window.localStorage['판매_출고가']; // 출고가 
	var getSupport = window.localStorage['판매_공시지원금']; // 지원금
	var getFinal = window.localStorage['판매_할부원금']; // 할부원금 --콤마 제거
	var getSelectInstalment = $("#selectInstalment option:selected").val(); // 할부개월

	//sekisuri start
	var get_addSupport = $("#add_support").val(); // 추가지원금
	window.localStorage['판매_추가지원금'] = get_addSupport;
	getFinal = Number(getFinal) - Number(get_addSupport);
	// sekisuri end
	console.log("get_addSupport : " +get_addSupport );
	console.log("get_addSupport : " +getFinal );
	var monthModelPrice = Number(getFinal) / Number(getSelectInstalment); // 월 기기 요금 
	

	

	console.log("sale.js :: 75 getOriginPrice = " + getOriginPrice);

	var getTelecomPrice = '';// 통신요금 
	var getDiscount = ''; // 할인 -- 넣을지 말지 모르것다.
	var getTelecomTex = '';// 부가세
	var monthTelecomPrice = '';// 월 통신요금
	
	$.ajax({
			url: "http://rubicone.cafe24.com/phonecooker/q.php?qdata=charge",
			dataType: 'jsonp',
			jsonpCallback: 'callback',
			success: function(data){
				
				$.each(data,function(key,val){
					if(val.요금제명 == getCharge)
					{
						getTelecomPrice = val.기본요금;
						getDiscount = val.월할인금;
					}	
				});

				getDiscount = Number(getDiscount) + (Number(getDiscount) / 10); //  요금할인 부가서 더해줌
				getTelecomTex = Number(getTelecomPrice) / 10;
				monthTelecomPrice = Number(getTelecomPrice) + Number(getTelecomTex) - Number(getDiscount);
				

				window.localStorage['판매_월통신기본요금'] =getTelecomPrice;
				window.localStorage['판매_통신할인금액'] = getDiscount;
				window.localStorage['판매_통신부가세'] = getTelecomTex;
				window.localStorage['판매_월최종통신요금'] = monthTelecomPrice;


				

				var totalMonthPrice = Number(monthModelPrice) + Number(monthTelecomPrice) ; // 최종 월 납부금액-- 

				$("#price_header").html("요금제: " + getCharge + " <p>모델명: " + getModelText + "</p>"); //요금명, 모델명
				$("#modalType").html(getTypeText); // 유형
				$("#modalOriginPrice").html($.number(getOriginPrice) + "원"); // 출고가, 어차피 계산할필요 없어서 콤마찍힌거 가져옴 
				$("#modalSupport").html($.number(getSupport) + "원"); // 지원금
				$("#modalFinalPrice").html($.number(getFinal) + "원");	 // 할부원금
				$("#modalMonth").html(getSelectInstalment + "개월");	// 할부개월
				$("#modalMonthModel").html($.number(monthModelPrice) + "원  <p>(할부수수료 미포함)</p>"); // 월 기기 요금
				$("#modalMonthTelecom").html($.number(getTelecomPrice) + "원"); // 통신요금  -- 아직 통신요금 모름
				//
				$("#modalTelecomTex").html($.number(getTelecomTex) + "원");		//통신요금 부가세 -- 아직모름
				//$("#modalTotalTelecom").html($.number(monthTelecomPrice) + "원")	//월 요금
				$("#modalDiscount").html("-" + $.number(getDiscount) + "원  <p>(요금할인 부가세 포함)</p>"); // 할인 -- 요건 넣을지 말지 아직모름
				$("#modalTotalMonthPrice").html("<strong>" + $.number(totalMonthPrice) + "원 </strong>");	
				// 월 납부금 --통신요금을 몰라서 우선 월 기기요금으로...

			},
			error: function(xhr){
				console.log('json Error',xhr);
			}

		});		
		$("#myModal").modal('show');

}

//sekisuri_   <END

