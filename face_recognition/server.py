"""
Simple Flask server for Datalake 3.0 - displays logs from browser to terminal
"""

from flask import Flask, request, send_from_directory, jsonify
from datetime import datetime
import os

app = Flask(__name__, static_folder='.', static_url_path='')

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    INFO = '\033[94m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

@app.route('/')
def index():
    """Serve index.html"""
    return send_from_directory('.', 'index.html')
    

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

@app.route('/face_recognition/<path:filename>')
def serve_face_recognition(filename):
    return send_from_directory('.', filename)

@app.route('/face_recognition/')
def serve_face_recognition_index():
    return send_from_directory('.', 'index.html')

@app.route('/api/log', methods=['POST'])
def receive_log():
    """Receive logs from browser and print to terminal"""
    data = request.json
    
    if not data or 'message' not in data:
        return jsonify({'status': 'error', 'message': 'No message provided'}), 400
    
    message = data.get('message', '')
    level = data.get('level', 'INFO').upper()
    
    # Determine color based on log level
    if 'SUCCESS' in message or '✅' in message:
        color = Colors.SUCCESS
    elif 'FAILED' in message or 'ERROR' in message or '❌' in message:
        color = Colors.ERROR
    elif 'WARNING' in message or 'WARN' in message:
        color = Colors.WARNING
    else:
        color = Colors.INFO
    
    # Format and print
    timestamp = datetime.now().strftime('%H:%M:%S')
    formatted_log = f"{color}[{timestamp}] {message}{Colors.RESET}"
    print(formatted_log)
    
    return jsonify({'status': 'ok'}), 200

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'message': 'Datalake 3.0 server running'}), 200

if __name__ == '__main__':
    print(f"\n{Colors.BOLD}{Colors.HEADER}🚀 Datalake 3.0 Server Starting...{Colors.RESET}")
    print(f"{Colors.INFO}📍 Open: http://localhost:5000/index.html{Colors.RESET}")
    print(f"{Colors.INFO}📍 Or:   http://localhost:5000/highway.html{Colors.RESET}")
    print(f"{Colors.SUCCESS}✅ Logs will appear below:{Colors.RESET}\n")
    
    app.run(debug=False, host='localhost', port=5000)
