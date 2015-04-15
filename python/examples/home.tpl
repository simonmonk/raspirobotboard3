<html>
<head>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js" type="text/javascript" charset="utf-8"></script>

<style>

.meters {
    border: 1px solid black;
}

.controls {
	width: 150px;
	font-size: 32pt;
	text-align: center;
	padding: 15px;
	background-color: green;
	color: white;
}
</style>

<script>
function sendCommand(command)
{
	$.get('/', {command: command});
}
</script>
</head>
<body>

<h1>Web Rover</h1>

<body>

<table align="center">
<tr><td></td><td class="controls" onClick="sendCommand('f');">F</td><td></td></tr>
<tr><td  class="controls" onClick="sendCommand('l');">L</td>
    <td  class="controls" onClick="sendCommand('s');">S</td>
    <td  class="controls" onClick="sendCommand('r');">R</td>
</tr>
<tr><td></td><td  class="controls" onClick="sendCommand('b');">B</td><td></td></tr>
</table>


</body>
</html>