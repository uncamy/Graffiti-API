/*javascript needed for google maps rendering */

function initialize(){
    var mapOptions = {
          center: new google.maps.LatLng(40.801406, -73.95906099),
          zoom: 8
    };
    var map = new google.maps.Map(document.getElementById("map-canvas"),
            mapOptions);
    }
    google.maps.event.addDomListener(window, 'load', initialize);
}
