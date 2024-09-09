from flask import Flask, request
import threading
import time
import os
import signal
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='/home/alwin/Documents/projects/test_proj/flask/logs/app.log', level=logging.INFO)

@app.route('/')
def hello():
    app.logger.info('Hello endpoint was reached')
    return "Hello, Flask inside Docker!"

@app.route('/shutdown', methods=['POST'])
def shutdown():
    if request.method == 'POST':
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()
        return 'Server shutting down...'
    return 'Invalid request method!'

def stop_server_after_delay():
    time.sleep(30)  # Wait for 30 seconds
    app.logger.info("Stopping the server...")
    os.kill(os.getpid(), signal.SIGINT)  # Send SIGINT to the current process

if __name__ == "__main__":
    # Start a thread to stop the server after a delay
    threading.Thread(target=stop_server_after_delay).start()
    app.run(host='0.0.0.0', port=5000)
