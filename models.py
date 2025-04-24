import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

def train_and_save_model(csv_path):
    df = pd.read_csv(csv_path)
    X = df['email']
    y = df['type']

    model = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english')),
        ('clf', MultinomialNB())
    ])
    
    model.fit(X, y)
    joblib.dump(model, 'model/saved_model.pkl')

def load_model():
    return joblib.load('model/saved_model.pkl')
