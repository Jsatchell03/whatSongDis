from flask import Flask, jsonify, request, render_template
from pytube import YouTube
app = Flask(__name__)

@app.route('/')
def build():
    return render_template("./index.html")

@app.route("/response", methods=["POST", "GET"])
def response():
    # Need to prevent default on button clik somehow
    # YouTube("https://www.youtube.com/watch?v=gte3BoXKwP0&pp=ygUVcG9ja2V0ZnVsIG9mIHN1bnNoaW5l").streams.first.downlad()
    return render_template("./response.html", link = request.form.get('userLink'))
