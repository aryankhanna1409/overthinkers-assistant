from flask import Flask, render_template, request
from engine import extract_options, generate_pros_cons
import json
import os
from datetime import datetime
from flowchart_generator import build_flowchart

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    context = {}

    if request.method == 'POST':
        user_input = request.form.get('decision')
        paralysis_mode = request.form.get('paralysis') == 'on'
        reason_count = 100 if paralysis_mode else 10
        markov_mode = request.form.get('markov') == 'on'

        options = extract_options(user_input)
        data = []

        for opt in options:
            pros, cons, sarcasm = generate_pros_cons(opt, count=reason_count, use_markov=markov_mode)
            data.append({'option': opt, 'pros': pros, 'cons': cons, 'sarcasm': sarcasm})

        image_path = build_flowchart(user_input, data)
        context['flowchart'] = image_path

        # Save to history.json
        history_entry = {
            "timestamp": datetime.now().isoformat(),
            "input": user_input,
            "paralysis_mode": paralysis_mode,
            "options": [
                {
                    "name": item['option'],
                    "pros": item['pros'],
                    "cons": item['cons'],
                    "sarcasm": item['sarcasm']
                }
                for item in data
            ]
        }

        # Save or create file
        if os.path.exists("history.json"):
            with open("history.json", "r+") as f:
                history = json.load(f)
                history.append(history_entry)
                f.seek(0)
                json.dump(history, f, indent=2)
        else:
            with open("history.json", "w") as f:
                json.dump([history_entry], f, indent=2)

        context['data'] = data
        context['user_input'] = user_input

    # Load past 5 decisions (latest first)
    if os.path.exists("history.json"):
        with open("history.json", "r") as f:
            history = json.load(f)
            context['history'] = history[-5:][::-1]

    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
