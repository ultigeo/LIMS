import os
from django.contrib.gis.utils import LayerMapping
from models import las_parcel

# Auto-generated `LayerMapping` dictionary for nyeri_county model
nyeri_county_mapping = {
    'id' : 'Id',
    'parcel_no':'parcel_no',
    'blockid':'blockcode',
    'sectcode':'sectcode',
    'geom' : 'MultiPolygon',
    'areacode' :'areacode',
  
}

nyericounty_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../testapp/data/newparcels.shp'))

def run(verbose=True):
    lm = LayerMapping(las_parcel, nyericounty_shp, nyeri_county_mapping,
                      transform=True)
    lm.save(strict=True, verbose=verbose)
