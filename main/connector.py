import json
import requests
from string import Template
import xml.etree.ElementTree as ET
import time

from results import ResultSet, ResultRow
from parameter import Input

output_parsers = {'json': json.loads, 'xml': ET.parse}

class Connector(object):

    def __init__(self):
        self.results = ResultSet() #list of dictionaries containing results

    def set_auth_type(self, auth_type):
        """Set the authorization type for given web service
        
        Allowed types:
        
        anon: web service only provides anonymous access
        login: user must be logged in to use the web service
        mixed: web service allows both anonymous and user-based access
        """
        pass

    def set_throttle(self, limit=None, units=None):
        """Set the request rate for the given service

        units: {'requests per second', 'requests per day', etc.}
        """
        self.delay = 0
        self.max_requests = 1e16
        self.made_requests = 0

    def throttle(f):
        """wrapper function for throttling web service requests"""
        def wrapper(self, *args, **kwargs):
            if self.made_requests < self.max_requests:
                time.sleep(self.delay)
                f(self, *args, **kwargs)
                self.made_requests += 1
            else:
                raise Exception, 'maximum request limit reached'
        return wrapper

    def set_url(self, url_str):
        self.url = Template(url_str)

    def set_parser(self, output_format):
        """sets the object variable to the correct output stream parser"""
        self.output_parser = output_parsers.get(output_format, lambda x:x)

    def get_url_params(self):
        p = {}
        for attr_name, attr_value in self.__class__.__dict__.items():
            if isinstance(attr_value, Input):
                p[attr_name] = getattr(attr_value, 'value')
        return p

    @throttle
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
        self.results.clear_results()