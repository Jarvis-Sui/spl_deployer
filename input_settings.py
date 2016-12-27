
AWS_INPUT_ROOT = '/servicesNS/nobody/Splunk_TA_aws/splunk_ta_aws/inputs'

AWS_INPUT_CLOUDTRAIL = 'cloudtrail'
AWS_INPUT_CONFIG = 'config'
AWS_INPUT_CLOUDWATCH = 'cloudwatch'
AWS_INPUT_CLOUDWATCH_LOGS = 'cloudwatch-logs'
AWS_INPUT_DESCRIPTION = 'description'
AWS_INPUT_S3 = 's3'
AWS_INPUT_BILLING = 'billing'
AWS_INPUT_KINESIS = 'kinesis'
AWS_INPUT_CONFIG_RULES = 'config-rules'
AWS_INPUT_INSPECTOR = 'inspector'
AWS_INPUT_SQS = 'sqs'

AWS_CLOUDWATCH_MOST_SPECIFIC_DIMENSION_TYPE = {
    'AWS/EBS': 'VolumeId',
    'AWS/EC2': 'InstanceId',
    'AWS/Billing': 'ServiceName',
    'AWS/SNS': 'TopicName',
    'AWS/SQS': 'QueueName',
    'AWS/ELB': 'LoadBalancerName',
    'AWS/CloudFront': 'DistributionId',
    'AWS/DynamoDB': 'TableName',
    'AWS/ElastiCache': 'CacheClusterId',
    'AWS/ElasticMapReduce': 'JobFlowId',
    'AWS/Kinesis': 'StreamName',
    'AWS/ML': 'MLModelId',
    'AWS/OpsWorks': 'InstanceId',
    'AWS/Redshift': 'NodeID',
    'AWS/RDS': 'DBInstanceIdentifier',
    'AWS/SWF': 'Domain',
    'AWS/StorageGateway': 'GatewayId',
    'AWS/WorkSpaces': 'WorkspaceId',
    'AWS/S3': 'BucketName',
    'AWS/Lambda': 'FunctionName'
}
