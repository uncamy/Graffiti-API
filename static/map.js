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
        title: "user location",
        map: map
    });

    /*add marker for graffiti locations */
    var image = {
        url:'http://www.alispagnola.com/Free/spraypaint2.jpg',
        scaledSize: new google.maps.Size(32, 32),
        origin: new google.maps.Point(0,0)
    };

    var location = new google.maps.LatLng(40.7236264, -73.9980549);
    var graffiti_marker = new google.maps.Marker({
        icon: image,
        position: location,
        title: "graffiti",
        map: map
    });


}
google.maps.event.addDomListener(window, 'load', initialize);
