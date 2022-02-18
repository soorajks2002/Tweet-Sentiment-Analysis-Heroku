from django.shortcuts import render
import pickle
import re

import nltk

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

def home_page(request):
    return render(request, 'index.html')


def model_prediction(x_pred):
    filename = 'trained_model'

    model = pickle.load(open(filename, 'rb'))

    pred = model.predict(x_pred)

    return pred


def tweet_vectorizer(twt):
    filename = 'tweet_vectorizer'

    vectorizer = pickle.load(open(filename, 'rb'))

    vect_t = vectorizer.transform([twt])

    return vect_t


def result_page(request):

    if request.method == 'POST':

        in_tweet = request.POST.get('email')

        if in_tweet == 'Sooraj' or in_tweet == 'sooraj' :
            context = {
                'your_tweet': in_tweet,
                'sent_tweet': "Creator"
            }

        else:
            words = re.sub('[^a-z A-Z]', ' ', in_tweet)
            words = words.lower()
            words = words.split()

            words = [WordNetLemmatizer().lemmatize(word)
                     for word in words if not word in set(stopwords.words('english'))]

            tweet = ' '.join(words)

            x = tweet_vectorizer(tweet)

            prediction = model_prediction(x)

            if prediction == 1:
                sentiment = "Positive"

            else:
                sentiment = "Negative"

            context = {
                'your_tweet': in_tweet,
                'sent_tweet': sentiment
            }

        return render(request, 'result.html', context=context)
