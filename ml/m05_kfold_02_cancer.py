import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score, train_test_split, KFold
from sklearn.preprocessing import MinMaxScaler, StandardScaler #대문자 클래스 약어도 from sklearn.svm import LinearSVC, SVC #리니어 서포트 벡터 
from sklearn.linear_model import Perceptron,LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from tensorflow.python.keras.callbacks import EarlyStopping
from sklearn.metrics import r2_score, accuracy_score
from sklearn.utils import all_estimators
import warnings
warnings.filterwarnings('ignore')
allAlgorithms = all_estimators(type_filter='classifier')
n_splits = 5
kfold = KFold(n_splits=n_splits, random_state=214,shuffle=True)
#1.데이터
data_sets = load_breast_cancer()

x = data_sets['data']
y = data_sets['target']

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=66)

for (name,algorithm) in allAlgorithms:
    try:
        model = algorithm()
        model.fit(x_train, y_train)
        y_predict = model.predict(x_test)
        acc = accuracy_score(y_test, y_predict)
        scores = cross_val_score(model,x_train,y_train,cv=kfold)
        p = round(np.mean(scores),4)
        print(name,'acc',acc,'\n','cross_val 평균',p)
    except:
        print(name,'안나옴')

# print('acc',model.score(x_test,y_test))
