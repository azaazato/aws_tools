from __future__ import print_function

import boto3

STATE = 'STOP'


def listup_instances(client):
    response = client.describe_instances(
            Filters=[
                {
                    'Name': 'tag-key',
                    'Values': ['AutoStop']
                    }
                ]
            )
    instance_ids = []
    instances = response['Reservations']
    for instance in instances:
        tags = instance['Instances'][0]['Tags']
        for tag in tags:
            if tag['Key'] == 'AutoStop' and tag['Value'] == 'True':
                instance_ids.append(instance['Instances'][0]['InstanceId'])
    return instance_ids


def lambda_handler(event, context):
    client = boto3.client('ec2')
    instance_ids = listup_instances(client)
    print('stop instances : {}'.format(instance_ids))

    if STATE == 'START':
        response = client.start_instances(
                DryRun=True,
                InstanceIds=instance_ids
        )
    elif STATE == 'STOP':
        response = client.stop_instances(
                DryRun=True,
                InstanceIds=instance_ids
        )
    else:
        raise Exception('STATE SET ERROR')
    return response
