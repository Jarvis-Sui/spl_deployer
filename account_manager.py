from rest_util import my_request
from xml.etree.ElementTree import XML
import logging

endpoint = '/servicesNS/nobody/Splunk_TA_aws/splunk_ta_aws/settings/account4ui'

def get_account_names():
    names = []
    response = my_request.request(endpoint)
    root = XML(response.read())
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        names.append(entry.find('{http://www.w3.org/2005/Atom}title').text)

    return names

def create_account(account_name, key_id, secret_key, category):
    # category: 
    # 1: Global
    # 2: Gov
    # 3: China
    data = {}
    data['name'] = account_name
    data['key_id'] = key_id
    data['secret_key'] = secret_key
    data['category'] = category
    my_request.request(endpoint, data, 'POST')
    logging.debug("account %s created" % account_name)

def create_accounts(accounts):
    for account in accounts:
        create_account(account['name'], account['key_id'],
                account['secret_key'], account['category'])
    return len(accounts)

def delete_account(account_name):
    response = my_request.request(endpoint + "/" + account_name, method='DELETE')
    logging.debug('account %s deleted' % account_name)
    return response

def delete_all_accounts():
    names = get_account_names()
    for name in names:
        delete_account(name)

if __name__ == '__main__':
    delete_all_accounts()
