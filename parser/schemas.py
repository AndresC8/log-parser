import shlex
from datetime import datetime, timezone

line = """

date=2025-03-12 time=08:21:34 devname=FGT60F type=event subtype=user srcip=185.199.108.166 user="admin" action=login status=failed msg="Administrator login failed"

"""

def parse_fortigate_kv(line: str):
    data = {}
    tokens = shlex.split(line.strip())

    for token in tokens:
        if "=" not in token:
            continue
        
        k, v = token.split("=", 1)
        data[k] = v

    return data

def build_timestamp(evt: dict):
    if "date" in evt and "time" in evt:
        try:
            dt = datetime.strptime(f"{evt['date']} {evt['time']}", "%Y-%m-%d %H:%M:%S")
            return dt.isoformat()
        except ValueError:
            pass

    if "eventtime" in evt:
        try:
            epoch = int(evt["eventtime"])
            dt = datetime.fromtimestamp(epoch, tz=timezone.utc)
            return dt.isoformat()
        except Exception:
            return None
        
def validate_minimum(evt: dict):
    if "srcip" not in evt:
        return False
    
    ts = build_timestamp(evt)

    return ts is not None

def mapping_fortigate_event(evt: dict):
    if not validate_minimum(evt):
        return None
    
    timestamp = build_timestamp(evt)
    if not timestamp:
        return None
    
    event_type = "other"

    action = evt.get("action", "")
    status = evt.get("status", "")

    if action == "login" and status == "failed":
        event_type = "login_failed"

    elif action == "login" and status == "succes":
        event_type = "login_success"

    elif action == "deny":
        event_type = "traffic_deny"

    normalized = {
        "timestamp": timestamp,
        "source_ip": evt.get("srcip"),
        "username": evt.get("user"),
        "event_type": event_type,
        "vendor": "fortigate",
        "raw": evt
    }

    return normalized


evt = parse_fortigate_kv(line)

timestamp = build_timestamp(evt)

print(mapping_fortigate_event(evt))