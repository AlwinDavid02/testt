from flask import Flask
import threading
import time
import requests  # To trigger a shutdown request to the Flask server

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Flask inside Docker!"

def shutdown_server():
    # Send a request to the Flask server to trigger the shutdown
    requests.get("http://127.0.0.1:5000/shutdown")

@app.route('/shutdown', methods=['GET'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return "Server shutting down..."

def stop_server_after_delay(delay):
    time.sleep(delay)
    print("Shutting down the server...")
    shutdown_server()

if __name__ == "__main__":
    # Start a timer to shut down the server after 120 seconds (2 minutes)
    threading.Thread(target=stop_server_after_delay, args=(30,)).start()
    app.run(host='0.0.0.0', port=5000)
