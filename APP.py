from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    links = [
        {"name": "Facebook", "url": "https://www.facebook.com/abdelrhman.sobh.2025"},
        {"name": "Instagram", "url": "https://www.instagram.com/abdelr7man_sobh/?hl=ar"},
        {"name": "Tiktok", "url": "https://www.tiktok.com/@abdelr7man_sobh"},
        {"name": "WhatsApp", "url": "https://wa.me/201015816031"}
    ]
    return render_template("index.html", links=links)

if __name__ == "__main__":
    app.run(debug=True)