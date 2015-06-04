import json
import xml.etree.ElementTree as ET
import requests

from parameter import URLParameter

output_parsers = {'json': json.loads, 'xml': ET.parse}

class Connector(object):

    def __init__(self):
        self.results = [] #list of dictionaries containing results
        self.url = None

    def set_parser(self, output_format):
        self.output_parser = output_parsers.get(output_format, lambda x:x)        

    def get_url_params(self):
        p = {}
        for attr_name, attr_value in self.__class__.__dict__.items():
            if type(attr_value) == URLParameter:
                p[attr_name] = getattr(attr_value, 'value')
        return p

    def fetch(self, config):
        for key, val in config.iteritems():
            setattr(getattr(self, key), 'value', val)

        url = self.url.substitute(self.get_url_params())
        r = requests.get(url)

        results = self.output_parser(r.text)
        self.parse_results(results)

    def fetchmany(self, config_list):
        for config in config_list:
            self.fetch(config)

    def parse_results(self):
        raise NotImplementedError

    def reset(self):
        self.results = []