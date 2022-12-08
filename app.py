from flask import Flask, render_template, url_for, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/start/<room>')
def start(room):
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"room: {room}, time: {current_time}")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)