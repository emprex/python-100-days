Python 100 Days Challenge
Welcome to my journey through the Python 100 Days challenge! This repository documents my daily progress as I learn Python from the ground up, practice algorithms, and build a professional coding portfolio using best practices in Python, Unix, and GitHub.

📁 Project Structure
text
python-100-days/
│
├── day1/                # Day 1 exercises and mini-projects
├── day2/                # Day 2 exercises and mini-projects
├── .gitignore           # Excludes venv and other files from version control
├── requirements.txt     # Python dependencies for this project
└── README.md            # This file
🚦 Progress Overview
Day	Topics & Projects	Folder/File(s)
Day 1	Python setup, variables, input/output, basic scripts	day1/
- Python basics (day1_basics.py)	
- Greeter mini-project (day1_greeter.py)	
Day 2	Control flow, functions, error handling, mini-project	day2/
- Age checker (day2_age_checker.py)	
- Sum of numbers (day2_sum_of_numbers.py)	
- Multiplication function (day2_multiply.py)	
- Number Guessing Game (day2_guessing_game.py)	
📝 How to Run the Code
Clone the repository:

bash
git clone https://github.com/yourusername/python-100-days.git
cd python-100-days
Create and activate a virtual environment:

bash
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
pip install -r requirements.txt
Navigate to a day's folder and run a script:

bash
cd day2
python3 day2_guessing_game.py
📦 Managing Your Python Environment
The venv/ or .venv/ folder is not tracked by Git (see .gitignore).

All dependencies are listed in requirements.txt.

To update dependencies after installing new packages, run:

bash
pip freeze > requirements.txt
🗂️ Folder Details
day1/
day1_basics.py: Practice with variables, input/output, and basic Python syntax.

day1_greeter.py: A simple greeter mini-project.

day2/
day2_age_checker.py: Checks if a user is a minor, just turned 18, or an adult, with input validation.

day2_sum_of_numbers.py: Sums numbers from 1 to 10 using a loop.

day2_multiply.py: Multiplies two numbers with error handling for invalid input.

day2_guessing_game.py: Mini-project—interactive number guessing game with input validation and attempt counter.

💡 What I’m Learning
Python syntax, functions, and control flow

Error handling and user input validation

Writing reusable, well-structured code

Using Git and GitHub for version control

Organizing code into logical folders by day/project

Documenting progress and building a public coding portfolio

🌟 How to Contribute or Follow
Explore the code in each day's folder.

Suggest improvements or new challenges via issues or pull requests.

Follow my progress and see how my skills grow each day!