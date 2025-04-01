import json
import boto3

sfn_client = boto3.client('stepfunctions')

def lambda_handler(event, context):
    # Get order details from API request
    order_data = json.loads(event['body'])
    order_id = order_data.get('orderId')

    input_data = {
        "orderId": order_id,
        "item": order_data.get("item"),
        "quantity": order_data.get("quantity"),
        "price": order_data.get("price")
    }

    response = sfn_client.start_execution(
        stateMachineArn='arn:aws:states:us-east-1:718361999916:stateMachine:OrderProcessingStateMachine', 
        name=f"order-execution-{order_id}",
        input=json.dumps(input_data)
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Order {order_id} processing started successfully'})
    }
