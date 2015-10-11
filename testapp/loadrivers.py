import os
from django.contrib.gis.utils import LayerMapping
from models import Rivers

# Auto-generated `LayerMapping` dictionary for nyeri_county model
nyeri_county_mapping = {
    'id' : 'Id',
    'name' : 'NAME',
    'river_type' : 'TYPE',
    'geom' : 'MULTILINESTRING',
}

nyericounty_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../testapp/data/RIVERS.shp'))

def run(verbose=True):
    lm = LayerMapping(Rivers, nyericounty_shp, nyeri_county_mapping,
                      transform=True)
    lm.save(strict=True, verbose=verbose)
