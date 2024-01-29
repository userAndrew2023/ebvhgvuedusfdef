import sys
from geocoder import *
from static_map import show_map

toponym_to_find = " ".join(sys.argv[1:])
delta = get_span(toponym_to_find)

code = get_geocode(address=toponym_to_find)
show_map(code, delta=delta)
