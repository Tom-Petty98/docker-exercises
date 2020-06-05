from flask import Flask, render_template, redirect, url_for, request
import requests

app = Flask(__name__)

api = 'http://http_docker_challange_api-service_1:5001'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home")

@app.route('/request', methods=['GET', 'POST'])
def request():
    animal = requests.get(api + '/get/text')
    noise = requests.post(api + '/post/json', json={'Tiger': 'Gggrrroooowwwlll', 'Dog': 'Woof', 'Cat': 'Meow'})
    return render_template("req_page.html", response=animal.text, response2=noise.json()["data"][animal.text], title="Your animal")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# noise = requests.post(api + '/post/text', data=animal.text)