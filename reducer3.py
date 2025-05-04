#!/usr/bin/env python3
import sys

# Dictionary to store statistics for each client
client_summary = {}

def process_record(client_id, cost, prediction, actual_status):
    cost = int(cost)
    prediction = int(prediction)
    actual_status = int(actual_status)

    if client_id not in client_summary:
        client_summary[client_id] = 
        {-
            'correct_predictions': 0,
            'total_requests': 0,
            'accumulated_cost': 0
        }
    
    # Update statistics based on the data
    client_summary[client_id]['correct_predictions'] += prediction
    client_summary[client_id]['total_requests'] += 1
    if actual_status == 200:
        client_summary[client_id]['accumulated_cost'] += cost

def process_missing_prediction(client_id, cost, actual_status):
    cost = int(cost)
    actual_status = int(actual_status)
    
    if actual_status == 200:
        if client_id not in client_summary:
            client_summary[client_id] = {
                'correct_predictions': 0,
                'total_requests': 0,
                'accumulated_cost': cost
            }
        else:
            client_summary[client_id]['accumulated_cost'] += cost

def main():
    for line in sys.stdin:
        line = line.strip()
        columns = line.split('\t')
        num_columns = len(columns)

        if num_columns == 4:
            client_id, cost, prediction, actual_status = columns
            process_record(client_id, cost, prediction, actual_status)
        elif num_columns == 3:
            client_id, cost, actual_status = columns
            process_missing_prediction(client_id, cost, actual_status)

    # Print the results
    for client_id, stats in client_summary.items():
        success_rate = f"{stats['correct_predictions']}/{stats['total_requests']}"
        print(f"{client_id} {success_rate} {stats['accumulated_cost']}")

if __name__ == "__main__":
    main()

