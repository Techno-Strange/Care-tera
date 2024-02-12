from flask import Flask, render_template, request, session, flash
import requests

app = Flask(__name__)
app.secret_key = ''

api_key = '' 
api_url = ''  

@app.route('/', methods=['GET', 'POST'])
def care():
    if request.method == 'POST':
        session['child_name'] = request.form['child_name']
        session['child_class'] = request.form['child_class']
        session['child_age'] = request.form['child_age']
        prompt = request.form['user_input']
        session['prompt'] = prompt

        flash(f"Welcome {session.get('child_name')}!")

    else:
        prompt = session.get('prompt', "Hello, how can I help you today?")

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }

    data = {
        'messages': [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': f"Child's Name: {session.get('child_name')}, Class: {session.get('child_class')}, Age: {session.get('child_age')}, Prompt: {prompt}"}
        ]
    }

    response = requests.post(api_url, headers=headers, json=data)
    reply = response.json()['choices'][0]['message']['content']

    return render_template('care.html', reply=reply)

if __name__ == "__main__":
    app.run(debug=True)



