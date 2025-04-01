import json

def lambda_handler(event, context):
    order_data = event
    order_id = order_data.get('orderId')
    
    
    print(f"Processing payment for orderId: {order_id}")
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Payment for order {order_id} processed successfully'})
    }
