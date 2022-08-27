from posixpath import split
import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import string
from sklearn.naive_bayes import MultinomialNB
import pickle

nltk.download('stopwords')
vectorizer= CountVectorizer()

def get_df():
    p_df=pd.DataFrame(columns=['Text','Label'])
    df=pd.read_csv('Dataset.csv')
    p_df['Text']=df['Text']
    p_df['Label']=df['Label']
    #print(p_df)
    return p_df

def input_process(text):
    translator= str.maketrans('','', string.punctuation)
    nopunc= text.translate(translator)
    words=[word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    return ' '.join(words)

def remove_stopwords(input):
    final_input=[]
    for line in input: 
        line=input_process(line)
        final_input.append(line)
    return final_input

def train_model(df):
    input= df['Text']
    output= df['Label']
    input= remove_stopwords(input)
    df['Text']=input
    input= vectorizer.fit_transform(input)
    model=MultinomialNB()
    model.fit(input,output)
    return model

if __name__=='__main__':
    df=get_df()
    model=train_model(df)
    pickle.dump(model,open('NB.model','wb'))
    pickle.dump(vectorizer, open('vectorizer.pickle','wb'))