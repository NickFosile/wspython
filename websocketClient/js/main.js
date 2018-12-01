var wsClient;

function hideInit() {
	document.getElementById('initiation');
	document.style.display = "none";
}

function showInit() {
	document.getElementById('initiation');
	document.style.display = 'block';
}

/*Websockets callbacks*/
function connectionAchieved(e) {
	alert("Connection made");
}

function msgReceived(e) {
	alert("received msg");
}

function connectionClosed(e) {
	alert("connection closed or wasn't established");
}

function connect() {
	if(!("WebSocket" in window)) {
		alert("Your browser doesn't support websockets");
		return;
	}
	let host = document.getElementById('host').value;
	let prot = document.getElementById('proto');
	let protocol = prot.options[prot.selectedIndex].value;
	if (host === null || host === undefined || host === '') {
		host = "localhost";
	}
	let port = document.getElementById('port').value;
	if(port === null || port === undefined || port === "") {
		port = 80;
	}
	let connector = "";
	if(parseInt(protocol) === 1) {
		connector += "ws://";
	}
	else if(parseInt(protocol) === 2) {
		connector += "wss://";
	}
	connector += host + ":";
	connector += port.toString();
	alert(connector);
	var webS = new WebSocket(connector);
	webS.onopen = connectionAchieved;
	webS.onmessage = msgReceived;
	webS.onclose = connectionClosed;
	swClient = webS;
	
}

let connectionBtn = document.getElementById('connect');
connectionBtn.addEventListener('click', connect);
