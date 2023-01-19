# Simple-recon-script
import requests
import json

# Import the target URL
target = "https://example.com"

# Request to the target and get the response
response = requests.get(target)

# Retrieve the headers 
headers = response.headers

# Retrieve the cookies 
cookies = response.cookies

# Retrieve the HTML 
html = response.text

# Search the HTML for subdomains
subdomains = []
for line in html.splitlines():
    if "href" in line:
        if "https://" in line or "http://" in line:
            subdomain = line.split("//")[-1].split("/")[0]
            subdomains.append(subdomain)

# Print the headers, cookies, and subdomains
print("Headers:", json.dumps(headers, indent=4))
print("Cookies:", json.dumps(cookies, indent=4))
print("Subdomains:", subdomains)
