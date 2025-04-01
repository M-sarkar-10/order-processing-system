import json

def lambda_handler(event, context):
    order_data = event
    is_valid = True
    error_message = ''
    
   
    if not order_data.get('orderId') or not order_data.get('item') or not order_data.get('quantity'):
        is_valid = False
        error_message = 'Missing required fields.'
    
    if not is_valid:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Order validation failed', 'error': error_message})
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Order is valid'})
    }
