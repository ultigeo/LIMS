import os
from django.contrib.gis.utils import LayerMapping
from models import landcover

# Auto-generated `LayerMapping` dictionary for nyeri_county model
nyeri_county_mapping = {
    'gid' : 'OBJECTID',
    'geom' : 'MULTIPOLYGON',
    'area' :'area',
    'landcover_code' : 'GRIDCODE',
    'landcover_type' : 'CLASS_NAME',

   
}

nyericounty_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../testapp/data/landcover2015.shp'))

def run(verbose=True):
    lm = LayerMapping(landcover, nyericounty_shp, nyeri_county_mapping,
                      transform=False)
    lm.save(strict=False, verbose=verbose)
