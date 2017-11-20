<html>
<head>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js" type="text/javascript" charset="utf-8"></script>

<style>

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

function keyPress(event){
	code = event.keyCode;
	if (code == 119) {
		sendCommand('f');
	}
	else if (code == 97) {
		sendCommand('l');
	}
	else if (code == 115) {
		sendCommand('s');
	}
	else if (code == 100) {
		sendCommand('r');
	}
	else if (code == 122) {
		sendCommand('b');
	}
}

$(document).keypress(keyPress);

</script>
</head>
<body>

<h1>Web Rover</h1>

<table align="center">
<tr><td></td><td class="controls" onClick="sendCommand('f');">W</td><td></td></tr>
<tr><td  class="controls" onClick="sendCommand('l');">A</td>
    <td  class="controls" onClick="sendCommand('s');">S</td>
    <td  class="controls" onClick="sendCommand('r');">D</td>
</tr>
<tr><td></td><td  class="controls" onClick="sendCommand('b');">Z</td><td></td></tr>
</table>


</body>
</html>