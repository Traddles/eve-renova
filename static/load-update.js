var myLink = "http://localhost:5111/unit";
var myLink2 = "http://localhost:5111/all/on";
var myResponseHandler = function() {
	if (this.readyState == 4 && this.status == 200) {
		console.log(this);
	}
};

// USE CREDENTIALS
var sendAjax = function(e) {
  var elements = this.getElementsByTagName('li');

  if(elements[0] == e.target || elements[0] == e.target.parentNode) {
  	console.log('0');
  }

  console.log(e.target);

  var req = new XMLHttpRequest();
  req.open('GET', myLink, true);
  req.onreadystatechange = myResponseHandler;
  req.send();
};

// USE CREDENTIALS
var reqJson = function(e) {

  console.log(e.target);

  var req = new XMLHttpRequest();
  req.open('GET', myLink2, true);
  req.setRequestHeader('Content-Type', 'application/xml');
  req.onreadystatechange = myResponseHandler;
  req.send();
};

/* NOT YET USED 
var sendCORSReq = function() {
	var xhr = new XMLHttpRequest();
	xhr.open('GET', myLink);
	xhr.onload = function(e) {
	  var data = JSON.parse(this.response);
	  console.log(this);
	}
	xhr.send();
}*/

document.getElementById('db-entries').addEventListener('click', sendAjax, false);
document.getElementsByTagName('h1')[0].addEventListener('click', reqJson, false);