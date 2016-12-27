from account_manager import create_accounts
from index_manager import create_indexes
from input_manager import create_inputs
from config import Config


def deploy_inputs():
    print "Creating accounts\n================"
    n = create_accounts(Config().get_accounts())
    print "Created %d accounts\n================" % n
    print "Creating indexes\n================="
    n = create_indexes(Config().get_indexes())
    print "Created %d indexes\n================" % n

if __name__ == '__main__':
    deploy_inputs()
