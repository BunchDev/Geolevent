function doClick(e) {
    alert($.label.text);
}

Titanium.Geolocation.getCurrentPosition(function(e)
{
    if (e.error)
    {
        alert('Error en la captura de tu ubicacion actual');
        return;
    }

  
var region = {
    latitude : e.coords.latitude,
    latitudeDelta : "0.01",
    longitude : e.coords.longitude,
    longitudeDelta : "0.01"
};

   $.mapview.setRegion(region);

});

$.index.open();
