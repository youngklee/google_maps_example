from main.connector import Connector
from main.parameter import Input, Output

# maybe import url so that url.GeoNames instead of GeoNames
from url import GeoNamesFindNearby, GeoNamesNeighbourhood

class Place(Connector):

    latitude = Input(iotype='float', required=True, min=-90., max=90.)
    longitude = Input(iotype='float', required=True, min=-180., max=180.)
    # elevation = Output(iotype='float')

    def __init__(self):
        super(Place, self).__init__()
        self.set_throttle()
        self.set_url(GeoNamesFindNearby)
        self.set_parser('json')

    def parse_results(self, results):
        for row in results['geonames']:
            result = {'name': row['name']}
            self.results.add(result)
            
class Neighbourhood(Connector):

    latitude = Input(iotype='float', required=True, min=-90., max=90.)
    longitude = Input(iotype='float', required=True, min=-180., max=180.)
    # elevation = Output(iotype='float')

    def __init__(self):
        super(Neighbourhood, self).__init__()
        self.set_throttle()
        self.set_url(GeoNamesNeighbourhood)
        self.set_parser('json')

    def parse_results(self, results):
        # print results['neighbourhood'].keys()
        # for row in results['neighbourhood']:
            
        result = {'name': results['neighbourhood']['name']}
        self.results.add(result)
    

if __name__ == '__main__':

    test = Weather()
    test.fetch({'latitude':39., 'longitude':-104.})
    test.fetch({'latitude':39., 'longitude':-110.})

    for i in test.results.get_iter():
        print i