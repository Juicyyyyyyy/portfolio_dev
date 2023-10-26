import openai
from multiprocessing import Pool
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, Blueprint, render_template
from .functions import callGpt

openai_tool_routes = Blueprint('prompt_tester', __name__)

# Load environment variables from .env
load_dotenv()

@openai_tool_routes.route('/prompt_tester', methods=['GET', 'POST'])
def process_prompt():
    if request.method == 'POST':
        try:
            # Get the prompt from the request
            prompt = request.form['prompt']

            # Get the number of tests (how many times to test the same prompt)
            num_tests = int(request.form['numTests'])

            # Process the prompt multiple times and store the results
            results = []
            for _ in range(num_tests):
                result = callGpt(prompt)
                results.append(result)

            return render_template('prompt_tester.html', results=results)
        except Exception as e:
            return jsonify({"error": str(e)})

    return render_template('prompt_tester.html')
