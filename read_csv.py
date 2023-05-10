import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
df = pd.read_csv('D:\pending\crop_predictionweb\src\static\Crop_recommendation.csv')
X = df.drop('label', axis=1)
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=66)

def random_forest(t1,t2,t3,t4,t5,t6,t7):
    rfc = RandomForestClassifier()
    rfc.fit(X_train,y_train)
    lst=[[t1,t2,t3,t4,t5,t6,t7]]
    lst=np.array(lst)
    lst.reshape(-1,1)

    rfc_predict = rfc.predict(lst)
    print(rfc_predict)
    ab = rfc.score(X_test, y_test)
    return str(rfc_predict[0]),ab


