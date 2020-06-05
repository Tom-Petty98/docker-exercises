from flask import Flask, request, jsonify, Response
import random

app = Flask(__name__)

@app.route('/get/text', methods=['GET'])
def get_text():
    list = ['Tiger', 'Dog', 'Cat']
    animal = list[random.randrange(3)]
    return Response(animal, mimetype='text/plain')

@app.route('/post/json', methods=['POST'])
def post_json():
    return jsonify({"data": request.get_json()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)



# a different method
@app.route('/post/text', methods=['POST'])
def animal_noise():
    animal = request.data.decode("UTF-8")
    if animal == "Tiger":
        noise = 'Gggrrroooowwwlll'
    elif animal == 'Dog':
        'Woof'
    elif animal == 'Cat':
        'Meow'
    else:
        noise = "Unsupported animal type"
    return Response(noise, mimetype='text/plain')