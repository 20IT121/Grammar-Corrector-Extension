document.addEventListener('DOMContentLoaded', function () {
    const userInput = document.getElementById('userInput');
    const generateButton = document.getElementById('generateButton');
    const generatedText = document.getElementById('generatedText');

    generateButton.addEventListener('click', function () {
        const inputText = userInput.value;
        fetch('/generate-text', { 
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams({ 'user_input': inputText }) // sending input json payload
        })
        .then(response => response.json())
        .then((data) => {
            if (data.result) { // we have sent output json object with key 'result'
                generatedText.textContent = data.result; // id Element of output text
            } else {
                generatedText.textContent = 'Error: Unable to generate text.';
            }
        })
        .catch(error => {
            console.log('Error: ' + error.message)
        });
    });
});
