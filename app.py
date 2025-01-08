from flask import Flask, render_template, request, session, redirect, url_for
import os
import random

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

questions = [

    # Geography (20 questions)
    {"question": "What is the capital of Australia?", "choices": ["Canberra", "Sydney", "Melbourne", "Brisbane"], "correct": "Canberra"},
    {"question": "What is the longest river in the world?", "choices": ["Amazon", "Nile", "Yangtze", "Mississippi"], "correct": "Nile"},
    {"question": "Which country has the most islands in the world?", "choices": ["Sweden", "Indonesia", "Philippines", "Canada"], "correct": "Sweden"},
    {"question": "Which desert is the largest in the world?", "choices": ["Sahara", "Gobi", "Kalahari", "Antarctic"], "correct": "Antarctic"},
    {"question": "What is the smallest country in the world?", "choices": ["Vatican City", "Monaco", "San Marino", "Liechtenstein"], "correct": "Vatican City"},
    {"question": "Which city is known as the 'Big Apple'?", "choices": ["New York", "Los Angeles", "Chicago", "San Francisco"], "correct": "New York"},
    {"question": "Which continent has the most countries?", "choices": ["Africa", "Asia", "Europe", "South America"], "correct": "Africa"},
    {"question": "What is the name of the sea bordered by Europe to the north and Africa to the south?", "choices": ["Mediterranean Sea", "Red Sea", "Caribbean Sea", "Baltic Sea"], "correct": "Mediterranean Sea"},
    {"question": "What is the highest waterfall in the world?", "choices": ["Angel Falls", "Niagara Falls", "Victoria Falls", "Iguazu Falls"], "correct": "Angel Falls"},
    {"question": "Which U.S. state is the Grand Canyon located in?", "choices": ["Arizona", "Nevada", "Colorado", "Utah"], "correct": "Arizona"},
    {"question": "Which mountain range is Mount Everest a part of?", "choices": ["Himalayas", "Rockies", "Andes", "Alps"], "correct": "Himalayas"},
    {"question": "What is the largest island in the world?", "choices": ["Greenland", "Australia", "New Guinea", "Borneo"], "correct": "Greenland"},
    {"question": "Which U.S. state is known as the 'Sunshine State'?", "choices": ["Florida", "California", "Texas", "Hawaii"], "correct": "Florida"},
    {"question": "What is the capital of Canada?", "choices": ["Ottawa", "Toronto", "Montreal", "Vancouver"], "correct": "Ottawa"},
    {"question": "Which African country has the largest population?", "choices": ["Nigeria", "Ethiopia", "Egypt", "South Africa"], "correct": "Nigeria"},
    {"question": "Which ocean is the largest?", "choices": ["Pacific", "Atlantic", "Indian", "Arctic"], "correct": "Pacific"},
    {"question": "What is the capital of Japan?", "choices": ["Tokyo", "Kyoto", "Osaka", "Nagoya"], "correct": "Tokyo"},
    {"question": "What is the tallest building in the world?", "choices": ["Burj Khalifa", "Shanghai Tower", "Empire State Building", "Willis Tower"], "correct": "Burj Khalifa"},
    {"question": "Which European country is known for its fjords?", "choices": ["Norway", "Sweden", "Iceland", "Finland"], "correct": "Norway"},
    {"question": "Which country is the Great Barrier Reef located in?", "choices": ["Australia", "Indonesia", "Philippines", "Thailand"], "correct": "Australia"},

    # History (20 questions)
    {"question": "Who was the first President of the United States?", "choices": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"], "correct": "George Washington"},
    {"question": "In which year did the Titanic sink?", "choices": ["1912", "1905", "1920", "1898"], "correct": "1912"},
    {"question": "Who discovered America?", "choices": ["Christopher Columbus", "Marco Polo", "Amerigo Vespucci", "Leif Erikson"], "correct": "Christopher Columbus"},
    {"question": "Which war was fought between the North and South regions in the United States?", "choices": ["Civil War", "World War I", "Revolutionary War", "Vietnam War"], "correct": "Civil War"},
    {"question": "Who was the first man to step on the moon?", "choices": ["Neil Armstrong", "Buzz Aldrin", "Michael Collins", "Yuri Gagarin"], "correct": "Neil Armstrong"},
    {"question": "In which year did World War II end?", "choices": ["1945", "1939", "1918", "1950"], "correct": "1945"},
    {"question": "Who was the first emperor of China?", "choices": ["Qin Shi Huang", "Han Wudi", "Emperor Gaozu", "Emperor Taizong"], "correct": "Qin Shi Huang"},
    {"question": "Which empire was ruled by Julius Caesar?", "choices": ["Roman Empire", "Ottoman Empire", "Byzantine Empire", "Mongol Empire"], "correct": "Roman Empire"},
    {"question": "Who was the famous queen of ancient Egypt?", "choices": ["Cleopatra", "Nefertiti", "Hatshepsut", "Maatkare"], "correct": "Cleopatra"},
    {"question": "Which event started World War I?", "choices": ["Assassination of Archduke Franz Ferdinand", "The bombing of Pearl Harbor", "The Treaty of Versailles", "The invasion of Poland"], "correct": "Assassination of Archduke Franz Ferdinand"},
    {"question": "What ancient civilization built the Machu Picchu?", "choices": ["Inca", "Maya", "Aztec", "Olmec"], "correct": "Inca"},
    {"question": "Who was the leader of the Soviet Union during World War II?", "choices": ["Joseph Stalin", "Leon Trotsky", "Vladimir Lenin", "Nikita Khrushchev"], "correct": "Joseph Stalin"},
    {"question": "Which battle is considered the turning point of the American Civil War?", "choices": ["Battle of Gettysburg", "Battle of Antietam", "Battle of Fort Sumter", "Battle of Appomattox"], "correct": "Battle of Gettysburg"},
    {"question": "In which country did the Industrial Revolution begin?", "choices": ["England", "France", "Germany", "United States"], "correct": "England"},
    {"question": "Who was the leader of the French Revolution?", "choices": ["Maximilien Robespierre", "Napoleon Bonaparte", "Louis XVI", "Jean-Paul Marat"], "correct": "Maximilien Robespierre"},
    {"question": "Which was the first country to grant women the right to vote?", "choices": ["New Zealand", "United States", "United Kingdom", "Finland"], "correct": "New Zealand"},
    {"question": "Who wrote the Declaration of Independence?", "choices": ["Thomas Jefferson", "George Washington", "Benjamin Franklin", "John Adams"], "correct": "Thomas Jefferson"},
    {"question": "What ancient civilization built the pyramids of Giza?", "choices": ["Ancient Egyptians", "Romans", "Greeks", "Babylonians"], "correct": "Ancient Egyptians"},
    {"question": "Which event marked the end of the Middle Ages?", "choices": ["Fall of Constantinople", "The Black Death", "The Renaissance", "The Reformation"], "correct": "Fall of Constantinople"},
    {"question": "Who was the first woman to fly solo across the Atlantic Ocean?", "choices": ["Amelia Earhart", "Bessie Coleman", "Jacqueline Cochran", "Sally Ride"], "correct": "Amelia Earhart"},

    # Science (20 questions)
    {"question": "What is the chemical symbol for water?", "choices": ["H2O", "CO2", "O2", "H2"], "correct": "H2O"},
    {"question": "What planet is known as the Red Planet?", "choices": ["Mars", "Venus", "Jupiter", "Saturn"], "correct": "Mars"},
    {"question": "What is the largest organ in the human body?", "choices": ["Skin", "Heart", "Liver", "Brain"], "correct": "Skin"},
    {"question": "What gas do plants absorb from the atmosphere during photosynthesis?", "choices": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "correct": "Carbon Dioxide"},
    {"question": "What element does 'O' represent on the periodic table?", "choices": ["Oxygen", "Osmium", "Oganesson", "Ozone"], "correct": "Oxygen"},
    {"question": "What is the powerhouse of the cell?", "choices": ["Mitochondria", "Nucleus", "Endoplasmic Reticulum", "Ribosome"], "correct": "Mitochondria"},
    {"question": "Which planet is the closest to the Sun?", "choices": ["Mercury", "Venus", "Earth", "Mars"], "correct": "Mercury"},
    {"question": "What is the hardest natural substance on Earth?", "choices": ["Diamond", "Gold", "Iron", "Platinum"], "correct": "Diamond"},
    {"question": "What is the chemical formula for table salt?", "choices": ["NaCl", "KCl", "CaCl2", "MgCl2"], "correct": "NaCl"},
    {"question": "Which scientist developed the theory of general relativity?", "choices": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla"], "correct": "Albert Einstein"},
    {"question": "What is the most common element in the Earth's crust?", "choices": ["Oxygen", "Silicon", "Aluminum", "Iron"], "correct": "Oxygen"},
    {"question": "What is the process by which plants make their food?", "choices": ["Photosynthesis", "Respiration", "Fermentation", "Transpiration"], "correct": "Photosynthesis"},
    {"question": "What is the main ingredient in natural gas?", "choices": ["Methane", "Ethane", "Propane", "Butane"], "correct": "Methane"},
    {"question": "Which part of the brain controls balance and coordination?", "choices": ["Cerebellum", "Cerebrum", "Medulla", "Hypothalamus"], "correct": "Cerebellum"},
    {"question": "How many bones are in the adult human body?", "choices": ["206", "205", "208", "210"], "correct": "206"},
    {"question": "Which element has the atomic number 1?", "choices": ["Hydrogen", "Helium", "Oxygen", "Carbon"], "correct": "Hydrogen"},
    {"question": "What is the largest planet in our solar system?", "choices": ["Jupiter", "Saturn", "Uranus", "Neptune"], "correct": "Jupiter"},
    {"question": "What is the center of an atom called?", "choices": ["Nucleus", "Electron", "Proton", "Neutron"], "correct": "Nucleus"},
    {"question": "Which chemical element has the symbol 'Fe'?", "choices": ["Iron", "Fermium", "Francium", "Fluorine"], "correct": "Iron"},
    {"question": "What is the main source of energy for the Earth?", "choices": ["The Sun", "The Moon", "The Earth’s Core", "Tidal Energy"], "correct": "The Sun"}


]

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