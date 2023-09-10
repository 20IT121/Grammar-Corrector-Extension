from flask import Flask, render_template, request, jsonify
import openai

openai.api_key=""

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-text', methods=['POST'])
def process_input():
    try:
        user_input = request.form['user_input']
        return jsonify({'result': user_input})

    except Exception as e:
        return jsonify({'error' : str(e)})
    
if __name__ == '__main__':
    app.run(debug=True)