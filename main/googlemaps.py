import json
from string import Template

from parameter import URLParameter, OutputParameter
from url import GoogleElevation
from connector import Connector

class Elevation(Connector):

    latitude = URLParameter(iotype='float', required=True, min=-90., max=90.)
    longitude = URLParameter(iotype='float', required=True, min=-180., max=180.)
    elevation = OutputParameter(iotype='float')

    def __init__(self):
        super(Elevation, self).__init__()
        self.url = Template(GoogleElevation)
        self.set_parser('json')

    def parse_results(self, results):
        for row in results['results']:
            result_row = {'elevation': row['elevation']}
            self.results.append(result_row)

if __name__ == '__main__':

    test = Elevation()
    test.fetch({'latitude':39., 'longitude':-104.})
    test.fetch({'latitude':39., 'longitude':-110.})

    for i in test.results:
        print i
    