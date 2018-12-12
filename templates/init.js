function loadDoc() {
  var myObj, obj2, obj3, obj4, x, y, txt = "";
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      myObj = JSON.parse(this.responseText);
      obj1 = myObj['ketones_level']
      console.log(obj1)
      obj2 = myObj['glucose_level']
      obj3 = myObj['pain_level']
      txt += "<table border='1' style='float:left;'><tr><th colspan='2'>Ketones</th></tr>"
      for (x in obj1) {
        txt += "<tr><td>" + convertTimestamp(x) + "</td>";
        txt += "<td>" + obj1[x] + "</td></tr>";
      }
      txt +="</table>"
      txt += "<table border='1' ><tr><th colspan='2'>Glucose</th></tr>"
      for (x in obj2) {
        txt += "<tr><td>" + convertTimestamp(x) + "</td>";
        txt += "<td>" + obj2[x] + "</td></tr>";
      }
      txt +="</table>"
      txt += "<table border='1'><tr><th colspan='2'>Pain</th></tr>"
      for (x in obj3) {
        txt += "<tr><td>" + convertTimestamp(x) + "</td>";
        txt += "<td>" + obj3[x] + "</td></tr>";
      }
      txt += "</table>"
      document.getElementById("demo").innerHTML = txt;
    }
  };
  xhttp.open("GET", '/get/kuku', true);
  xhttp.send();
}

function getData() {
    var myObj, obj2, obj3, obj4;
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			myObj = JSON.parse(this.responseText);
			obj1 = myObj['ketones_level'];
            obj2 = myObj['glucose_level'];
            obj3 = myObj['pain_level'];
			var t = Object.keys(obj1).map(convertTimestamp);

            var ctx = document.getElementById("myChart").getContext('2d');
			var myChart = new Chart(ctx, {
				type: 'bar',
				data: {
					labels: t,
					datasets: [{
						label: 'Ketones level',
						data: Object.keys(obj1).map(function(key){return obj1[key]}),
						backgroundColor: 'rgba(255, 99, 132, 0.2)'
					},
					{
						label: 'Glucose level',
						data: Object.keys(obj2).map(function(key){return obj2[key]}),
						backgroundColor: 'rgba(54, 162, 235, 0.2)'

					},
					{
						label: 'Pain level',
						data: Object.keys(obj3).map(function(key){return obj3[key]}),
						backgroundColor: 'rgba(255, 206, 86, 0.2)'

					}
					]
				},
				options: {
					responsive: true,
					scales: {
						yAxes: [{
							ticks: {
								beginAtZero:true
							}
						}]
					}
				}
			});

            
		}
	};
	xhttp.open("GET", "/get/kuku", true);
	xhttp.send();
}


getData();

function convertTimestamp(timestamp) {
  var d = new Date(timestamp * 1000),	// Convert the passed timestamp to milliseconds
		yyyy = d.getFullYear(),
		mm = ('0' + (d.getMonth() + 1)).slice(-2),	// Months are zero based. Add leading 0.
		dd = ('0' + d.getDate()).slice(-2),			// Add leading 0.
		hh = d.getHours(),
		h = hh,
		min = ('0' + d.getMinutes()).slice(-2),		// Add leading 0.
		ampm = 'AM',
		time;

	if (hh > 12) {
		h = hh - 12;
		ampm = 'PM';
	} else if (hh === 12) {
		h = 12;
		ampm = 'PM';
	} else if (hh == 0) {
		h = 12;
	}

	// ie: 2013-02-18, 8:35 AM
	time = yyyy + '-' + mm + '-' + dd + ', ' + h + ':' + min + ' ' + ampm;

	return time;
}
