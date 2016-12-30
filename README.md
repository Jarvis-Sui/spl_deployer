# How to USE
Configure in config.conf, and run `python deploy_input.py`.

# deploy\_input
Program entry point. Run `python deploy_input.py` to create account, indexes and inputs. You can also use functions in *account|indexes|input\_manager* to customize your own deployment.

# [account|indexes|input]\_manager
Provide methods to manipulate account/index/input, respectively

`delete_indexes` and `create_indexes` loads index names from config.conf file, and will check whether the index exists before creating/deleting it. However, `delete_index` and `create_index` don't do any validation.

`create_inputs` loads inputs from inputs.conf. It will check whether index and account exists before creating inputs. However, `create_input` does not make such validation.

# rest\_util
Make REST calls

# config.conf 
1. specify splunkd, username and password 
2. specify aws accounts
3. specify indexes that need to be created

# inputs 
Containing input conf files. Input conf file is similar to the splunk's inputs.conf file, but some keys are different and no default value is provided if a key is not assigned a value.

# log
Log is written to request.log under the same folder.
