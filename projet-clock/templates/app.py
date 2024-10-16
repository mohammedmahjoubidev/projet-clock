from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def home():
    current_time = time.strftime('%H:%M:%S')
    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
