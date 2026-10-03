#### Challenge:

Ahoy, officer

your task is to pass a test that is part of the crew drill. Because of your rank of third officer, you must lead the crew by example and pass the test without a single mistake.

May you have fair winds and following seas!

The quiz webpage is available at <a href="http://quiz.cns-jv.tcc" target="_blank">http:&#47;&#47;quiz.cns-jv.tcc</a>.

---

#### Solution:

The title "Alpha–Zulu" is a nod to the NATO phonetic alphabet (Alpha, Bravo, …, Zulu), and the challenge is a crew-drill quiz: `http://quiz.cns-jv.tcc` serves one multiple-choice question at a time and demands a perfect run — a single wrong answer and I have to start over. The web page is an HTML form: each question carries a hidden `question_id`, a `csrf_token`, and four radio options rendered as `label`s (`answer-0` … `answer-3`). The run is too long and the answers too fiddly to click through by hand without ever slipping, so the sensible move is to script the request/answer loop and let it talk to the quiz endpoint directly.

> Note: the quiz host `quiz.cns-jv.tcc` is part of the retired The Catch 2023 infrastructure and is offline now, so I can only reason about the approach from the solver script rather than re-run it live.

I solved it in two phases with a Python script (`az_quiz.py`, using `requests` + `BeautifulSoup`).

**Phase 1 — learn the correct answers.** The quiz reuses a fixed pool of questions, and the key observation is that the correct answer is always present among the four options while the distractors are drawn at random. So if I poll the quiz many times and tally, per `question_id`, how often each answer *text* appears, the correct answer is simply the one that shows up most often. I hammer the front page ~200 times and build a `{question_id: {answer_text: count}}` map:

```python
import requests, operator
from bs4 import BeautifulSoup

ses = requests.session()
questions = {}

for _ in range(200):
    soup = BeautifulSoup(ses.get('http://quiz.cns-jv.tcc/').text, 'lxml')
    qid = soup.find('input', {'id': 'question_id'})['value']
    questions.setdefault(qid, {})
    for n in range(4):                      # answer-0 .. answer-3
        lbl = soup.find('label', {'for': f'answer-{n}'})
        if lbl:
            text = lbl.text
            questions[qid][text] = questions[qid].get(text, 0) + 1
```

**Phase 2 — run the drill without a mistake.** With the answer map built, I open a fresh session and walk the quiz, each time reading the current `question_id` and `csrf_token` out of the page and POSTing the most-frequently-seen (i.e. correct) answer back to `/answer`. Looping through all the questions this way produces a flawless run, and the final response contains the flag:

```python
ses = requests.session()
r = ses.get('http://quiz.cns-jv.tcc/')

for _ in range(20):
    soup = BeautifulSoup(r.text, 'lxml')
    qid  = soup.find('input', {'id': 'question_id'})['value']
    csrf = soup.find('input', {'id': 'csrf_token'})['value']
    best = max(questions[qid].items(), key=operator.itemgetter(1))[0]
    data = {'question_id': qid, 'answer': best,
            'submit': 'Submit', 'csrf_token': csrf}
    r = ses.post('http://quiz.cns-jv.tcc/answer', data=data)
    print(r.text)
```

The final page returned by the loop carries the flag:

```
FLAG{....-....-....-....}
```

---

<details><summary>FLAG:</summary>

```
FLAG{QOn7-MdEo-9cuH-aP6X}
```

</details>
<br/>
