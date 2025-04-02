import json
import boto3
import uuid
from decimal import Decimal  # Import Decimal

# Initialize the AWS clients
dynamodb = boto3.resource('dynamodb')
order_table = dynamodb.Table('OrderTable')

# Lambda function to trigger the Step Function workflow
def triggerOrderProcessing(event, context):
    try:
        print("Received event in triggerOrderProcessing:", json.dumps(event))  # Debugging log

        # Extract order details from the event (ensure it's a valid JSON)
        body = json.loads(event.get('body', '{}'))
        
        order_id = str(uuid.uuid4())  # Generate a unique order ID
        body['orderId'] = order_id

        # Convert float values to Decimal before storing in DynamoDB
        body = convert_to_decimal(body)

        # Store order in DynamoDB
        save_order(body)

        # Start the Step Function workflow to process the order
        stepfunctions_client = boto3.client('stepfunctions')
        response = stepfunctions_client.start_execution(
            stateMachineArn='arn:aws:states:us-east-1:718361999916:stateMachine:OrderProcessingStateMachine-test-v2',
            name=order_id,
            input=json.dumps({"input": body})  # Ensure input is properly wrapped
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Order processing started successfully!',
                'executionArn': response['executionArn'],
                'orderId': order_id
            })
        }
    
    except Exception as e:
        print(f"Error in triggerOrderProcessing: {str(e)}")
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}

# Function to create an order
def createOrder(event, context):
    try:
        print("Received event in createOrder:", json.dumps(event))  # Debugging log

        order_data = event.get('input', {})
        if not order_data:
            raise ValueError("Missing 'input' key in event payload")

        order_data['status'] = 'Created'

        # Convert float values to Decimal before saving
        order_data = convert_to_decimal(order_data)
        save_order(order_data)

        return order_data
    
    except Exception as e:
        print(f"Error in createOrder: {str(e)}")
        return {'error': str(e)}

# Function to process payment
def processPayment(event, context):
    try:
        print("Received event in processPayment:", json.dumps(event))  # Debugging log

        order_data = event.get('input', {})
        if not order_data or 'orderId' not in order_data:
            raise ValueError("Invalid order data received in processPayment")

        order_id = order_data['orderId']
        amount = order_data.get('amount', 0)

        if amount <= 0:
            raise ValueError(f"Invalid payment amount for order {order_id}.")

        order_data['paymentStatus'] = 'Paid'

        # Convert float values to Decimal before updating
        order_data = convert_to_decimal(order_data)
        update_order(order_data)

        return order_data
    
    except Exception as e:
        print(f"Error in processPayment: {str(e)}")
        return {'error': str(e)}

# Function to ship an order
def shipOrder(event, context):
    try:
        print("Received event in shipOrder:", json.dumps(event))  # Debugging log

        order_data = event.get('input', {})
        if not order_data or 'orderId' not in order_data:
            raise ValueError("Invalid order data received in shipOrder")

        order_data['shippingStatus'] = 'Shipped'

        # Convert float values to Decimal before updating
        order_data = convert_to_decimal(order_data)
        update_order(order_data)

        return order_data
    
    except Exception as e:
        print(f"Error in shipOrder: {str(e)}")
        return {'error': str(e)}

# Function to send a notification
def sendNotification(event, context):
    try:
        print("Received event in sendNotification:", json.dumps(event))  # Debugging log

        order_data = event.get('input', {})
        if not order_data or 'orderId' not in order_data:
            raise ValueError("Invalid order data received in sendNotification")

        order_data['notificationStatus'] = 'Sent'

        # Convert float values to Decimal before updating
        order_data = convert_to_decimal(order_data)
        update_order(order_data)

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'Order {order_data["orderId"]} processed and notification sent!',
                'order': order_data
            })
        }
    
    except Exception as e:
        print(f"Error in sendNotification: {str(e)}")
        return {'error': str(e)}

# Helper function to save order to DynamoDB
def save_order(order_data):
    order_table.put_item(Item=order_data)

# Helper function to update an existing order in DynamoDB
def update_order(order_data):
    update_expression = "set #status = :status"
    expression_attribute_values = {':status': order_data.get('status', 'Pending')}
    expression_attribute_names = {'#status': 'status'}

    if 'paymentStatus' in order_data:
        update_expression += ", #paymentStatus = :paymentStatus"
        expression_attribute_values[':paymentStatus'] = order_data['paymentStatus']
        expression_attribute_names['#paymentStatus'] = 'paymentStatus'

    if 'shippingStatus' in order_data:
        update_expression += ", #shippingStatus = :shippingStatus"
        expression_attribute_values[':shippingStatus'] = order_data['shippingStatus']
        expression_attribute_names['#shippingStatus'] = 'shippingStatus'

    if 'notificationStatus' in order_data:
        update_expression += ", #notificationStatus = :notificationStatus"
        expression_attribute_values[':notificationStatus'] = order_data['notificationStatus']
        expression_attribute_names['#notificationStatus'] = 'notificationStatus'

    order_table.update_item(
        Key={'orderId': order_data['orderId']},
        UpdateExpression=update_expression,
        ExpressionAttributeNames=expression_attribute_names,
        ExpressionAttributeValues=expression_attribute_values
    )

# Helper function to convert float values to Decimal
def convert_to_decimal(data):
    if isinstance(data, dict):
        return {k: convert_to_decimal(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_to_decimal(v) for v in data]
    elif isinstance(data, float):  # Convert float to Decimal
        return Decimal(str(data))
    return data
