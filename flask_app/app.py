from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Deploying Flask App at Vercel"

# ✅ Fix the favicon error by handling requests for it
@app.route('/favicon.ico')
def favicon():
    return '', 204  # Returns an empty response with status 204 (No Content)

if __name__ == '_main_':
    app.run(debug=True)