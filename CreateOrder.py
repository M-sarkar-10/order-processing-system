import json

def lambda_handler(event, context):
    # Print the event object for debugging purposes
    print(f"Received event: {json.dumps(event)}")

    # Parse the JSON body of the request (it's usually a string in the event body)
    try:
        order_data = json.loads(event['body'])  # Parse the incoming JSON body
        
        # Extract orderId from the parsed data
        order_id = order_data.get('orderId')
        
        if not order_id:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Missing orderId'})
            }

        print(f"Creating order with orderId: {order_id}")
        
        # Return a success response
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'Order {order_id} created successfully'})
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal server error'})
        }
