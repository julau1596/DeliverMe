var currentLat = 37.7749;
var currentLng = -122.4194;
var geoLat;
var geoLng; 
var location; 
var directionsService;
var directionsDisplay
function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(browserHasGeolocation ?
                        'Error: The Geolocation service failed.' :
                        'Error: Your browser doesn\'t support geolocation.');
  infoWindow.open(map);
}

//map and markers
function initMap(){
  //default location

  directionsService = new google.maps.DirectionsService;
    //returns an efficient path
  directionsDisplay = new google.maps.DirectionsRenderer;
  var defaultLocation = {
    zoom: 11,
    center: {lat: 37.7749, lng: -122.4194}
  }

  //map
  var map = new google.maps.Map(document.getElementById('map'), defaultLocation);

  var infoWindow =  new google.maps.InfoWindow;
   directionsDisplay.setMap(map);
  //gets current location coordinates
  if (navigator.geolocation) {

    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };

      currentLat = position.coords.latitude;
      currentLng = position.coords.longitude;

      infoWindow.setPosition(pos);
    
      infoWindow.open(map);
      map.setCenter(pos);

    }, function() {
      handleLocationError(true, infoWindow, map.getCenter());
    });

  } else {
    // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
  }
 

}
function getData(event) {
  //location = event.children[0].innerHTML;
  geocode(directionsService, directionsDisplay,event);
  //console.log(event.closest('H5.dest-item'));
}
 function calculateAndDisplayRoute(directionsService, directionsDisplay) {
    console.log("LAT: " + geoLat);
 
    directionsService.route({
      origin: {lat: currentLat, lng: currentLng},
      destination: {lat: geoLat, lng: geoLng},
      travelMode: 'DRIVING'
    }, function(response, status) {
      if (status === 'OK') {
        directionsDisplay.setDirections(response);
      } else {
        window.alert('Directions request failed due to ' + status);
      }
    });
  }
function geocode(directionsService, directionsDisplay, event){
  //e.preventDefault();
  //var location = document.getElementById('location-input').value;

  var location =  event.children[3].innerHTML;
 
  axios.get('https://maps.googleapis.com/maps/api/geocode/json', {
    params:{
      address:location,
      key:'AIzaSyB6vz8qr0YzLIR4jDNh3gLiVQsLEcHdMQA'
    }
  })
  .then(function(response){
    console.log(response);

    
    //format address
    var formAddress = response.data.results[0].formatted_address;
    var formAddressOutput = `
      <ul class="list-group">
        <li class="list-group-item">${formAddress}</li>
      </ul>
    `;
    
    //geometry determining lat long by search
    geoLat = response.data.results[0].geometry.location.lat;
    geoLng = response.data.results[0].geometry.location.lng;
    console.log("IM HERE");
    calculateAndDisplayRoute(directionsService, directionsDisplay);

  })


}