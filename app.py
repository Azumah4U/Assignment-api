from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Assignment API is running successfully"}

@app.route('/api/hello')
def hello():
    return {"status": "success", "message": "Hello from Azumah4U"}

@app.route('/api/info')
def info():
    return {
        "name": "Assignment-api",
        "owner": "Azumah4U",
        "version": "1.0"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)