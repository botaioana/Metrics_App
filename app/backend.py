from flask import Flask, jsonify, render_template
import random
import time

app = Flask(__name__)

# Simulăm metrici pentru securitate și performanță
def get_metrics():
    return {
        "attack_prevented": random.randint(0, 10),
        "vulnerabilities_found": random.randint(0, 5),
        "response_time": round(random.uniform(0.1, 1.5), 2),  # timpi de răspuns
        "cpu_usage": round(random.uniform(20, 80), 2),  # CPU usage
        "memory_usage": round(random.uniform(30, 90), 2),  # Memory usage
    }

@app.route('/')
def home():
    # Răspunde cu pagina principală (dashboard-ul)
    return render_template('frontend.html')

@app.route('/api/metrics', methods=['GET'])
def metrics():
    # Returnează metricile ca JSON
    metrics = get_metrics()
    return jsonify(metrics)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)  # ← Accessible from outside
