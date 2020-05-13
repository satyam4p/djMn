from datetime import datetime


def generate_timestamp():
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S') + str(datetime.timestamp(datetime.now())).split('.')[1]
    print("timestamp is:: ",timestamp)
    return timestamp