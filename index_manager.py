from rest_util import my_request
from xml.etree.ElementTree import XML

def create_index(name):
    data = {"name":name}
    response = my_request.request("/services/data/indexes", data, method='POST')

def create_indexes(indexes):
    exist_indexes = get_indexes()
    for index in indexes:
        if index not in exist_indexes:
            create_index(index)
    return len(indexes)

def get_indexes():
    indexes = []
    root = XML(my_request.request("/services/data/indexes").read())
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        indexes.append(entry.find('{http://www.w3.org/2005/Atom}title').text)
    return indexes

def delete_index(name):
    response = my_request.request("/services/data/indexes/%s" % name, method='DELETE')

def delete_indexes(indexes):
    exist_indexes = get_indexes()
    for index in indexes:
        if index in exist_indexes:
            delete_index(index)
    return len(indexes)


if __name__ == '__main__':
    import config
    delete_indexes(config.Config().get_indexes())
    # print get_indexes()

