import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__)

def crawl(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def extract_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    links =  soup.find_all('a')
    urls = []
    for link in links:
        herf = link['href']
        urls.append(herf)
    return urls
        

# Example usage
url = "https://www.google.com/search?q=response+python&oq=&gs_lcrp=EgZjaHJvbWUqCQgCEEUYOxjCAzIJCAAQRRg7GMIDMgkIARBFGDsYwgMyCQgCEEUYOxjCAzIJCAMQRRg7GMIDMgkIBBBFGDsYwgMyCQgFEEUYOxjCAzIJCAYQRRg7GMIDMgkIBxBFGDsYwgPSAQk0OTY3NmowajeoAgiwAgE&sourceid=chrome&ie=UTF-8"
html_content = crawl(url)
if html_content:
    text = extract_text(html_content)

@app.route('/', methods=['GET', 'POST'])
def home():
    text = []
    if request.method == 'POST':
        url = request.form['url']  # Get the URL from the form input
        html_content = crawl(url)
        if html_content:
            text = extract_text(html_content)  # Extract URLs from the content

    return render_template('index.html', urls=text)

if __name__ == '__main__':
    app.run(debug=True)




    
