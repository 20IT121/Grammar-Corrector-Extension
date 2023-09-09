from flask import Flask, requests, jsonify
import openai

app = Flask(__name__)
openai.api_key = "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"

@app.route('/generate-text', methods=['POST'])
def correct_grammar(text):
    # openai.api_key = "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"
    
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo-0301",
    #     messages=[{"role": "user", "content": "Correct the grammar of following sentence: '{text}'\n"}]
    # )
    try:
        # GET user_input from POST request
        data = requests.get_json()
        user_input = data.get('input', '')

        # Make a request to openAI 
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Correct the grammar of following sentence: '{user_input}'\n",
            n=1,
            max_tokens=50
        )

        # Extracting generated text from response
        corrected_text = response.choices[0].text.strip()

        # Send the generated text as JSON response
        return jsonify({'generated-text' : corrected_text})
    
    except Exception as e:
        return jsonify({'error' : str(e)}) , 500
    

# # Example usage
# input_text = "He were an good boy."
output_text = correct_grammar()
print(f"Original: ")
print(f"Corrected: {output_text}")

if __name__ == '__main__':
    app.run(debug=True)
