from bs4 import BeautifulSoup
import requests

def on_page_seo(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    title = soup.title.string if soup.title else "Missing"
    meta_desc = soup.find("meta", attrs={"name": "description"})
    h1 = soup.find_all("h1")
    images = soup.find_all("img")

    return {
        "title": title,
        "meta_description": meta_desc['content'] if meta_desc else "Missing",
        "h1_count": len(h1),
        "missing_alt_count": sum(1 for img in images if not img.get("alt"))
    }
