var myLink = "http://localhost:5111/unit";
var myLink2 = "http://localhost:5111/all/on";

var dbDataContainer = document.getElementById('db-entries');


function ajaxRequest(path = '') {
	var req = new XMLHttpRequest();
	req.open('GET', myLink, true);
	req.onreadystatechange = myResponseHandler;
	req.send();
}

var myResponseHandler = function() {
	if (this.readyState == 4 && this.status == 200) {
		var payload = JSON.parse(this.response);
		console.log(payload);
  		var elements = dbDataContainer.getElementsByTagName('li');
  		if(elements.length != payload._items.length) {
  			alert('Somethings wrong (payload mismatch).1');
  			return 0;
  		}
		for(i=0; i<payload._items.length; i++) {
			if(elements[i].dataset.id != payload._items[i]._id &&
				elements[i].dataset.state != payload._items[i].state) {
  				alert('Somethings wrong (payload mismatch).2');
			}
			elements[i].dataset.etag = payload._items[i]._etag;
		}
		console.log('Etag loading done');
	}
	else if (this.readyState == 4) {
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

$(document).ready(function() {
	ajaxRequest();
});

//dbDataContainer.addEventListener('click', sendAjax, false);
document.getElementsByTagName('h1')[0].addEventListener('click', reqJson, false);