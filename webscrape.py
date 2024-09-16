from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask_question():
    # Get data from POST request
    data = request.json
    question = data.get('question')
    url = data.get('url')

    if not question or not url:
        return jsonify({"error": "Please provide both 'question' and 'url' fields."}), 400

    # Scrape the website
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({"error": "Unable to retrieve content from the website."}), 400

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract all paragraphs
    paragraphs = soup.find_all('p')
    content = " ".join([p.get_text() for p in paragraphs])

    # Search for keywords in the content
    question_keywords = question.lower().split()
    if all(keyword in content.lower() for keyword in question_keywords):
        return jsonify({"question": question, "answer": content[:300]})  # Return first 300 characters
    else:
        return jsonify({"question": question, "answer": "No relevant answer found."})

if __name__ == '__main__':
    app.run(debug=True)
