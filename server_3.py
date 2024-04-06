from langchain_openai import OpenAI

from flask import Flask, request, jsonify
import os

os.environ["openai_api_key"] = "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"

PROMPT_STRING = """
INSTRUCT: I am a large language model trained on a massive dataset of text and code. I can provide summaries of factual information about various skin diseases, but I cannot diagnose or give medical advice.

HOW TO USE: Ask me a question about a skin disease, and I will try my best to answer it based on reliable sources.

IMPORTANT: If you have any concerns about your skin health, please consult a qualified healthcare professional for diagnosis and treatment.

DISCLAIMER: I cannot provide medical advice, make claims of cures, or recommend specific treatments.

EXAMPLE: {},

RESPONSE FORMAT: I will deliver the information in a clear, well-structured, and easy-to-understand manner, using a neutral and objective tone. I will focus on factual accuracy and avoid making claims that could be misconstrued as medical advice.
"""

# Start ngrok tunnel to expose localhost:3000


# Stop ngrok tunnel

app = Flask(__name__)
llm = OpenAI(temperature=0.6, openai_api_key=os.environ["openai_api_key"])

@app.route("/", methods=["POST"])
def process_query():
    data = request.json
    query = data.get("query", "")
    prompt = PROMPT_STRING.format(query)
    response = llm.predict(prompt)
    return jsonify({"response": response})

if __name__ == "__main__":

    app.run(port=3000)
