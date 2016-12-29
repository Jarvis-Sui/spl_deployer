import re

auth_pat = '\[auth\]'
account_pat = '\[account:(?P<name>[\w-]+)\]'
index_pat = '\[index\]'
input_pat = '\[(?P<kind>[\w-]+)://(?P<name>[\w-]+)\]'

stanza_header = '\['

class Config(object):
    class _Config(object):
        def __init__(self):
            self.accounts = []
            self.auth = {}
            self.indexes = []
            self.inputs = {}
            with open('config.conf', 'r') as reader:
                while True:
                    line = reader.readline()
                    if line == '':
                        break
                    line = line.strip()
                    if re.match('#', line):
                        continue
                    elif re.match(auth_pat, line):
                        # get auth parameters
                        self.auth = self._get_kv_pairs(reader)
                    elif re.match(account_pat, line):
                        # get account parameters
                        name = re.search(account_pat, line).group('name')
                        account = self._get_kv_pairs(reader)
                        account['name'] = name
                        self.accounts.append(account)
                    elif re.match(index_pat, line):
                        self.indexes = self._get_indexes(reader)
                    else:
                        pass
            
            with open('inputs.conf', 'r') as reader:
                while True:
                    line = reader.readline()
                    if line == '':
                        break
                    line = line.strip()
                    if re.match('#', line):
                        continue
                    elif re.match(input_pat, line):
                        m = re.search(input_pat, line)
                        kind = m.group('kind')
                        name = m.group('name')
                        input = self._get_kv_pairs(reader)
                        if kind not in self.inputs:
                            self.inputs[kind] = {}
                        self.inputs[kind][name] = input

        def get_auth(self):
            return self.auth
        
        def get_accounts(self):
            return self.accounts

        def get_indexes(self):
            return self.indexes

        def get_inputs(self):
            return self.inputs

        def _get_kv_pairs(self, reader):
            line = reader.readline()
            pairs = {}
            while line != '' and not re.match(stanza_header, line):
                if not re.match('#', line.strip()): 
                    if '=' in line:
                        key, value = [ele.strip() for ele in line.split('=')]
                        pairs[key] = value
                line = reader.readline()
            # seek back since the stanza head is consumed by readline()
            reader.seek(-len(line), 1) 
            return pairs

        def _get_indexes(self, reader):
            line = reader.readline()
            indexes = []
            while line != '' and not re.match(stanza_header, line):
                if not re.match('#', line) and line.strip() != '':
                    indexes.append(line.strip())
                line = reader.readline()
            reader.seek(-len(line), 1)
            return indexes


    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = cls._Config()
        return cls.instance 

if __name__ == '__main__':
    config = Config()
    print config.get_auth()
    print config.get_accounts()
    print config.get_indexes()

