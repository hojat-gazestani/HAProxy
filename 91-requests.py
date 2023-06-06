import requests
import threading

def send_requests():
    url = 'http://192.168.56.21:81'

    for _ in range(1000):
        threading.Thread(target=send_request, args=(url,)).start()

def send_request(url):
    try:
        response = requests.get(url)
        print(f"Response from server: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")

send_requests()
