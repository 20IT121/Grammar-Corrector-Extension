import openai
import backoff

# @backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def correct_grammar(text):
    # openai.api_key = "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"
    
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo-0301",
    #     messages=[{"role": "user", "content": "Correct the grammar of following sentence: '{text}'\n"}]
    # )


    openai.api_key = "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"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Correct the grammar of following sentence: '{text}'\n",
        n=1,
        max_tokens=50
    )

    corrected_text = response.choices[0].text.strip()
    return corrected_text

# Example usage
input_text = "He were an good boy."
output_text = correct_grammar(input_text)
print(f"Original: {input_text}")
print(f"Corrected: {output_text}")
