$(document).ready(function(){
	$("input:radio[name='radio']").click(function(){
		//var selectRadio = $(":radio[name='radio']:checked").val();
		//alert(selectRadio);
		consult_ajax();
	});
	//consult_ajax();
});

function consult_ajax()
{

	var queryUrl = "http://rubicone.cafe24.com/phonecooker/q.php?qdata=incentive";
	var tableIncentive = [];
	var selectRadio = $(":radio[name='radio']:checked").val();
	var telecomFirst = selectRadio + "_신규";
	var telecomMnp = selectRadio + "_MNP";
	var telecomChange = selectRadio + "_기변";


	tableIncentive.push("<tr>"); 
	tableIncentive.push("	<td>제조사</td>");
	tableIncentive.push("	<td>모델명</td>");
	tableIncentive.push("	<td>펫네임</td>");
	tableIncentive.push("	<td>신규</td>");
	tableIncentive.push("	<td>번호이동</td>");
	tableIncentive.push("	<td>기기변경</td>");
	tableIncentive.push("</tr>");
	//$("#tableIncentive").html(tableIncentive.join(""));

	$.ajax({
		url: queryUrl,
		dataType: 'jsonp',
		jsonpCallback: 'callback',
		success:function(data){
			$.each(data,function(key,val){
				if(val.제조사 != "")
				{
					tableIncentive.push("<tr>");
					tableIncentive.push("	<td>" + val.제조사 + "</td>");
					tableIncentive.push("	<td>" + val.모델명 + "</td>");
					tableIncentive.push("	<td>" + val.펫네임 + "</td>");
					tableIncentive.push("	<td>" + val[telecomFirst] + "</td>");
					tableIncentive.push("	<td>" + val[telecomMnp] + "</td>");
					tableIncentive.push("	<td>" + val[telecomChange] + "</td>");
					tableIncentive.push("</tr>");
				}
				else
				{

				}
				
			});
			$("#tableIncentive").html(tableIncentive.join(""));
		}

	});
}