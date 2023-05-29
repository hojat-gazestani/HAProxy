import requests
import threading

def send_requests():
    url = 'http://192.16.56.22:8010'

    for _ in range(2):
        threading.Thread(target=send_request, args=(url,)).start()

def send_request(url):
    try:
        response = requests.get(url)
        print(f"Response from server: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")

send_requests()