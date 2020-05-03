import botocore
import boto3

ec2 = boto3.client('ec2')
rds = boto3.client('rds')

instances = ['i-09bfb5917e6433936', 'i-0b440ab36a0e4bf74']

rds = 'jay'

def start_ec2(event, context):        
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))


def stop_ec2(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))

def start_rds(event, context):
    result = rds.start_db_instance(DBInstanceIdentifier=rds)
    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response


def stop_rds(event, context):
    result = rds.stop_db_instance(DBInstanceIdentifier=rds)
    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response

# get the list of all the ec2 instances
def get_all_ec2_ids():
    response = ec2.describe_instances(DryRun=False)
    instances = []
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            # This sample print will output entire Dictionary object
            # This will print will output the value of the Dictionary key 'InstanceId'
            instances.append(instance["InstanceId"])
    return instances
