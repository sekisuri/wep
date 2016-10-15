<?php
include "db/db_info.php";
include "lib/config.php";
 ?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Av List</title>
        <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
   <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
   <!--[if lt IE 9]>
     <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
     <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
   <![endif]-->
   <link href="css/avrank.css" rel="stylesheet">


   	</head>
   	<body>
   		<!-- 헤더 -->
        <div class="header home">




    	</div>
    	<div class="box-padding-big">
            <div class="rank_list c7">

<?php

//$query ="SELECT * FROM `av_model` ORDER BY av_id DESC LIMIT 1,10";
$query = "SELECT * FROM av_model INNER JOIN mpb_rank ON av_model.av_krName = mpb_rank.av_krName ORDER BY  mpb_rank.rank_id";
$result = mysql_query($query, $conn);
while ($row=mysql_fetch_array($result)) {
    # code...
    $profile_pic = $site.$pic.$row['av_id'].".jpg";
 ?>
            <ul class="mactorul c7">
                <a href="http://www.mpb.kr/actor/1361">
                    <li class="main_img">
                        <img src=<?=$profile_pic?> data-original=<?=$profile_pic?> class="lazy" style="display: inline;">
                    </li>
                <li class="main_title">
                    <p><a href="http://www.mpb.kr/actor/1361" class="mactor"><?php echo $row['av_krName']; ?></a></p><span>데뷰 : <?php echo $row['av_debut'];?><br>출연작품 : 209개</span>
                </li>
                <li class="main_keyword">
                    <a href="http://www.mpb.kr/cup/I/1">
                        <span class="dataHref" data-href="http://www.mpb.kr/cup/I/1"><?=$row['av_bustcup']?></span></a>
                    <a href="http://www.mpb.kr/age/32/1">
                        <span class="dataHref" data-href="http://www.mpb.kr/age/32/1">32세</span></a>
                </li>
                <span class="ranking_icon"><?=$row['rank_id']?>위</span></a>
            </ul>
<?php

} // while($row=mysql_fetch_array($result))


mysql_close( $conn);
 ?>
                    </div>
    	</div>



    
    	<div class="dark-footer">

    	</div>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
   		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
   			<script>

   				$(function() {
   					$(window).scroll(function(e) {
   						if ($(this).scrollTop() > 750) {
   							$(".menu-top-home-fixed").css("margin-top", "0px");
   						} else {
   							$(".menu-top-home-fixed").css("margin-top", "-78px");
   						}
   					});
   				});

   			</script>
   	</body>
   </html>
