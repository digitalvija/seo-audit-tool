from flask import Flask, render_template, request
import seo.technical as technical
import seo.on_page as on_page
import seo.speed as speed

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/audit", methods=["POST"])
def audit():
    url = request.form["url"]
    tech_report = technical.analyze(url)
    on_page_report = on_page.analyze(url)
    speed_report = speed.analyze(url)
    return render_template("report.html", tech=tech_report, onpage=on_page_report, speed=speed_report)

# This is required for WSGI (Passenger)
application = app