import json
from datetime import datetime, timedelta

devices = ["Android_App", "iOS_15", "Web_Dashboard", "API_Client"]
http_codes = ["HTTP_200_OK", "HTTP_500_INTERNAL_ERROR", "HTTP_429_RATE_LIMIT", "HTTP_403_FORBIDDEN"]
servers = ["ai-node-04.delhi.server.internal:8080", "gpu-cluster-delhi.internal.net:9092", "eu-west-1.aws.internal:443"]

data_pipeline = []
start_time = datetime(2026, 5, 19, 9, 0, 0)

for i in range(1, 201):
    current_time = start_time + timedelta(minutes=i*2)
    
    if i % 15 == 0:
        ts = current_time.strftime("%d/%m/%Y %H:%M")
    else:
        ts = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
    session = f"USR_{1000 + i}"
    
    device = devices[i % len(devices)]
    code = http_codes[i % len(http_codes)]
    query = "Explain quantum physics" if i % 2 == 0 else "Write a python code"
    prompt = f"Req_SRC: {device} | STATUS: [{code}] | Msg: {query}"
    
    if i % 10 == 0:
        conf = None               
    elif i % 12 == 0:
        conf = "High"            
    elif i % 14 == 0:
        conf = f"{70 + (i%20)}%"  
    else:
        conf = round(0.5 + (i % 49)/100, 2) 
        
    server = servers[i % len(servers)]
    trace = f"Routing -> https://{server}/v1/chat"
    if i % 20 == 0:
        trace = None              
        
    if i % 8 == 0:
        latency = "timeout_error"
    elif i % 25 == 0:
        latency = None
    else:
        latency = round(100.5 + (i * 2.5), 1)

    row = {
        "timestamp": ts,
        "session_id": session,
        "raw_system_prompt": prompt,
        "ai_confidence_score": conf,
        "backend_server_trace": trace,
        "execution_latency_ms": latency
    }
    data_pipeline.append(row)

file_name = 'data/raw/api_logs_v1_2026-05-19.json'
with open(file_name, 'w') as f:
    json.dump(data_pipeline, f, indent=4)
print(f"Generated {len(data_pipeline)} mock log entries in {file_name}")