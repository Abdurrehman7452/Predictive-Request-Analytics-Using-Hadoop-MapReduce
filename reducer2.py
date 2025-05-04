#!/usr/bin/env python3
import sys

# Dictionary to hold request details
client_requests = {}

# Cost for each API endpoint
api_cost = {
    'user/profile': 100,
    'user/settings': 200,
    'order/history': 300,
    'order/checkout': 400,
    'product/details': 500,
    'product/search': 600,
    'cart/add': 700,
    'cart/remove': 800,
    'payment/submit': 900,
    'support/ticket': 1000
}

# Function to update request data
def process_request(request_id, client_id, endpoint, actual_status):
    client_requests[request_id] = {
        'client_id': client_id,
        'cost': api_cost.get(endpoint, 0),  # Default to 0 if unknown
        'actual_status_code': actual_status,
        'is_prediction_correct': None
    }

# Function to process the prediction
def process_prediction(request_id, predicted_status):
    if request_id in client_requests:
        if client_requests[request_id]['actual_status_code'] == predicted_status:
            client_requests[request_id]['is_prediction_correct'] = True
        else:
            client_requests[request_id]['is_prediction_correct'] = False

def main():
    # Reading and processing input
    for line in sys.stdin:
        line = line.strip()
        tokens = line.split('\t')
        token_count = len(tokens)

        if token_count == 5:  # Request Data
            record_type, request_id, client_id, api_endpoint, actual_status = tokens
            process_request(request_id, client_id, api_endpoint, actual_status)

        elif token_count == 3:  # Prediction Data
            record_type, request_id, predicted_status = tokens
            process_prediction(request_id, predicted_status)

    # Output the result for each request
    for request_id, details in client_requests.items():
        if details['is_prediction_correct'] is None:  # No prediction available
            print(f"{details['client_id']}\t{details['cost']}\t{details['actual_status_code']}")
        else:
            prediction_result = 1 if details['is_prediction_correct'] else 0
            print(f"{details['client_id']}\t{details['cost']}\t{prediction_result}\t{details['actual_status_code']}")

if __name__ == "__main__":
    main()

