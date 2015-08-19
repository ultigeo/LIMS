import os
from django.contrib.gis.utils import LayerMapping
from models import Riperian

# Auto-generated `LayerMapping` dictionary for nyeri_county model
nyeri_county_mapping = {
    'id':'Id',
    'name':'NAME',
    'geom':'MultiPolygon',
    'reserve':'STREAM_ORD',
}

nyericounty_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../testapp/data/RIVERS.shp'))

def run(verbose=True):
    lm = LayerMapping(Riperian, nyericounty_shp, nyeri_county_mapping,
                      transform=True)
    lm.save(strict=True, verbose=verbose)
