import input_settings as IS
from rest_util import my_request
from xml.etree.ElementTree import XML

import logging

def create_inputs(inputs):
    for kind, input in inputs.iteritems():
        for name, data in input.iteritems():
            create_input(name, kind, data)

def create_input(name, kind, data):
    # kind shoud be one of input_settings.AWS_INPUT_xxx
    endpoint = IS.AWS_INPUT_ROOT + "/" + kind
    data['name'] = name
    response = my_request.request(endpoint, data, 'POST')
    return response

def delete_input(name, kind):
    endpoint = IS.AWS_INPUT_ROOT + "/" + kind + "/" + name
    response = my_request.request(endpoint, method = 'DELETE')
    logging.debug('%s of %s deleted' % (input_name, kind))

def delete_all_inputs():
    kinds = get_input_kinds()
    for kind in kinds:
        input_names = get_input_names(kind)
        for input_name in input_names:
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

if __name__ == '__main__':
    #data = {
    #        'sourcetype': 'aws:cloudwatch',
    #        'index': 'main',
    #        'aws_account': 'jarvis2',
    #        'metric_namespace': 'AWS/EC2',
    #        'metric_names': '".*"',
    #        'metric_dimensions': '[{"instanceID":[".*"]}]',
    #        'period': 600,
    #        'polling_interval': 7200,
    #        'statistics': '["Average", "Sum", "Maximum", "Minimum"]',
    #        'aws_regions': 'ap-southeast-1,ap-northeast-2'
    #        }
    #create_input('cloudwatch-rest', 'cloudwatch', data)

    #import input_settings as IS
    #inputs = {
    #        IS.AWS_INPUT_CLOUDWATCH:{ # kind
    #            'cloudwatch-rest':{ # name
    #                'sourcetype': 'aws:cloudwatch',
    #                'index': 'main',
    #                'aws_account': 'jarvis2',
    #                'metric_namespace': 'AWS/EC2',
    #                'metric_names': '".*"',
    #                'metric_dimensions': '[{"instanceID":[".*"]}]',
    #                'period': 600,
    #                'polling_interval': 7200,
    #                'statistics': '["Average", "Sum", "Maximum", "Minimum"]',
    #                'aws_regions': 'ap-southeast-1,ap-northeast-2'
    #                }
    #            }
    #}
    #create_input(inputs)

    #delete_input('cloudwatchlogs_4', IS.AWS_INPUT_CLOUDWATCH_LOGS)
    print get_input_kinds()
