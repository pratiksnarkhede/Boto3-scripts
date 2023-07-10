import boto3

client = boto3.client('sns')

def lambda_handler(event, context):
    
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    message = f"A new object {object_key} was uploaded to bucket {bucket_name}."
    topic_arn = 'arn:aws:sns:us-east-1:899048518063:s3eventsns'
    # replace topic_arn with your topic_arn
    client.publish(TopicArn=topic_arn, Message=message)
