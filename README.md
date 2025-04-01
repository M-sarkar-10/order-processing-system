# Order Processing System

## Overview
This project is a **Serverless Order Processing System** implemented using AWS Step Functions and Lambda. The system automates the order processing workflow, integrating various AWS services for scalability and efficiency.

## Architecture
The order processing system follows a **state machine workflow** using AWS Step Functions. The main stages include:
1. **Create Order** - Stores order details.
2. **Process Payment** - Simulates payment processing.
3. **Ship Order** - Initiates order shipment.
4. **Send Notification** - Notifies the customer about the order status.

Each step is handled by a separate AWS Lambda function.

## AWS Services Used
- **AWS Lambda** (Python)
- **AWS Step Functions**
- **Amazon API Gateway**
- **Amazon CloudWatch** (Logging & Monitoring)
- **AWS IAM** (Role Permissions)

## Deployment
This project is deployed using the **Serverless Framework**.

### Prerequisites
- AWS account
- Node.js & npm installed
- Serverless Framework installed (`npm install -g serverless`)
- AWS CLI configured with credentials

### Deploy the Application
To deploy the service, run the following command in your project folder:
```bash
serverless deploy
```

## API Endpoints
The following API endpoints are available:
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/order` | POST | Create a new order |
| `/order/{orderId}` | GET | Get order status |

## Local Development & Testing
To invoke a function locally:
```bash
serverless invoke local --function createOrder
```
To remove the deployment:
```bash
serverless remove
```

## Repository Structure
```
order-processing-system/
│-- handler.py  # Main Lambda handler functions
│-- serverless.yml  # Serverless framework configuration
│-- requirements.txt  # Python dependencies
│-- README.md  # Project documentation
```

## License
This project is open-source and available under the MIT License.

## Author
[Moupriya] - AWS Cloud Engineer

