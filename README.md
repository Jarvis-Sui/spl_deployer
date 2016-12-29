
# deploy\_input
Program entry point. Run `python deploy\_input.py` to create account, indexes and inputs. You can also use functions in *account|indexes|input\_manager* to customize your own deployment.

# [account|indexes|input]\_manager
Provide methods to manipulate account/index/input, respectively

`delete\_indexes` and `create\_indexes` loads index names from config.conf file, and will check whether the index exists before creating/deleting it. However, `delete\_index` and `create\_index` don't do any validation.

`create\_inputs` loads inputs from inputs.conf. It will check whether index and account exists before creating inputs. However, `create_input` does not make such validation.

# rest\_util
Make REST calls

# config.conf 
1. specify splunkd, username and password 
2. specify aws accounts

# inputs.conf
specify inputs. This conf file is similar to the splunk's inputs.conf file, but some keys are different and no default value is provided if a key is not assigned a value.

# log
Log is write to request.log under the same folder.
