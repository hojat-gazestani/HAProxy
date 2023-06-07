import requests
from bs4 import BeautifulSoup

from haproxyadmin import haproxy

hap = haproxy.HAProxy(socket_file='/run/haproxy/admin.sock')

backends = hap.backends()

# stats_url = "http://localhost:9999/stats"  # Replace with your HAProxy stats URL
backend_name = "myapps"  # Replace with your backend name

response = requests.get(stats_url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the backend section
backend_section = soup.find("h2", text=backend_name)
if backend_section is None:
    print("Backend '{}' not found.".format(backend_name))
    exit()

# Find the sticky table section within the backend
sticky_table_section = backend_section.find_next("h3", text="Sticky table")
if sticky_table_section is None:
    print("Sticky table information not found for backend '{}'.".format(backend_name))
    exit()

# Extract the sticky table records
sticky_table_records = sticky_table_section.find_next("tbody").find_all("tr")
if not sticky_table_records:
    print("No sticky table records found for backend '{}'.".format(backend_name))
    exit()

# Print the sticky table records
print("Backend: {}".format(backend_name))
for record in sticky_table_records:
    record_key = record.find("td", class_="col0").text.strip()
    print("  Record: {}".format(record_key))
