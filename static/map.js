/*javascript needed for google maps rendering */

/*var latlng= new google.maps.LatLng(document.getElementById("user_loc").innerHTML);*/

var latlng = new google.maps.LatLng(lat,lng);

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
