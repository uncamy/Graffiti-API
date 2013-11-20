/*javascript needed for google maps rendering */

/*var latlng= new google.maps.LatLng(document.getElementById("user_loc")); */
var latlng = new google.maps.LatLng('40.72078, -74.001119');

function initialize(){
    var mapOptions = {
          center: latlng,
          zoom: 15
    }

    var map = new google.maps.Map(document.getElementById("map-canvas"),
            mapOptions);

    /*adds a marker to the map for the user's location*/
    var marker = new google.maps.Marker({
        position: latlng,
        map: map,
        title: "user location"
    });


}
google.maps.event.addDomListener(window, 'load', initialize);
