import ConfigParser
import os

SECTION = 'DEFAULT'


class Config(object):

    def __init__(self, profile_name=None):
        self.cfg = ConfigParser.ConfigParser()
        path = os.path.expanduser('~/.cwgreprc')
        self.cfg.read([path])

    def get(self, key, required=False):
        if self.cfg.has_option(SECTION, key):
            return self.cfg.get(SECTION, key)
        elif required:
            raise Exception("Option '%s' is missing from config" % key)



