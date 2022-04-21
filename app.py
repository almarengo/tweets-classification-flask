from flask import Flask, request, jsonify, render_template
import pickle
from utils.utils import *
import spacy
import os

os.environ['LANGUAGE_MODEL_SPACY'] = "en_core_web_sm"
lemmatizer = spacy.load(os.environ['LANGUAGE_MODEL_SPACY'])

app = Flask('Tweets Sebtiment API')

@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def prediction_sentiment():
    
    #input_json = request.get_json(force=True)
    #print(f'Data sent in request: {input_json}')

    #tweet = input_json['tweet']
    original_tweet = request.form['text1']
    tweet = sentence_cleaning(original_tweet)
    tweet = ' '.join([x.lemma_ for x in lemmatizer(tweet)])
    tweet = [tweet]

    model = pickle.load(open('saved_model/finalized_model.pickle', 'rb'))
    response = model.predict(tweet)

    #return jsonify({'sentiment': response[0]})
    return render_template('form.html', text1=original_tweet, final=response[0])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    #app.run(debug=True)
    