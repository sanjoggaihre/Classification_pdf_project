
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import string
import nltk
from nltk.corpus import stopwords
import pickle

nltk.download('stopwords')
vectorizer = CountVectorizer()

def pre_process_df():
    f_df=pd.DataFrame(columns=["Text","Labels"])
    df=pd.read_csv("dataset.csv")
    # print(df)
    f_df["Text"]=df["Text"]
    f_df["Labels"]=df["Labels"]
    # print("fdf is: ")
    # print(f_df)
    return f_df

def input_process(text):
    translator= str.maketrans('','',string.punctuation)
    nopunc= text.translate(translator)
    words=[word for word in nopunc.split() if word.lower() not in stopwords.words("English")]
    # print(f'Inside input_process function {words}')
    return ' '.join(words)

def remove_stop_words(ip):
    final_ip=[]
    for line in ip:
        line=input_process(line)
        final_ip.append(line)
    # print(f'final_ip is {final_ip}')
    return final_ip

def train_model(df):
    input=df['Text']
    output=df["Labels"]
    input=remove_stop_words(input)
    df['Text']=input
    input=vectorizer.fit_transform(input)
    # print (input)
    nb=MultinomialNB()
    nb.fit(input,output)
    return nb



if __name__=='__main__':
    df=pre_process_df()
    print(df)
    model=train_model(df)
    pickle.dump(model,open('classifier.model','wb'))
    pickle.dump(vectorizer,open('vectorizer.pickle','wb'))