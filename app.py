from flask import Flask, jsonify, render_template
import psutil
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # ← THIS LINE IS CRUCIAL

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/stats')
def get_stats():
    try:
        # CPU
        cpu = psutil.cpu_percent(interval=1)
        
        # Memory
        mem = psutil.virtual_memory().percent
        
        # Disk
        disk = psutil.disk_usage('/').percent
        
        # Network
        net1 = psutil.net_io_counters()
        time.sleep(1)
        net2 = psutil.net_io_counters()
        
        return jsonify({
            "cpu_usage": cpu,
            "memory_usage": mem,
            "disk_usage": disk,
            "upload_speed": (net2.bytes_sent - net1.bytes_sent) / 1048576,  # MB
            "download_speed": (net2.bytes_recv - net1.bytes_recv) / 1048576
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)