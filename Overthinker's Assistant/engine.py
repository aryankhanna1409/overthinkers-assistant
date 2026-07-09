import random
import json
import os
import markovify

used_reasons_store = "used_reasons.json"

# Load previously used reasons (to avoid session repeats)
def load_used():
    if os.path.exists(used_reasons_store):
        with open(used_reasons_store, "r") as f:
            return json.load(f)
    return {"pros": [], "cons": []}

# Save updated reason history
def save_used(used):
    with open(used_reasons_store, "w") as f:
        json.dump(used, f, indent=2)

# Templates
pro_templates = [
    "{option} might {verb} your {outcome} in a {adj} way.",
    "{option} sounds like a {adj} decision that could {verb} your {outcome}.",
    "Choosing {option} shows your {adj} brilliance.",
    "Experts say {option} can {verb} {outcome}, maybe.",
    "{option} might actually work... in theory.",
    "A {adj} choice, {option} may {verb} your {outcome}.",
]

con_templates = [
    "{option} could {verb} your {outcome} in the worst possible way.",
    "{option}? It's a trap wrapped in a {adj} package.",
    "{option} might look smart until it starts affecting your {outcome}.",
    "Legend says {option} has led to at least 3 existential crises.",
    "{option} might cause an irreversible {adj} spiral.",
    "Some say {option} is how your villain arc begins.",
]

sarcasm_pool = [
    "Wow, {option}? Revolutionary. Truly groundbreaking.",
    "Sure, {option} worked out *so well* the last time, right?",
    "{option}? Might as well just roll a D20 and pray.",
    "That choice is so {adj}, it belongs in a TED talk titled 'What Not To Do'.",
    "{option} is definitely what Aristotle would've done. Probably.",
    "If common sense had a nemesis, it would be {option}.",
]

def generate_sentence(template, option):
    verbs = ["enhance", "ruin", "complicate", "elevate", "influence", "destabilize", "improve", "transform"]
    adjectives = ["unexpected", "existential", "awkward", "glorious", "regrettable", "strategic", "chaotic", "deep"]
    outcomes = ["life", "career", "day", "sleep", "coffee intake", "mental health", "friendships", "internet history"]

    sentence = template.replace("{option}", option)
    sentence = sentence.replace("{verb}", random.choice(verbs))
    sentence = sentence.replace("{adj}", random.choice(adjectives))
    sentence = sentence.replace("{outcome}", random.choice(outcomes))
    return sentence

def build_markov_model():
    seed_corpus = """
    Choosing {option} might influence your life decisions.
    {option} could backfire in the most poetic way.
    Experts once debated the value of {option}, but they all died confused.
    {option} aligns with cosmic chaos and caffeine addiction.
    Some say {option} causes butterfly effects in parallel timelines.
    Nobody has survived {option} with their sanity intact.
    {option} will haunt your résumé and your dreams.
    Your ancestors scream in six dimensions every time you consider {option}.
    Ancient philosophers agreed on many things. {option} was not one of them.
    {option} is like trying to win chess with a spoon.
    If overthinking were a sport, choosing {option} would be the world record.
    Even your past self is shaking their head at {option}.
    Studies show {option} increases cringe by 37%.
    """
    return markovify.Text(seed_corpus)

def generate_pros_cons(option, count=100, use_markov=False):
    if use_markov:
        model = build_markov_model()
        pros, cons, sarcasm_out = [], [], []
        attempts = 0

        while len(pros) < count and attempts < count * 5:
            s = model.make_sentence()
            if s:
                pros.append(s.replace("{option}", option))
            attempts += 1

        attempts = 0
        while len(cons) < count and attempts < count * 5:
            s = model.make_sentence()
            if s:
                cons.append(s.replace("{option}", option))
            attempts += 1

        attempts = 0
        while len(sarcasm_out) < 3 and attempts < 15:
            s = model.make_sentence()
            if s:
                sarcasm_out.append(s.replace("{option}", option))
            attempts += 1

        return pros, cons, sarcasm_out

    # fallback to template system if not using Markov
    used = load_used()
    pros, cons = [], []

    attempts = 0
    while len(pros) < count and attempts < count * 5:
        sentence = generate_sentence(random.choice(pro_templates), option)
        if sentence not in used["pros"]:
            pros.append(sentence)
            used["pros"].append(sentence)
        attempts += 1

    attempts = 0
    while len(cons) < count and attempts < count * 5:
        sentence = generate_sentence(random.choice(con_templates), option)
        if sentence not in used["cons"]:
            cons.append(sentence)
            used["cons"].append(sentence)
        attempts += 1

    # Save the updated used list
    save_used(used)

    sarcasm_out = [generate_sentence(random.choice(sarcasm_pool), option) for _ in range(3)]

    return pros, cons, sarcasm_out
def extract_options(user_input):
    # Lowercase, strip whitespace, and split on ' or '
    parts = [x.strip() for x in user_input.lower().split(" or ")]
    
    # If no 'or' detected, return whole string as a single option
    return parts if len(parts) > 1 else [user_input.strip()]
