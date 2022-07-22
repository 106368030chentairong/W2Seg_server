import boto3
import time

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('users')

'''
table.put_item(
   Item={
        'username': 'janedoe',
        'first_name': 'Jane',
        'last_name': 'Doe',
        'age': 30,
        'account_type': 'standard_user',
    }
)
'''
start = time.time()
response = table.get_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)
end = time.time()
item = response['Item']
print(item)
print(format(end-start))