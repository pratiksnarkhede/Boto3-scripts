#ec2sns.py 

This GitHub repository contains a Boto3 script that focuses on checking the status of AWS EC2 instances and sending SNS notifications for instances that are running or not running. The script utilizes the Boto3 library, a Python SDK for AWS, and provides a convenient way to automate the monitoring and alerting of EC2 instances.

#EC2-weekends.py

AWS Lambda Function to Stop EC2 Instances on Weekends

This repository contains a Python AWS Lambda function that can be used to stop running EC2 instances on weekends. The function utilizes the Boto3 library to interact with the AWS EC2 service and perform the necessary actions.

Description:

The stop_running_instance function defined in the code is the main logic for stopping running EC2 instances on weekends. It follows these steps:

It creates an EC2 client using Boto3 to interact with EC2 instances.

It retrieves the current day of the week using the datetime module.

If the current day is a weekend day (Saturday or Sunday), it proceeds to the next step; otherwise, it prints a message stating that it is not a weekend and no action is required.

It uses the EC2 client to describe instances with the filter set to running instances only.

It extracts the instance IDs from the response using a list comprehension.

If there are running instances, it stops them using the EC2 client's stop_instances method and prints the instance IDs that were stopped; otherwise, it prints a message stating that there are no running instances to stop.

Finally, it returns a response indicating the successful execution of the Lambda function.
