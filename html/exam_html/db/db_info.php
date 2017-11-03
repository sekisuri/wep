<?php
include "dbset.php";
$conn=@mysql_connect("{$localhost}","{$user}","{$pass}") or die('DB ERROR!!!'.mysql_error());
mysql_set_charset("utf8",$conn);
@mysql_select_db($user, $conn) or die('DB Connect Error');

?>
