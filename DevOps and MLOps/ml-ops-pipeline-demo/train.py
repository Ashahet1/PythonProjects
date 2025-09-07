import pandas as pd
from sklearn.linear_model import LogisticRegression

import pickle

def train():
    #load data
    data = pd.read_csv('data/sample.csv')
    X = data[['feature1', 'feature2']]
    Y = data['label']
    #Train Data
    model = LogisticRegression()
    model.fit(X, Y)
    # Save trained model
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("✅ Model trained and saved as model.pkl")

if __name__ == "__main__":
    train()