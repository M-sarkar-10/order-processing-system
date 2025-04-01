import json

# Lambda function to create an order
def create_order(event, context):
    order_data = event.get('body', {})
    order_id = order_data.get('orderId')
    item = order_data.get('item')
    quantity = order_data.get('quantity')
    price = order_data.get('price')

    if not order_id or not item or not quantity or not price:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid order data'})
        }

    print(f"Creating order with orderId: {order_id}, Item: {item}, Quantity: {quantity}, Price: {price}")
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Order {order_id} created successfully'})
    }

# Lambda function to process the payment
def process_payment(event, context):
    payment_data = event.get('body', {})
    order_id = payment_data.get('orderId')
    payment_status = payment_data.get('paymentStatus')

    if not order_id or not payment_status:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid payment data'})
        }

    print(f"Processing payment for orderId: {order_id}, Status: {payment_status}")
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Payment for order {order_id} processed successfully'})
    }

# Lambda function to ship the order
def ship_order(event, context):
    shipment_data = event.get('body', {})
    order_id = shipment_data.get('orderId')
    shipping_address = shipment_data.get('shippingAddress')

    if not order_id or not shipping_address:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid shipment data'})
        }

    print(f"Shipping order with orderId: {order_id}, Shipping Address: {shipping_address}")
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Order {order_id} shipped successfully'})
    }

# Lambda function to send a notification
def send_notification(event, context):
    notification_data = event.get('body', {})
    order_id = notification_data.get('orderId')
    notification_status = notification_data.get('notificationStatus')

    if not order_id or not notification_status:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid notification data'})
        }

    print(f"Sending notification for orderId: {order_id}, Status: {notification_status}")
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Notification for order {order_id} sent successfully'})
    }
