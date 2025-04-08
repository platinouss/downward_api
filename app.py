# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    pod_name = os.getenv('POD_NAME', 'Unknown')
    node_name = os.getenv('NODE_NAME', 'Unknown')
    pod_namespace = os.getenv('POD_NAMESPACE', 'Unknown')

    return {
        "pod_name": pod_name,
        "node_name": node_name,
        "pod_namespace": pod_namespace
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
