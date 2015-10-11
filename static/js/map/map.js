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
	}).setView([-0.454085, 36.950451], 10);
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
function getColor(d) {
        return d === 'plantation'  ? "LawnGreen" :
               d === 'agriculture (dense)'  ? "ForestGreen" :
               d === 'agriculture (sparse)' ? "Green" :
               d === 'woodland' ? "DarkOliveGreen " :
               d === 'town' ? "Peru" :
               d === 'barren land (R)' ? "IndianRed " :
               d === 'forest' ? "DarkGreen" :
                            "green";
    }

    function style(feature) {
        return {
            weight: 1.5,
            opacity: 1,
            fillOpacity: 1,
            radius: 6,
            fillColor: getColor(feature.properties.zone_type),
            color: "grey"

        };
    }
function doStylenewparcels(feature) {
			switch (feature.properties.blockcode) {
				case 27:
					return {
						weight: '1.3',
						fillColor: '#ca0020',
						color: '#000000',
						weight: '1',
						dashArray: '',
						opacity: '1.0',
						fillOpacity: '1.0',
					};
					break;
				case 466:
					return {
						weight: '1.3',
						fillColor: '#eb846e',
						color: '#000000',
						weight: '1',
						dashArray: '',
						opacity: '1.0',
						fillOpacity: '1.0',
					};
					break;
				case 491:
					return {
						weight: '1.3',
						fillColor: '#f5d6c8',
						color: '#000000',
						weight: '1',
						dashArray: '',
						opacity: '1.0',
						fillOpacity: '1.0',
					};
					break;
				case 493:
					return {
						weight: '1.3',
						fillColor: '#cee3ed',
						color: '#000000',
						weight: '1',
						dashArray: '',
						opacity: '1.0',
						fillOpacity: '1.0',
					};
					break;
				case 495:
					return {
						weight: '1.3',
						fillColor: '#75b4d4',
						color: '#000000',
						weight: '1',
						dashArray: '',
						opacity: '1.0',
						fillOpacity: '1.0',
					};
					break;
			}
		}
function getstyle(feature) {
	switch (feature.properties.zone_type){
		case 'plantation':
			return {
				weight: 2,
				opacity: 1,
				color: 'orange',
				dashArray: '3',
				fillOpacity: 0.7
			};
			break;
		case 'agriculture (dense)':
			return {
				weight: 2,
				opacity: 1,
				color: 'purple',
				dashArray: '3',
				fillOpacity: 0.7
			};
			break;
		case 'agriculture (sparse)':
			return {
				weight: 2,
				opacity: 1,
				color: 'brown',
				dashArray: '3',
				fillOpacity: 0.7
			};
			break;
		case 'forest':
			return {
				weight: 2,
				opacity: 1,
				color: 'green',
				dashArray: '3',
				fillOpacity: 0.7
			};
			break;
		case 'woodland':
			return {
				weight: 2,
				opacity: 1,
				color: 'yellow',
				dashArray: '3',
				fillOpacity: 0.7
			};
			break;
		case 'barren land (R)':
			return {
				weight: 2,
				opacity: 1,
				color: 'yellow',
				dashArray: '3',
				fillOpacity: 0.7
			};
			break;
		case 'town':
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
    parcel.addData(data).setStyle(doStylenewparcels);
    //parcel.bindLabel(feature.properties['registration_section'], { 'noHide': true });
    parcel.eachLayer(function (layer) {    	
    layer.bindLabel(layer.feature.properties['sectcode']);
	
	layer.on('click', function (e) {
		var popup = "<strong>" + "Id : " + e.target.feature.properties.id + "<br>" + "Area Code : " + e.target.feature.properties.areacode + "<br>" + "Section Code : " + e.target.feature.properties.sectcode + "<br>" + "Parcel No : " + e.target.feature.properties.parcel_no +  "</strong>";
		layer.bindPopup(popup).openPopup(e.latlng);
		if (!L.Browser.ie && !L.Browser.opera) {
				layer.bringToFront();
		}

	});
	layer.on('mouseover',function(e){
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
    landuse.addData(data).setStyle(style);
    landuse.eachLayer(function (layer) { 
    layer.on('click', function (e) {
		var popup = "<strong>" + "Id : " + e.target.feature.properties.id + "<br>" + "Landuse : " + e.target.feature.properties.zone_type + "<br>" + "Zone Code : " + e.target.feature.properties.zone_code +  "</strong>";
		layer.bindPopup(popup).openPopup(e.latlng);

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

	});	
	});	
    //parcel.bindLabel(feature.properties['registration_section'], { 'noHide': true });
});
$.getJSON(riperianurl, function (data) {
    riperian.addData(data).setStyle(riperianStyle);
    //parcel.bindLabel(feature.properties['registration_section'], { 'noHide': true });
});
map.addLayer(landuse);
//map.addLayer(landcover);
//map.addLayer(roads);

var legend = L.control({position: 'bottomright'});
    legend.onAdd = function (map) {

    var div = L.DomUtil.create('div', 'info legend');
    labels = ['<strong>Categories</strong>'],
    categories = ['plantation','agriculture (dense)','agriculture (sparse)','woodland','town','barren land (R)','forest'];

    for (var i = 0; i < categories.length; i++) {

            div.innerHTML += 
            labels.push(
                '<i class="rectangle" style="background:' + getColor(categories[i]) + '"></i> ' +
            (categories[i] ? categories[i] : '+'));

        }
        div.innerHTML = labels.join('<br>');
    return div;
    };
    legend.addTo(map);

var baseLayers = {
	"OSM Mapnik": osmMap,
	"Landscape": landMap
};
var overlays = {
	"Land Parcels": parcel,
	"Rivers":rivers,
	"Riparian Reserve":riperian,
	"Landuse Zoning":landuse,
	"LandCover 2015":landcover
};


L.control.layers(baseLayers,overlays,{collapsed:true}).addTo(map);
info.addTo(map);
L.control.scale({position:"bottomleft"}).addTo(map);

// Add fuse search control
var options = {
        position: 'topright',
        title: 'Parcel Search',
        placeholder: 'Enter parcel No',
        maxResultLength: 15,
        threshold: 0.0,
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
        var props = ['parcel_no'];
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

