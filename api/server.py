from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route('/')
def home():
    return render_template('index.html')  # Serve frontend

@app.route('/stats')
def get_stats():
    # Dummy data for Vercel
    return jsonify({
        "cpu_usage": 10.5,
        "memory_usage": 55.3,
        "disk_usage": 30.2,
        "upload_speed": 10,
        "download_speed": 50
    })

if __name__ == "__main__":
    app.run()