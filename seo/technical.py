import requests

def check_robots_sitemap(url):
    domain = url.replace("https://", "").replace("http://", "").strip("/")
    robots = f"https://{domain}/robots.txt"
    sitemap = f"https://{domain}/sitemap.xml"
    
    robots_status = requests.get(robots).status_code
    sitemap_status = requests.get(sitemap).status_code
    
    return {
        "robots.txt": "Present" if robots_status == 200 else "Missing",
        "sitemap.xml": "Present" if sitemap_status == 200 else "Missing"
    }
