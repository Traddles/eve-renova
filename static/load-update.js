
var myResponseHandler = function() {
	if (this.readyState == 4 && this.status == 200) {
		console.log(this);
	}
};

var sendAjax = function() {
  var req = new XMLHttpRequest();
  req.open('GET', 'http://localhost:5111/all/on', true);
  req.onreadystatechange = myResponseHandler;
  req.send();
};
document.getElementById('db-entries').addEventListener('click', sendAjax, false);