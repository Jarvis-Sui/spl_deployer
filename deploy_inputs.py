from account_manager import create_accounts, delete_all_accounts
from index_manager import create_indexes, delete_indexes
from input_manager import create_inputs, delete_all_inputs
from config import Config


def deploy_inputs():
    print "Creating accounts\n================"
    n = create_accounts(Config().get_accounts())
    print "Created %d accounts\n================" % n
    print "Creating indexes\n================="
    n = create_indexes(Config().get_indexes())
    print "Created %d indexes\n================" % n
    print "Creating inputs\n=================="
    #print Config().get_inputs()
    n = create_inputs(Config().get_inputs())
    print "Create %d inputs\n==================" % n

def clear_all():
    delete_all_inputs()
    delete_all_accounts()
    delete_indexes(Config().get_indexes())

if __name__ == '__main__':
    deploy_inputs()
