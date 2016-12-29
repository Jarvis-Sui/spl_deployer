import urllib2
import urllib
import base64
import json
import ssl
from xml.etree.ElementTree import XML
import logging
import config
from os.path import join, dirname

logging.basicConfig(filename=join(dirname(__file__), 'request.log'), format='%(asctime)s %(filename)s %(levelname)s %(message)s', level=logging.DEBUG)

class MyRequest(object):
    def __init__(self, authority, username, password):
        self.authority = authority
        self.username = username
        self.password = password
        self.token = self._auth_token()

    def request(self, path_segment, data = None, method='GET'):
        body = None
        if data:
            body = urllib.urlencode(data)

        logging.debug('rest %s %s. data: %s' % (method, (self.authority + path_segment), data))
        req = urllib2.Request(self.authority + path_segment + '?count=-1', body)
        req.add_header("Authorization", self.token)
        req.get_method = lambda: method # set 'DELETE' request. Using HttpLib to make 'DELETE' request is more common
        ctx = ssl._create_unverified_context()
        return urllib2.urlopen(req, context=ctx)

    def _auth_token(self):
        token = "Splunk %s" % self._get_session_key()
        return token

    def _get_session_key(self):
        values = {'username':self.username,
                'password':self.password}
        data = urllib.urlencode(values)
        logging.debug('rest POST %s/services/auth/login' % self.authority)
        request = urllib2.Request(self.authority + '/services/auth/login', data=data)

        auth = base64.b64encode("%s:%s" % (self.username, self.password))
        request.add_header("Authorization","Basic %s" % auth)

        ctx = ssl._create_unverified_context()
        try:
            response = urllib2.urlopen(request, context=ctx)
            session = XML(response.read()).findtext("sessionKey")
            return session
        except Exception as err:
            logging.error(err)
            print "connection faild: %s. Please check the url and your username:password.\
                    Do not use default password 'changeme'" % str(err)
            exit()

auth = config.Config().get_auth()
my_request = MyRequest(auth['authority'], auth['username'], auth['password'])

if __name__ == '__main__':
    print my_request.request('/servicesNS/nobody/Splunk_TA_aws/splunk_ta_aws/inputs/config').read()
    pass
