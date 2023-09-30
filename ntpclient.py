import ntplib
from datetime import datetime , timedelta
def get_current_time():
    try:
        c = ntplib.NTPClient()
        response = c.request('time.google.com', version=3)
        return response.tx_time
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    current_time = get_current_time()
    if current_time:
           # Convert timestamp to a datetime object
        current_datetime = datetime.utcfromtimestamp(current_time)

        # Add three hours
        new_datetime = current_datetime + timedelta(hours=3)

        # Convert the new datetime to a readable format
        readable_time = new_datetime.strftime('%Y-%m-%d %H:%M:%S UTC')

        print(f"Current Time (UTC): {readable_time}")
current_time