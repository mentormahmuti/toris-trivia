from flask import Flask, render_template, request, session, redirect, url_for
import os
import random
import json

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

# Load questions from JSON file
with open('questions.json') as f:
    questions = json.load(f)

@app.route("/")  # Define the route for the homepage
def home():
    # Shuffle the questions and select 10 random questions
    random.shuffle(questions)
    selected_questions = questions[:10]

    # Shuffle the choices for each question
    for question in selected_questions:
        random.shuffle(question["choices"])

    session['score'] = 0
    session['current_question'] = 0
    session['questions'] = selected_questions
    session['correct_answer'] = None
    return render_template("home.html")  # Render the HTML file for the homepage

@app.route("/quiz", methods=["GET", "POST"])  # Allow both GET and POST methods for quiz page
def quiz():
    if request.method == "POST":
        selected_choice = request.form.get("choice")
        current_question = session.get('current_question')
        questions = session.get('questions')
        correct_answer = questions[current_question]['correct']

        if selected_choice == correct_answer:
            session['score'] += 1
            session['correct_answer'] = None
        else:
            session['correct_answer'] = correct_answer

        session['current_question'] += 1

        if session['current_question'] >= len(questions):
            return redirect(url_for('results'))

    current_question = session.get('current_question')
    questions = session.get('questions')
    question = questions[current_question]

    return render_template("quiz.html", question=question, score=session.get('score'), correct_answer=session.get('correct_answer'))

@app.route("/results")
def results():
    score = session.get('score')
    return render_template("results.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)