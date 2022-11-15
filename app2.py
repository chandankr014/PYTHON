import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
##IRIS DATA PREDICTION APP
IT PREDICTS **IRIS-FLOWER** TYPE
""")

st.header("User Input Parameters")

def user_input_feature():
    sl = st.sidebar.slider('sepal-length', 4.3,7.9,5.4)
    sw = st.sidebar.slider('sepal-width', 2.0,4.4,3.4)
    pl = st.sidebar.slider('petal-length', 1.0,6.9,1.3)
    pw = st.sidebar.slider('petal-width', 0.1,2.5,0.2)
    data = {
        'sepal-length':sl,
        'sepal-width':sw,
        'petal-length':pl,
        'petal-width':pw
    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_feature()

st.subheader('user input parameters')
st.write(df)

iris = datasets.load_iris()
x = iris.data
y = iris.target

algo = RandomForestClassifier()
algo.fit(x,y)

pred = algo.predict(df)
pred_prob = algo.predict_proba(df)

st.subheader('class label and their corresponding index number')
st.write(iris.target_names)

st.subheader('predictions')
st.write(iris.target_names[pred])

st.subheader('prediction probability')
st.write(pred_prob)



