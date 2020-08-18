import boto3

dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

def create_user_table():
    table = dynamodb.create_table(
        TableName = 'Customers',
        KeySchema = [
            {
                'AttributeName' : 'customerID',
                'KeyType' : 'HASH'
            }
        ],
        AttributeDefinitions = [
            {
                'AttributeName' : 'customerID',
                'AttributeType' : 'S'
            }
        ],
        ProvisionedThroughput = {
            'ReadCapacityUnits' : 10,
            'WriteCapacityUnits' : 10,
        }
    )
    return table

if __name__ == '__main__':
    customer_table = create_user_table()
    print("Table status:", customer_table.table_status)
