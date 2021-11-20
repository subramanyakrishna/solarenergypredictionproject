function onfocusSubmit() {
  var x = document.getElementById("citytofocus").value;
  var spanCity = document.getElementById("spanCity");
  if (x == "") {
    spanCity.innerHTML = "Enter complete name of your city";
    spanCity.style.color = "red";
  } else {
    spanCity.innerHTML = "";
    fetch(
      "https://api.opencagedata.com/geocode/v1/json?q=" +
        x +
        "&key=f2740148ebe74bcba317ceac0f432b63&language=en&pretty=1&no_annotations=1"
    )
      .then((response) => response.json())
      .then((data) => {
        if (data["results"].length == 0) {
          spanCity.innerHTML = "Enter valid city name";
          spanCity.style.color = "red";
        } else {
          spanCity.innerHTML = "";
          lat = data["results"][0]["geometry"]["lat"];
          lng = data["results"][0]["geometry"]["lng"];
          document.getElementById("lat").value = lat.toFixed(4);
          document.getElementById("long").value = lng.toFixed(4);
          mymap.flyTo([lat, lng], 13);
        }
      });
  }
}

function checkDate() {
  selectedDate = document.getElementById("endDate").value;
  var yyyy = selectedDate.slice(0, 4);
  var mm = selectedDate.slice(5, 7);
  var dd = selectedDate.slice(8);
  console.log(yyyy, mm - "1", dd);
  selectedDateInComparableFormat = new Date(yyyy, mm - "1", dd);
  var error = document.getElementById("errorDate");
  if (selectedDateInComparableFormat > new Date()) {
    error.innerHTML = "Please select date lesser than today's date";
    error.style.color = "red";
  } else {
    error.innerHTML = "";
  }
}
