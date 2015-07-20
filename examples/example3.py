import sys
sys.path.append('..')

from services.geonames import Place, Neighbourhood

place = Place()
place.fetch({'latitude':39., 'longitude':-104.})
place.fetch({'latitude':39., 'longitude':-110.})

for i in place.results.get_iter():
    print i
    
neighbourhood = Neighbourhood()
neighbourhood.fetch({'latitude':40.78343, 'longitude':-73.96625})

for i in neighbourhood.results.get_iter():
    print i
    
