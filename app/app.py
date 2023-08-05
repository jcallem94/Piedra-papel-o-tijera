from flask import Flask, render_template, request
from werkzeug.exceptions import BadRequestKeyError
import random

app = Flask(__name__)
user_score = 0
computer_score = 0

def get_computer_choice():
  """Gets the computer's choice of rock, paper, or scissors."""
  computer_choice = random.choice(["rock", "paper", "scissors"])
  return computer_choice

def compare_choices(user_choice, computer_choice):
  """Compares the user's and computer's choices and returns the winner."""
  if user_choice == computer_choice:
    return "Tie!"
  elif user_choice == "rock" and computer_choice == "scissors":
    return "User wins!"
  elif user_choice == "paper" and computer_choice == "rock":
    return "User wins!"
  elif user_choice == "scissors" and computer_choice == "paper":
    return "User wins!"
  else:
    return "Computer wins!"

@app.route("/")
def index():
  """The main page of the application."""
  return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
  """The page where the user can play the game."""
  global user_score, computer_score
  if request.method == "POST":
    try:
      user_choice = request.form["user_choice"]
    except BadRequestKeyError:
      return render_template("results.html", user_choice="Please select an image", computer_choice="", winner="", user_score=user_score, computer_score=computer_score)
    computer_choice = random.choice(["rock", "paper", "scissors"])
    winner = compare_choices(user_choice, computer_choice)
    if winner == "User wins!":
      user_score += 1
    elif winner == "Computer wins!":
      computer_score += 1
    return render_template("results.html", user_choice=user_choice, computer_choice=computer_choice, winner=winner, user_score=user_score, computer_score=computer_score)
  else:
    return render_template("index.html")

if __name__ == "__main__":
  app.run(debug=True)