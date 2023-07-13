import boto3
import datetime

def lambda_handler(event, context):
    return stop_running_instance(event, context)

def stop_running_instance(event,context):
    ec2=boto3.client('ec2',region_name='ap-south-1')
    current_day =datetime.datetime.now().strftime('%A')

    if current_day in ['saturday','sunday']:
        response = ec2.describe_instances(
            Filters=[
                {'name': 'instace-state-name', 'Values':['running']}
                ]
        )

        instance_ids = [],
        for reservation in  response['Reservations']: 
            for instance in ['Instances']:
                instance_ids.append(instance['InstanceId'])

        if instance_ids:
            ec2.client.stop_instances(Instance_Ids = instance_ids)
            print('instance stopped:',instance_ids)
        else:
            print('No instance is running to stop')

    else:
        print('Not a weekend. No action is required')

    return{
        'statusCode': 200,
        'body': 'function executed sucessfully'

    }
