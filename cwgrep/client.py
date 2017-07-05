import boto3

from cwgrep import config


class Client(object):

    def __init__(self, profile_name=None):
        self.cfg = config.Config()
        self.session = self._session(profile_name)

    def _session(self, profile_name=None):
        cfg_profile = self.cfg.get('profile_name')

        if profile_name:
            session = boto3.Session(profile_name=profile_name)
        elif cfg_profile:
            session = boto3.Session(profile_name=cfg_profile)
        else:
            # try the default profile
            session = boto3.Session()

        # test connectivity
        sts = session.client('sts')
        sts.get_caller_identity()

        return session

    def filter_logs(self):
        print "filter shit"
