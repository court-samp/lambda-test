import boto3
import sysv

dynamodb = boto3.resource('dynamodb')

def create_table():

    table = dynamodb.create_table(
        TableName = Customers,
        KeySchema = [
            {
                'AttributeName' : 'customerID',
                'KeyType' : 'HASH'
            }
        ],
        AttributeDefinitions = [
            {
                'AttributeName' : 'cust_name',
                'AttributeType' : 'S'
            },
            {
                'AttributeName' : 'Territory',
                'AttributeType' : 'N'
            },
            {
                'AttributeName' : 'SA'
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
        customer_table = create_table()
        print("Table status:", customer_table.table_status)
