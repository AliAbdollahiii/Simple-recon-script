{\rtf1\ansi\ansicpg1252\cocoartf2707
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #Simple Recon script\
import requests\
import json\
\
# Import the target URL\
target = "https://example.com"\
\
# Request to the target and get the response\
response = requests.get(target)\
\
# Retrieve the headers \
headers = response.headers\
\
# Retrieve the cookies \
cookies = response.cookies\
\
# Retrieve the HTML \
html = response.text\
\
# Search the HTML for subdomains\
subdomains = []\
for line in html.splitlines():\
    if "href" in line:\
        if "https://" in line or "http://" in line:\
            subdomain = line.split("//")[-1].split("/")[0]\
            subdomains.append(subdomain)\
\
# Print the headers, cookies, and subdomains\
print("Headers:", json.dumps(headers, indent=4))\
print("Cookies:", json.dumps(cookies, indent=4))\
print("Subdomains:", subdomains)\
}