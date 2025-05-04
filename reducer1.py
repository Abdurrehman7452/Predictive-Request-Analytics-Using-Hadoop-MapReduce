#!/usr/bin/env python3
import sys

requests = {}
predictions = {}

# Initialize server dictionary with counts
endpoints_info = {
    'user/profile': {'last_time': '', 'users': set(), 'servers_available': 3},
    'user/settings': {'last_time': '', 'users': set(), 'servers_available': 3},
    'order/history': {'last_time': '', 'users': set(), 'servers_available': 3},
    'order/checkout': {'last_time': '', 'users': set(), 'servers_available': 3},
    'product/details': {'last_time': '', 'users': set(), 'servers_available': 3},
    'product/search': {'last_time': '', 'users': set(), 'servers_available': 3},
    'cart/add': {'last_time': '', 'users': set(), 'servers_available': 3},
    'cart/remove': {'last_time': '', 'users': set(), 'servers_available': 3},
    'payment/submit': {'last_time': '', 'users': set(), 'servers_available': 3},
    'support/ticket': {'last_time': '', 'users': set(), 'servers_available': 3},
}

for input_line in sys.stdin:
    input_line = input_line.strip()
    components = input_line.split(',')

    if len(components) == 6 and components[-1] == "REQUEST":  # Request lines
        time_stamp, req_id, client, endpoint, down_servers, _ = components
        down_servers = int(float(down_servers))

        # If the request is from the same client in the same timestamp, ignore it
        if client in requests and requests[client] == time_stamp:
            continue

        # Determine if the request is successful (200) or fails (500)
        if down_servers == 3:  # All servers down
            actual_code = 500
        else:
            endpoint_data = endpoints_info[endpoint]
            if endpoint_data['last_time'] != time_stamp:
                # New time, reset server availability
                endpoint_data['servers_available'] = 3 - down_servers - 1
                endpoint_data['users'].clear()
                actual_code = 200
            elif client not in endpoint_data['users'] and endpoint_data['servers_available'] > 0:
                # Client request is processed
                endpoint_data['servers_available'] -= 1
                actual_code = 200
            else:
                # Request fails if no servers are available or client has already requested
                actual_code = 500

            endpoint_data['last_time'] = time_stamp
            endpoint_data['users'].add(client)

        requests[client] = time_stamp

        # Store the request information in a dictionary
        predictions[req_id] = {
            'client': client,
            'endpoint': endpoint,
            'timestamp': time_stamp,
            'down_servers': down_servers,
            'actual_status': actual_code,
            'predicted_status': ''  
        }

    elif len(components) == 3 and components[-1] == "PREDICTION":  
        req_id, predicted_code, _ = components

        # Update the prediction status for the request if it exists
        if req_id in predictions:
            predictions[req_id]['predicted_status'] = predicted_code

for req_id, details in predictions.items():
    print(f"0\t{req_id}\t{details['client']}\t{details['endpoint']}\t{details['timestamp']}\t{details['down_servers']}\t{details['actual_status']}")
    if details['predicted_status']:
        print(f"1\t{req_id}\t{details['predicted_status']}")

