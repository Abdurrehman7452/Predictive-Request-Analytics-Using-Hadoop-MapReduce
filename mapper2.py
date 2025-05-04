#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    tokens = line.split('\t')
    num_fields = len(tokens)

    if num_fields == 7:  # Type 0 record (Request data)
        record_type, request_id, client_id, api_endpoint, time_stamp, down_servers, actual_status = tokens
        print(f"{record_type}\t{request_id}\t{client_id}\t{api_endpoint}\t{actual_status}")
    
    elif num_fields == 3:  # Type 1 record (Prediction data)
        record_type, request_id, predicted_status = tokens
        print(f"{record_type}\t{request_id}\t{predicted_status}")

