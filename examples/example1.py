import sys
sys.path.append('..')

from services.googlemaps import Elevation

example1 = Elevation()
example1.fetch({'latitude':39., 'longitude':-104.})
example1.fetch({'latitude':39., 'longitude':-110.})

for i in example1.results.get_iter():
    print i
