from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/preset', methods=['GET'])
def preset():
    q = request.args.get('preset')
    if not q:
        return jsonify({"error": "Missing required query parameter 'q'"}), 400

    print(f"Received preset: {q}")
    return jsonify({"status": "received", "preset": q})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

