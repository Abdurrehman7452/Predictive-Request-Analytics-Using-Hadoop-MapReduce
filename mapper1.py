#!/usr/bin/env python3
import sys

def process_request(line):
    parts = line.strip().split()
    
    # check Request data (4 or 5 parts)
    if len(parts) >= 4:  
        request_id, client_id, endpoint, timestamp = parts[:4]
        
        #  filling missing servers down 
        servers_down = parts[4] if len(parts) == 5 else "0.0"  
        return f"{timestamp},{request_id},{client_id},{endpoint},{servers_down},REQUEST"
    
    # check Prediction data (2 parts)
    elif len(parts) == 2:  
        request_id, predicted_status = parts
        return f"{request_id},{predicted_status},PREDICTION"
    
    return None

for line in sys.stdin:
    result = process_request(line)
    
    if result: # success  
        print(result)

