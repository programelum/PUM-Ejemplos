<h1>Conversion de Coordenadas</h1>

<form>
RA: <input type="text" name="RA" value="<?echo $_GET['RA']?>"><br/>
DEC: <input type="text" name="DEC" value="<?echo $_GET['DEC']?>"><br/>
<input type="submit" value="Convertir">
</form>

<?php
$RA=$_GET["RA"];
$DEC=$_GET["DEC"];
$salida=shell_exec("python coordenadas.py $RA $DEC");
$resultados=split(" ",$salida);
echo "LAT. ECL. = $resultados[0]<br/>";
echo "LON. ECL. = $resultados[1]<br/>";
?>
