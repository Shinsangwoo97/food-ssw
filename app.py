from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@Cluster0.88k4h.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/food', methods=['POST'])
def food_post():
    name_receive = request.form['name_give']
    url_receive = request.form['url_give']
    choice_receive = request.form['choice_give']
    comment_receive = request.form['comment_give']

    food_list = list(db.food.find({}, {'_id': False}))
    count = len(food_list) + 1

    doc = {
        'num': count,
        'name': name_receive,
        'url': url_receive,
        'choice': choice_receive,
        'comment': comment_receive
    }
    db.food.insert_one(doc)

    return jsonify({'result':'success', 'msg': '등록 완료!'})

@app.route("/food", methods=["GET"])
def food_get():
    food_list = list(db.food.find({}, {'_id': False}))
    return jsonify({'foods': food_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)