
<body>
	<div>
		<h2><a href="index.php">Principal</a></h2>
	</div>
	<table>
		<tr>
			<td>
				<fieldset>
					<legend>===Arrays===</legend>
					<?php 
						$shoppingList[0] = 'wine';
						$shoppingList[1] = 'fish';
						$shoppingList[2] = 'bread';
						$shoppingList[3] = 'grapes';
						$shoppingList[4] = 'cheese';

						#$shoppingList = ['wine', 'fish', 'bread', 'grapes', 'cheese'];
						#$shoppingList = array('wine', 'fish', 'bread', 'grapes', 'cheese');
						foreach ($shoppingList as $lista) {
							echo "===> ".$lista . '<br>';
						}
					 ?>					
				</fieldset>	
				
				<fieldset>
					<legend>array_simple</legend>
					<?php 
					   $arrSimple = array("uno","dos","tres");
					   
					   foreach ($arrSimple as $arr)
					       echo "$arr <br/>";
    					echo '<hr>';
    					
    					foreach ($arrSimple as $clave => $valor){
    					    echo "$clave => $valor <br/>";
    					 }    					     					 
    					 //echo '<br>';
    					 echo  '<hr>';
    					 
    					 echo '===== tabla multiplicar ===== <br>';
    					 
    					 echo '<table> <tr>';
    					 
    					 for ($i=1; $i <=12; $i++){
    					     echo "<td> $i</td>";
    					     //echo '<tr>';
    					     echo "<tr><td>$i";
    					     
    					     for ($k=$i; $k<12; $k++){
    					       echo "<td>$i*$k</td>";     
    					     }
    					     echo "<br>";
    					     echo "</td></tr>";
    					     
    					 }
    					 
    					 
    					 
					?>
				</fieldset>	
			</td>

			<td>
				<fieldset style="width: 200px;">
					<legend>associative array</legend>
					<?php 
						$book = [
							'title' => 'PHP 7 Solutions: Dynamic Web Design Made Easy, Fourth Edition',
							'author' => 'David Powers',
							'publisher' => 'Apress'];
						foreach ($book as $key => $value) {
							echo "clave:".$key." :::> ".$value . '<br>';
						}
					 ?>
				</fieldset>
			</td>

			<td>
				<fieldset>
					<legend>arrays--array(array))</legend>
					<?php 

						$fruits = array(1=>'banana', 'color'=> 'amarillo', 'geometria'=>'curvapolimorfico');
						array(2 => 'naranja', 'color'=> 'anaranjado', 'geometria'=>'circular' );
						foreach ($fruits as $key => $value) {
							echo $key."::: ". $value . '<br>';
						}

					 ?>
				</fieldset>
			</td>
		</tr>
	</table>



</body>


<?php 
	
	$cars = array("Volvo", "BMW", "Toyota");
echo "I like " . $cars[0] . ", " . $cars[1] . " and " . $cars[2] . ".";

$cars = array("Volvo", "BMW", "Toyota");
echo count($cars);
?>
//---
<?php
$cars = array("Volvo", "BMW", "Toyota");
$arrlength = count($cars);

for($x = 0; $x < $arrlength; $x++) {
  echo $cars[$x];
  echo "<br>";
}

///............
$age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");

foreach($age as $x => $x_value) {
  echo "Key=" . $x . ", Value=" . $x_value;
  echo "<br>";
}

//...............
$cars = array (
  array("Volvo",22,18),
  array("BMW",15,13),
  array("Saab",5,2),
  array("Land Rover",17,15)
);

for ($row = 0; $row < 4; $row++) {
  echo "<p><b>Row number $row</b></p>";
  echo "<ul>";
  for ($col = 0; $col < 3; $col++) {
    echo "<li>".$cars[$row][$col]."</li>";
  }
  echo "</ul>";
}

	//..sorting arrays....
/*
sort() - sort arrays in ascending order
rsort() - sort arrays in descending order
asort() - sort associative arrays in ascending order, according to the value
ksort() - sort associative arrays in ascending order, according to the key
arsort() - sort associative arrays in descending order, according to the value
krsort() - sort associative arrays in descending order, according to the key
*/

$cars = array("Volvo", "BMW", "Toyota");
sort($cars);
	
$age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");
asort($age);


 ?>