from flask import Flask, jsonify, request, render_template
from yt_dlp import YoutubeDL
app = Flask(__name__)

@app.route('/')
def build():
    return render_template("./index.html")

@app.route("/response", methods=["POST", "GET"])
def response():
    # one request but useres can add a time stamp to start at for song recog. 
    # Downlad mp3 file to databse
    # From database get mp3 then convert to 

    YoutubeDL().download(request.form.get('userLink'))
    return render_template("./response.html", link = request.form.get('userLink'))


