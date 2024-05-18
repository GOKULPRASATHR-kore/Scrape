from flask import Flask, request, jsonify
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    try:
        url_to_scrape = request.args.get('url')
        app.logger.info(url_to_scrape)
        
        if not url_to_scrape:
            return jsonify({"error": "No URL provided"}), 400
        
        req = Request(url_to_scrape, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
        request_page = urlopen(req)
        page_html = request_page.read()
        request_page.close()
        
        html_soup = BeautifulSoup(page_html, 'html.parser')
        html_content = html_soup.prettify()
        
        return jsonify({"html": html_content}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Server is Running"}), 200

if __name__ == '__main__':
    app.run()
