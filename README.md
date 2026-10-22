<div align="center">

# 🧠 Overthinker's Assistant

**Type a decision. Get pros, cons, sarcasm and a flowchart, so you can overthink it properly.**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-web%20app-000000?style=flat-square&logo=flask&logoColor=white)
![Graphviz](https://img.shields.io/badge/Graphviz-decision%20tree-1F77B4?style=flat-square)
![Markov](https://img.shields.io/badge/markovify-text%20generation-8A2BE2?style=flat-square)

</div>

---

## ✨ What it does

Enter something like `coffee or tea` and the app:

- 🔀 **Splits it into options** and writes pros, cons and a few sarcastic remarks for each
- 🎛️ **Paralysis mode:** 100 reasons per option instead of 10, for maximum overthinking
- 🔗 **Markov mode:** generates the reasons with a Markov chain (`markovify`) instead of fixed templates
- 🌳 **Draws a decision tree** with Graphviz: your question, each option, and the top three pros (green) and cons (red)
- 🕘 **Remembers your past decisions** and shows the latest five

Reasons are intentionally unhelpful and funny ("Some say coffee is how your villain arc begins."). The app never makes the decision for you.

---

## 🚀 Quick start

Install [Graphviz](https://graphviz.org/download/) first (the system tool, not just the Python package), then:

```bash
git clone https://github.com/aryankhanna1409/overthinkers-assistant.git
cd "overthinkers-assistant/Overthinker's Assistant"

pip install -r requirements.txt
python app.py
```

Open the address Flask prints (normally http://127.0.0.1:5000).

---

## 📁 Project layout

| File | Role |
|---|---|
| `app.py` | Flask routes, form handling and decision history |
| `engine.py` | Option extraction plus template and Markov reason generators |
| `flowchart_generator.py` | Builds the decision tree image with Graphviz |
| `templates/index.html` | The web page |
| `static/` | Generated decision-tree image |

Decision history (`history.json`) and the list of already-used reasons (`used_reasons.json`) are created automatically the first time you run the app.

---

<div align="center">

Built for people who think about thinking

</div>
