from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    ip = socket.gethostbyname(socket.gethostname())
    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <h1>Hello World (GitHub Actions)</h1>"""

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
