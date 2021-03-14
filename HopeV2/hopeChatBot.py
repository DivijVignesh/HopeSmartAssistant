import random
import json
import pickle
import datetime
import numpy as np
from numpy import array
import nltk
from nltk.stem import WordNetLemmatizer
 
from tensorflow.keras.models import load_model
 
lemmatizer=WordNetLemmatizer()
intents=json.loads(open('intents.json').read())

words= pickle.load(open('words.pkl','rb'))
classes= pickle.load(open('classes.pkl','rb'))
model =load_model('hopeChatbot_model.h5')

def clean_up_sentence(sentence):
    sentence_words =  nltk.word_tokenize(sentence)
    sentence_words =[lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):    
    sentence_words = clean_up_sentence(sentence)
    bag= [0]*len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word==w:
                bag[i]=i
    return np.array(bag)


def predict_class(sentence):
    bow=bag_of_words(sentence)
    res= model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i , r in enumerate(res) if  r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list =[]
    for r in results:
        return_list.append({'intents': classes[r[0]] , 'probabilty': str(r[1])})
    return return_list

def get_response(intents_list,intents_json):
    tag=intents_list[0]['intents']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tags'] == tag:
            result=random.choice(i['responses'])
            if i['tags']== 'time':
                print(datetime.datetime.now().strftime("%H:%M:%S"))
            break
    return result
print(classes)
print("GO! You are on")

def index(query):
    message=query
    ints = predict_class(message)
    res = get_response(ints , intents)
    return ints ,res

# while True:
#     message=input("")
#     ints =predict_class(message)
#     res = get_response(ints,intents)
#     print(res) 