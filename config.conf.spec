[auth]
# to login to splunk
authority = https://localhost:8089
username = admin
password = changeme

[account:my_account_name_1]
# can specify multiple accounts
key_id = my_key_id
secret_key = my_secret_key
# 1: Global
# 2: Gov
# 4: China
category = 1

[indexes]
# specify indexes to be added to or deleted from splunk
index_1
index_2
index_3
index_4

[input_files]
# specify input conf files. Files should be in the form of filename.conf, and be put in inputs/ dir.
# ONLY list filename here, don't append '.conf' suffix
input_file_1
input_file_2

