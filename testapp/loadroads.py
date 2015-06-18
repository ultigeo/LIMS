import os
from django.contrib.gis.utils import LayerMapping
from models import Roads

# Auto-generated `LayerMapping` dictionary for nyeri_county model
nyeri_county_mapping = {
    'id':'Id',
    'name':'NAME',
    'geom':'POLYGON',
    'road_type':'TYPE',
    'road_class':'CLASS'
}

nyericounty_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../testapp/data/ROADS.shp'))

def run(verbose=True):
    lm = LayerMapping(Roads, nyericounty_shp, nyeri_county_mapping,
                      transform=True)
    lm.save(strict=True, verbose=verbose)
