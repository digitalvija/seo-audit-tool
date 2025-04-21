import requests

def get_pagespeed_score(url, api_key):
    endpoint = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={api_key}"
    response = requests.get(endpoint).json()
    
    score = response['lighthouseResult']['categories']['performance']['score'] * 100
    return round(score)
