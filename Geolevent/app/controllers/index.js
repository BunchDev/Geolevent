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

function addsomething(){
/*	var textValue = $.text.getValue();
    var hobbyData = [
    {properties: { title:textValue}},
            ];

    var item = $.section.appendItems(hobbyData);
    $.list.setSections(item);

    $.text.blur();  */
}

$.index.open();
