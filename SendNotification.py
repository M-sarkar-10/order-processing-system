import json

def lambda_handler(event, context):
    order_data = event
    order_id = order_data.get('orderId')
    

    print(f"Sending notification for orderId: {order_id}")
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Notification for order {order_id} sent successfully'})
    }
