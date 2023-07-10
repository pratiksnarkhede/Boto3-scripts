import boto3

instance_id = input("Enter the ID of the intance you want to track: ") 
sns_topic_arn = 'arn:aws:sns:us-east-1:899048518063:Ec2'

ec2 = boto3.resource('ec2')
sns = boto3.client('sns')

instance = ec2.Instance(instance_id)
state = instance.state['Name']

if state == 'running':
    message = 'EC2 instance {} is running!'.format(instance_id)
    subject = 'EC2 Instance Running'
    sns.publish(TopicArn=sns_topic_arn, Message=message, Subject=subject)
    print('EC2 instance is running Notification sent!')
else:
    print('EC2 instance is not running')


