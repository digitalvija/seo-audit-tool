from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/audit', methods=['POST'])
def audit():
    url = request.form.get('url')

    # Dummy result - Later we'll add real logic from /seo modules
    report = {
        "URL": url,
        "Title Tag": "Good ✅",
        "Meta Description": "Missing ❌",
        "H1 Tag": "Present ✅",
        "Robots.txt": "Found ✅",
        "Sitemap.xml": "Missing ❌",
        "HTTPS": "Yes ✅",
        "Page Speed": "65/100 ⏳",
    }

    return render_template('report.html', url=url, report=report)

if __name__ == '__main__':
    app.run(debug=True)
