from main.connector import Connector
from main.parameter import Input, Output
from url import OpenWeatherMap

class Weather(Connector):

    latitude = Input(iotype='float', required=True, min=-90., max=90.)
    longitude = Input(iotype='float', required=True, min=-180., max=180.)
    elevation = Output(iotype='float')

    def __init__(self):
        super(Weather, self).__init__()
        self.set_throttle()
        self.set_url(OpenWeatherMap)
        self.set_parser('json')

    def parse_results(self, results):
        for row in results['weather']:
            result = {'description': row['description']}
            self.results.add(result)

if __name__ == '__main__':

    test = Weather()
    test.fetch({'latitude':39., 'longitude':-104.})
    test.fetch({'latitude':39., 'longitude':-110.})

    for i in test.results.get_iter():
        print i
    