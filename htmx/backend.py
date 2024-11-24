from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "The purpose of our lives is to be happy.",
    "Get busy living or get busy dying.",
    "You have within you right now, everything you need to deal with whatever the world can throw at you."
]

@app.route('/quote')
def get_quote():
    return random.choice(quotes)

if __name__ == '__main__':
    app.run(debug=True)
