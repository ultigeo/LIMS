var osmLink = '<a href="http://openstreetmap.org">OpenStreetMap</a>',
	thunLink = '<a href="http://thunderforest.com/">Thunderforest</a>';

var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
	osmAttrib = '&copy; ' + osmLink + ' Contributors',
	landUrl = 'http://{s}.tile.thunderforest.com/landscape/{z}/{x}/{y}.png',
	thunAttrib = '&copy; '+osmLink+' Contributors & '+thunLink;

var mapUrl = 'http://otile4.mqcdn.com/tiles/1.0.0/sat/{z}/{x}/{y}.png',
	mapAttrib = '&copy; ' + osmLink + ' Contributors';

var osmMap = L.tileLayer(osmUrl, {attribution: osmAttrib}),
	landMap = L.tileLayer(landUrl, {attribution: thunAttrib});

var aerial= L.tileLayer(mapUrl, {attribution: mapAttrib});

var parcel = L.geoJson();
var rivers = L.geoJson();
var landuse = L.geoJson();
var riperian= L.geoJson();
var landcover= L.geoJson();

var map = L.map('map',{
	layers: [osmMap],
	keyboard: true,
	boxZoom: true,
	zoomControl: false,
	//measureControl: true,
	doubleClickZoom: true,
	scrollWheelZoom: true,
	fullscreenControl: true,
	fullscreenControlOptions: {
		position: 'topleft'
	} 
	}).setView([-0.418715, 36.950451], 12);
	mapLink ='<a href="http://openstreetmap.org">OpenStreetMap</a>';
	L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
				attribution: 'Map data &copy; ' + mapLink,
			    maxZoom:32,
			    }).addTo(map);
				
var sidebar = L.control.sidebar('sidebar', {
    closeButton: true,
    position: 'left'
});
map.addControl(sidebar);
// add the new control to the map
var zoomHome = new L.Control.zoomHome();
zoomHome.addTo(map);

function parcelStyle(feature) {
	return {
		weight: 2,
		//opacity: 1,
		color: 'brown',
		dashArray: '3',
		fillOpacity: 0.3,
		fillColor: 'brown'
	};
}
function outStyle(feature) {
	return {
		weight: 2,
		opacity: 1,
		color: 'brown',
		dashArray: '3',
		fillOpacity: 0.3,
		fillColor: 'brown'
	};
}
function riverStyle(feature) {
	return {
		weight: 2,
		opacity: 1,
		color: 'blue',
		dashArray: '3',
		//fillOpacity: 0.7,
		//fillColor: 'brown'
	};
}
function riperianStyle(feature) {
	return {
		weight: 2,
		opacity: 1,
		color: 'orange',
		dashArray: '3',
		fillOpacity: 0.7,
		fillColor: 'yellow'
	};
}
function getstyle(feature) {
	switch (feature.properties.zone_type){
		case 'Agricultural':
			return {
				weight: 2,
				opacity: 1,
				color: 'orange',
				dashArray: '3',
				fillOpacity: 0.7
			};
			break;
		case 'Residential':
			return {
				weight: 2,
				opacity: 1,
				color: 'purple',
				dashArray: '3',
				fillOpacity: 0.7
			};
			break;
		case 'Commercial':
			return {
				weight: 2,
				opacity: 1,
				color: 'brown',
				dashArray: '3',
				fillOpacity: 0.7
			};
			break;
		case 'Reserve':
			return {
				weight: 2,
				opacity: 1,
				color: 'green',
				dashArray: '3',
				fillOpacity: 0.7
			};
			break;
		case 'Public':
			return {
				weight: 2,
				opacity: 1,
				color: 'yellow',
				dashArray: '3',
				fillOpacity: 0.7
			};
			break;

	}

}
function coverstyle(feature) {
	switch (feature.properties.landcover_type){
		case 'Agriculture':
			return {
				weight: 2,
				opacity: 1,
				color: 'brown',
				dashArray: '3',
				fillOpacity: 0.7
			};
			break;
		case 'Built Up':
			return {
				weight: 2,
				opacity: 1,
				color: 'purple',
				dashArray: '3',
				fillOpacity: 0.7
			};
			break;
		case 'Bushland':
			return {
				weight: 2,
				opacity: 1,
				color: 'pink',
				dashArray: '3',
				fillOpacity: 0.7
			};
			break;
		case 'Forest':
			return {
				weight: 2,
				opacity: 1,
				color: 'green',
				dashArray: '3',
				fillOpacity: 0.7
			};
			break;
		case 'Grassland':
			return {
				weight: 2,
				opacity: 1,
				color: 'yellow',
				dashArray: '3',
				fillOpacity: 0.7
			};
			break;
		case 'Clouds':
			return {
				weight: 2,
				opacity: 1,
				color: 'white',
				dashArray: '3',
				fillOpacity: 0.7
			};
			break;
		case 'Transition':
			return {
				weight: 2,
				opacity: 1,
				color: 'grey',
				dashArray: '3',
				fillOpacity: 0.7
			};
			break;
		case 'Water':
			return {
				weight: 2,
				opacity: 1,
				color: 'blue',
				dashArray: '3',
				fillOpacity: 0.7
			};
			break;
		case 'Unclassified':
			return {
				weight: 2,
				opacity: 1,
				color: 'black',
				dashArray: '3',
				fillOpacity: 0.7
			};
			break;

	}

}
function style(feature) {
	return {
		weight: 2,
		opacity: 1,
		color: 'white',
		dashArray: '3',
		fillOpacity: 0.7,
		fillColor: getColor(feature.properties.zone_type)
	};
}

var measureControl = L.control.measure({
	position: 'topleft',
	completedColor: '#C8F2BE'
});
measureControl.addTo(map);
// control that shows state info on hover
var info = L.control();
info.onAdd = function (map) {
	this._div = L.DomUtil.create('div', 'info');
	this.update();
	return this._div;
};

info.update = function (props) {
	this._div.innerHTML = '<h4>Parcel Information</h4>' +  (props ?
		'<b>'+ "Id : " + props.id + '</b><br/>' + "Parcel No : "+ props.parcel_no + '</b><br/>'
		: 'Select a Parcel');
};
//var roads = L.geoJson();												
var dataurl = '/ladm/data/';
var riverurl = '/ladm/rivers/';
var landuseurl = '/ladm/landuse/';
var riperianurl ='/ladm/riperian/';
var landcoverurl='/ladm/landcover/';

$.getJSON(dataurl, function (data) {
    parcel.addData(data).setStyle(parcelStyle);
    //parcel.bindLabel(feature.properties['registration_section'], { 'noHide': true });
    parcel.eachLayer(function (layer) {    	
    layer.bindLabel(layer.feature.properties['sectcode']);
	
	layer.on('click', function (e) {
		var popup = "<strong>" + "Id : " + e.target.feature.properties.id + "<br>" + "Area Code : " + e.target.feature.properties.areacode + "<br>" + "Section Code : " + e.target.feature.properties.sectcode + "<br>" + "Parcel No : " + e.target.feature.properties.parcel_no +  "</strong>";
		layer.bindPopup(popup).openPopup(e.latlng);
		map.fitBounds(e.target.getBounds());
		if (!L.Browser.ie && !L.Browser.opera) {
				layer.bringToFront();
		}

	});
	layer.on('mouseover',function(e){
		var layer = e.target;

			layer.setStyle({
				weight: 5,
				color: '#666',
				dashArray: '',
				fillOpacity: 0.7
			});

			if (!L.Browser.ie && !L.Browser.opera) {
				layer.bringToFront();
			}

			info.update(layer.feature.properties);
  	
	});			    
	
	layer.on('mouseout',function(e){
		parcel.setStyle(outStyle);    	
	});
			    
	});
});
$.getJSON(riverurl, function (data) {
    rivers.addData(data).setStyle(riverStyle);
    rivers.eachLayer(function (layer) {    	
    layer.on('click', function (e) {
		var popup = "<strong>" + "Id : " + e.target.feature.properties.id + "<br>" + "Name : " + e.target.feature.properties.name + "<br>" + "Reserve : " + e.target.feature.properties.reserve +  "</strong>";
		layer.bindPopup(popup).openPopup(e.latlng);

	});			    
	});
    //parcel.bindLabel(feature.properties['registration_section'], { 'noHide': true });
});
$.getJSON(landuseurl, function (data) {
    landuse.addData(data).setStyle(getstyle);
    landuse.eachLayer(function (layer) { 
    layer.on('click', function (e) {
		var popup = "<strong>" + "Id : " + e.target.feature.properties.id + "<br>" + "Landuse : " + e.target.feature.properties.zone_type + "<br>" + "Zone Code : " + e.target.feature.properties.zone_code +  "</strong>";
		layer.bindPopup(popup).openPopup(e.latlng);
		map.fitBounds(e.target.getBounds());

	});	
	});	
    //parcel.bindLabel(feature.properties['registration_section'], { 'noHide': true });
});
$.getJSON(landcoverurl, function (data) {
    landcover.addData(data).setStyle(coverstyle);
    landcover.eachLayer(function (layer) { 
    layer.on('click', function (e) {
		var popup = "<strong>" + "Id : " + e.target.feature.properties.id + "<br>" + "Landcover Type: " + e.target.feature.properties.landcover_type + "<br>" + "Landcover Code : " + e.target.feature.properties.landcover_code +  "</strong>";
		layer.bindPopup(popup).openPopup(e.latlng);
		map.fitBounds(e.target.getBounds());

	});	
	});	
    //parcel.bindLabel(feature.properties['registration_section'], { 'noHide': true });
});
$.getJSON(riperianurl, function (data) {
    riperian.addData(data).setStyle(riperianStyle);
    //parcel.bindLabel(feature.properties['registration_section'], { 'noHide': true });
});
map.addLayer(parcel);
//map.addLayer(landcover);
//map.addLayer(roads);
var legend = L.control({position:'bottomright'});
legend.onAdd = function (map) {
	var div = L.DomUtil.create('div','info legend');
	div.innerHTML = "<h3>Legend</h3><table></table>";
	return div;
}
legend.addTo(map);

var baseLayers = {
	"OSM Mapnik": osmMap,
	"Landscape": landMap,
	"Aerial":aerial
};
var overlays = {
	"Land Parcels": parcel,
	"Rivers":rivers,
	"Riperian Reserve":riperian,
	"Landuse Zoning":landuse,
	"Land Cover":landcover
};


L.control.layers(baseLayers,overlays,{collapsed:false}).addTo(map);
info.addTo(map);
L.control.scale({position:"bottomleft"}).addTo(map);

// Add fuse search control
var options = {
        position: 'topright',
        title: 'Parcel Search',
        placeholder: 'Parcen No,Block, Sect Code',
        maxResultLength: 15,
        threshold: 0.5,
        showInvisibleFeatures: true,
        showResultFct: function(feature, container) {
            props = feature.properties;
            var name = L.DomUtil.create('b', null, container);
            name.innerHTML = props.parcel_no;
            container.appendChild(L.DomUtil.create('br', null, container));
            var info = '' +  props.id + ', ' + props.blockid;
        	container.appendChild(document.createTextNode(info));

            
        }
    };
    var fuseSearchCtrl = L.control.fuseSearch(options);
    map.addControl(fuseSearchCtrl);

    // Load the data
    jQuery.getJSON(dataurl, function(data) {
        displayFeatures(data.features, parcel);
        var props = ['parcel_no','blockid', 'sectcode'];
        fuseSearchCtrl.indexFeatures(data.features, props);
        //map.fitBounds(e.target.getBounds()); 
        //parcel.feature = parcel;   
   });  
     
function displayFeatures(features, parcel) {

    var popup = L.DomUtil.create('div', 'tiny-popup', map.getContainer());
                    
    for (var id in features) {
        var feat = features[id];  
        var cat = feat.properties.parcel_no;      
        var site = L.geoJson(feat, {
            onEachFeature: bindPopup
        }); 
        var layer = parcel[feat];
        if (layer !== undefined) {
            layer.addLayer(site);
        }    
    }
    return parcel;
}
 
function bindPopup(feature, layer) {
    // Keep track of the layer(marker)
    feature.parcel = layer;
    
    var props = feature.properties;
    if (props) {
        var desc = '<span id="feature-popup">';
        desc += '<strong>' + props.parcel_no + '</strong><br/>';        
                 
        var details = '' + props.id + ' ' + props.sectcode + ' ' + props.blockid;
        desc += details + '<br/>';
        desc += '</span>';
        layer.bindPopup(desc);
        //map.fitBounds(layer.getBounds());
    }
}

