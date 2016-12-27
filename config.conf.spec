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

[index]
# specify indexes to be added to or deleted from splunk
index_1
index_2
index_3
index_4
