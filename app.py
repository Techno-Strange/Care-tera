from flask import Flask, render_template, redirect, url_for, request, session

app=Flask(__name__)
app.secret_key='bf9374gf939bv9'

api_key=''
api_url=''

@app.route('/')
def home():
    if request.method == 'POST':
        prompt = request.form['user_input']
        session['prompt'] = prompt
    else:
        prompt = session.get('prompt', "Hello, how can I help you today?")
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    data = {
        'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'},
                     {'role': 'user', 'content': prompt}]
    }

    response = requests.post(api_url, headers=headers, json=data)
    reply = response.json()['choices'][0]['message']['content']

    return render_template('home.html', reply=reply)



if __name__=="__main__":
	app.run(debug=True)
