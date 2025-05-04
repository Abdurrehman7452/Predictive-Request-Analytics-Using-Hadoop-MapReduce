#!/usr/bin/env python3
import sys

for input_line in sys.stdin:
    input_line = input_line.strip()
    columns = input_line.split('\t')
    num_columns = len(columns)

    if num_columns == 4:  # If we have both prediction and actual status
        client_id, cost, prediction, actual_status = columns
        print(f"{client_id}\t{cost}\t{prediction}\t{actual_status}")

    elif num_columns == 3:  # If only actual status is present
        client_id, cost, actual_status = columns
        print(f"{client_id}\t{cost}\t{actual_status}")

