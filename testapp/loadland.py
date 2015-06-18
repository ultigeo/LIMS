import os
from django.contrib.gis.utils import LayerMapping
from testapp.models import landuse_zoning

# Auto-generated `LayerMapping` dictionary for nyeri_county model
nyeri_landuse = {
    'id' : 'id',
    'area' :'AreaKm2',
    'length':'length',
   'zone_type' : 'LANDUSE',
   'zone_code' : 'LUNUM',
   'geom' : 'Polygon',
}

nyericounty_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../testapp/data/landuse.shp'))

def run(verbose=True):
    lm = LayerMapping(landuse_zoning, nyericounty_shp, nyeri_landuse,
                      transform=True, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
