from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # '0.0.0.0' = 127.0.0.1 i.e. localhost
    # port = 5000 : we can modify it for localhost
    app.run(host='0.0.0.0', port=5000, debug=True) # local webserver : app.run()