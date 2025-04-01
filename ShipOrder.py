import json

def lambda_handler(event, context):
    order_data = event
    order_id = order_data.get('orderId')
    
    
    print(f"Shipping order with orderId: {order_id}")
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Order {order_id} shipped successfully'})
    }
