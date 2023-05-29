import requests
import threading

def send_requests():
<<<<<<< HEAD
    url = 'http://192.168.56.21:81'
=======
    url = 'http://192.16.56.21:81'
>>>>>>> 87515f4fc3dd6a76497dd3a19355def92714fb00

    for _ in range(1000):
        threading.Thread(target=send_request, args=(url,)).start()

def send_request(url):
    try:
        response = requests.get(url)
        print(f"Response from server: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")

send_requests()
