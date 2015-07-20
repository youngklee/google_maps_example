import sys
sys.path.append('..')

from services.openweathermap import Weather

example2 = Weather()
example2.fetch({'latitude':39., 'longitude':-104.})
example2.fetch({'latitude':39., 'longitude':-110.})

for i in example2.results.get_iter():
    print i