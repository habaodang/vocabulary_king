from flask import Flask,render_template,url_for,jsonify
from game import shuffle_word
from data import readData
import random

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/viet_nam')
def viet_nam():
    return render_template('vietnam.html')

@app.route('/getwordvietnam')
def get_word_english():
    data=readData('data/vietnam.txt')
    shuffled_word, original_word = shuffle_word(data[random.randint(0, len(data) - 1)])  # Tạo từ mới
    return jsonify({'ques': shuffled_word, 'answer': original_word})

@app.route('/english')
def english():
    return render_template('english.html')

@app.route('/getwordenglish')
def get_word_vietnam():
    data=readData('data/english.txt')
    shuffled_word, original_word = shuffle_word(data[random.randint(0, len(data) - 1)])  # Tạo từ mới
    return jsonify({'ques': shuffled_word, 'answer': original_word})



if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=80)
