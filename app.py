from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Load mock data
with open('schemes.json', 'r') as file:
    schemes = json.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').lower()
    response = search_scheme(user_message)
    return jsonify({"response": response})

def search_scheme(query):
    matching_schemes = []

    # Loop through all the schemes
    for scheme in schemes:
        # Check if the query is found in either the name or description of the scheme
        if query in scheme["name"].lower() or query in scheme["description"].lower():
            matching_schemes.append(
                f"<b>Scheme Name:</b> {scheme['name']}<br>"
                f"<b>Description:</b> {scheme['description']}<br>"
                f"<b>Eligibility:</b> {scheme['eligibility']}<br>"
                f"<b>Income Criteria:</b> {scheme['income_criteria']}<br>"
                f"<b>State Criteria:</b> {scheme['state_criteria']}<br>"
                f"<b>Age Criteria:</b> {scheme['age_criteria']}<br>"
                f"<b>More Info:</b> <a href='{scheme['url']}' target='_blank'>{scheme['url']}</a><br><br>"
            )

    # If there are matching schemes, return them, otherwise show no results
    if matching_schemes:
        return "<hr>".join(matching_schemes)
    return "Sorry, no schemes matched your query. Please try again with different keywords."

if __name__ == '__main__':
    app.run(debug=True)
