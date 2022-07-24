import boto3
import time
import asyncio

from boto3.dynamodb.conditions import Key

class consql():
    def __init__(self) -> None:
        self.dynamodb = None
        
    def connect(self):
        # Get the service resource.
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('word_table')

    def put_word(self, userid, sentence):
        for word in sentence:
            self.check_put(userid, word)

    def check_put(self, userid, word):
        self.connect()
        num = self.check_num(userid, word)
        if num != None:
            num += 1
        else:
            num = 1

        self.table.put_item(
            Item={
                'userid': userid,
                'word': word,
                'num': num
            }
        )
    def check_num(self, userid, word):
        response = self.table.get_item(
            Key={
                'userid': userid,
                'word': word,
            }
        )
        if "Item" in response:
            return response['Item']['num']
        else:
            return None

    def get_word_num(self, userid, word):
        self.connect()
        response = self.table.get_item(
            Key={
                'userid': userid,
                'word': word,
            }
        )
        #print(response)
        if "Item" in response:
            return response['Item']['num']
        else:
            return None

    def get_top_num(self, userid):
        self.connect()
        response = self.table.query(
            Limit = 3,
            IndexName='to-timestamp-index',
            KeyConditionExpression=Key('userid').eq(userid)
        )
        print(response)

'''
socep = consql()
socep.connect()
num = socep.put_word("123a", [['我', '要', '買', ' macbook', ' air']])
print(num)

table.get_item(Key={'userid': "Uc8fdb046e4e5bd2693aa12b10fae64ad","word":"觀測"})


table.query(Limit = 1,KeyConditionExpression=Key('userid').eq("Uc8fdb046e4e5bd2693aa12b10fae64ad")& Key('num').lte(5), ScanIndexForward=False)
'''