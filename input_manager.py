import input_settings as IS
from rest_util import my_request
from xml.etree.ElementTree import XML
from account_manager import get_account_names
from index_manager import get_indexes
from datetime import datetime

import logging

def create_inputs(inputs):
    count = 0
    for kind, one_inputs in inputs.iteritems():
        for name, data in one_inputs.iteritems():
            if validate_input(name, data):
                new_name = build_name(name, kind, data)
                try:
                    create_input(new_name, kind, data)
                    count += 1
                except Exception as err:
                    logging.error("Failed to create input '%s' of kind '%s'. %s" %(name, kind, str(err)))
                    print "Failed to create input '%s' of kind '%s'. For more info, see log file." %(name, kind)
            else:
                logging.warning("'%s' of kind '%s' not created. Check whether account and index exist." % (name, kind))
    return count

def create_input(name, kind, data):
    # kind shoud be one of input_settings.AWS_INPUT_xxx
    endpoint = IS.AWS_INPUT_ROOT + "/" + kind
    data['name'] = name
    response = my_request.request(endpoint, data, 'POST')
    return response

def delete_input(name, kind):
    endpoint = IS.AWS_INPUT_ROOT + "/" + kind + "/" + name
    response = my_request.request(endpoint, method = 'DELETE')
    logging.debug('%s of %s deleted' % (name, kind))

def delete_all_inputs():
    for kind in get_input_kinds():
        for input_name in get_input_names(kind):
            delete_input(input_name, kind)

def get_input_kinds():
    kinds = []
    response = my_request.request(IS.AWS_INPUT_ROOT)
    root = XML(response.read())
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        kinds.append(entry.find('{http://www.w3.org/2005/Atom}title').text)
    logging.info('get input kinds: %s' % kinds)
    return kinds

def get_input_names(kind):
    name = []
    response = my_request.request(IS.AWS_INPUT_ROOT + "/" + kind)
    root = XML(response.read())
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        name.append(entry.find('{http://www.w3.org/2005/Atom}title').text)
    logging.info('get inputs of %s: %s' %(kind, name))
    return name

def get_all_input_names():
    kinds = get_input_kinds()
    input_names = []
    for kind in kinds:
        input_names.extend(get_input_names(kind))
    return input_names

def validate_input(name, data):
    # check input name, account and index
    # exist_inputs = get_all_input_names()
    # if name not in exist_inputs:
    if data['aws_account'] in get_account_names() and \
            (data['index'] in get_indexes() or data['index'] == 'default'):
        return True
    return False

def build_name(name, kind, data):
    # account_kind_name_timestamp
    return '_'.join([data['aws_account'], kind, name, datetime.today().strftime("%Y%m%d%H%M%S")])

if __name__ == '__main__':
    # inputs = {
    #         IS.AWS_INPUT_CLOUDWATCH:{ # kind
    #             'rest1':{ # name
    #                 'sourcetype': 'aws:cloudwatch',
    #                 'index': 'main',
    #                 'aws_account': 'jarvis',
    #                 #'aws_iam_role': '',
    #                 'metric_namespace': 'AWS/EC2',
    #                 'metric_names': '".*"',
    #                 'metric_dimensions': '[{"InstanceID":[".*"]}]',
    #                 'period': '600',
    #                 'polling_interval': '7200',
    #                 'statistics': '["Average", "Sum", "Maximum", "Minimum"]',
    #                 'aws_regions': 'ap-southeast-1,ap-northeast-2'
    #                 }
    #             }
    # }
    # create_inputs(inputs)
    # print get_input_kinds()
    delete_all_inputs()
