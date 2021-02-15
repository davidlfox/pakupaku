from flask import Flask, render_template, jsonify, request, make_response
from teller import Teller
from eightball import EightBall
app = Flask(__name__)

STATE = 'state'
QUESTION = 'question'
teller = Teller(["blue", "red", "green", "yellow"], range(8), False)


@app.route("/")
def home():
    resp = make_response(render_template('index.html'))
    resp.set_cookie(STATE, '0')
    return resp


def start_json_response(payload):
    response = jsonify({"message": payload})
    return response


def question(input):
    message = f'ahhh yes, i see--you\'re curious indeed.\nthe great paku-paku shows these colors. choose one:\n{teller.colors}'
    response = start_json_response(message)
    response.set_cookie(STATE, '1')
    response.set_cookie(QUESTION, input)
    return response


def choose_color(input):
    if not teller.colors.__contains__(input):
        message = f'the paku-paku does not recognize your choice...\nthe great paku-paku shows these colors. choose one:\n{teller.colors}'
        response = start_json_response(message)
    else:
        message = f'an interesting choice...{input}\n{input} has {len(input)} letters...'
        message += f'\nthe paku-paku now shows {teller.visible_numbers()}, so choose one...'
        # advance state
        response = start_json_response(message)
        response.set_cookie(STATE, '2')

    return response


def choose_number(input):
    if not teller.visible_numbers().__contains__(int(input)):
        message = f'the paku-paku does not recognize your choice...\nthe great paku-paku shows these numbers. choose one:\n{teller.visible_numbers()}'
        response = start_json_response(message)
    else:
        svc = EightBall(request.cookies.get(QUESTION))
        message = svc.getFortune()
        message += f'. what ELSE do you ask of the almighty paku-paku?'
        # advance state
        response = start_json_response(message)
        response.set_cookie(STATE, '0')
        response.set_cookie(QUESTION, '', expires=0)


    return response


states = {
    0: question,
    1: choose_color,
    2: choose_number,
}


@app.route("/fortune", methods=["POST"])
def fortune():
    state = int(request.cookies.get(STATE))
    form = request.form["input"]
    response = states[state](form)
    return response
