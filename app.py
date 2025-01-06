from flask import Flask, render_template, request, session

app = Flask(__name__)  # Create a Flask application

# Secret key for session management (for security)
import os
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

# List of questions, choices, and correct answers
questions = [
    {"question": "What is the capital of France?", "choices": ["Paris", "London", "Berlin", "Rome"], "correct": "Paris"},
    {"question": "What is 2 + 2?", "choices": ["3", "4", "5", "6"], "correct": "4"},
    {"question": "What is the color of the sky?", "choices": ["Blue", "Green", "Red", "Yellow"], "correct": "Blue"},
    # Add more questions here as needed
]

@app.route("/")  # Define the route for the homepage
def home():
    return render_template("home.html")  # Render the HTML file for the homepage

@app.route("/quiz", methods=["GET", "POST"])  # Allow both GET and POST methods for quiz page
def quiz():
    # Reset the session for a new quiz if not already initialized (after restarting)
    if request.method == "GET":
        session.pop('current_question', None)
        session.pop('score', None)

    # Initialize the game state if not already in session
    if 'current_question' not in session:
        session['current_question'] = 0
        session['score'] = 0

    current_question = session['current_question']
    score = session['score']

    # Get the current question
    if current_question >= len(questions):
        # If we exceed the number of questions, show the results page
        return render_template("results.html", score=session['score'], total=len(questions))

    question = questions[current_question]

    if request.method == "POST":
        # Get the selected answer from the form
        answer = request.form.get("answer")

        # Check if the answer is correct
        if answer == question["correct"]:
            session['score'] += 1  # Increase score if the answer is correct

        # Move to the next question
        session['current_question'] += 1

        # If there are no more questions, show the results
        if session['current_question'] >= len(questions):
            return render_template("results.html", score=session['score'], total=len(questions))

    # If there are still more questions, render the quiz page
    if session['current_question'] < len(questions):
        question = questions[session['current_question']]  # Get the next question
        return render_template("quiz.html", question=question["question"], choices=question["choices"])

    return "Error: No more questions available."

@app.route("/restart")
def restart():
    # Reset the session to restart the game
    session.pop('current_question', None)
    session.pop('score', None)
    return render_template("home.html")  # Redirect to the home page after restarting

if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode for development
