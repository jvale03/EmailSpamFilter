import os
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from joblib import dump, load


# paths para o dataset e model
dataset_path = "../PreProcessedDataSet/"
model_path = "../Model"


def naive_bayes():
    try:
        # carregar dataset
        data = load_files(dataset_path, encoding="utf-8", decode_error="ignore")

        # dividir em treino e teste
        x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

        # vetorizar dados com o countvectorizer e o Tfidf
        count_vect = CountVectorizer()
        x_train_counts = count_vect.fit_transform(x_train)
        x_test_counts = count_vect.transform(x_test)

        tfidf_transformer = TfidfTransformer()
        x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)
        x_test_tfidf = tfidf_transformer.transform(x_test_counts)

        # treinar dados
        data_clf = MultinomialNB()
        data_clf.fit(x_train_tfidf, y_train)


        # prever resultados
        y_pred = data_clf.predict(x_test_tfidf)

        # avaliar precisao
        classification_result = classification_report(y_test, y_pred) 

        return (count_vect,tfidf_transformer,data_clf,classification_result)
    except Exception as e:
        print(f"\033[31mError: {e}\033[m")
    


# guardar modelo para poder usar posteriormente sem ter de o treinar
def save_model(model):
    print("\033[32mSaving model...\033[m")
    try:
        dump(model[0],model_path + '/count_vectorizer.joblib')
        dump(model[1],model_path + '/tfidf_transformer.joblib')
        dump(model[2],model_path + '/naive_bayes_model.joblib')
        dump(model[3],model_path + '/clf_report.joblib')
        print("\033[32mModel saved!\033[m")
    except Exception as e:
        print(f"\033[31mError: {e}\033[m")

# obter report do modelo guardado
def get_report():
    print("\033[32mGetting report...\033[m")
    try:
        clf = load(model_path + '/clf_report.joblib')
        print("Classification Report:")
        print(clf)
    except Exception as e:
        print(f"\033[31mError: {e}")
        print("Try to save a Naive Bayes model first!\033[m")

# carregar modelo para poder usa lo
def load_model():
    print("\033[32mLoading model...\033[m")
    try:
        count_vectorizer = load(model_path + '/count_vectorizer.joblib')
        tfidf_transformer = load(model_path + '/tfidf_transformer.joblib')
        clf = load(model_path + '/naive_bayes_model.joblib')
        print("\033[32mModel loaded!\033[m")
    except Exception as e:
        print(f"\033[31mError: {e}")
        print("Try to save a Naive Bayes model first!\033[m")

    return (count_vectorizer,tfidf_transformer,clf)

# testar input para o modelo guardado
def test_input(text):
    try:
        count_vect, tfidf_trans, clf = load_model()
        x_count_vect = count_vect.transform(text)
        x_tfidf_trans = tfidf_trans.transform(x_count_vect)

        result = clf.predict(x_tfidf_trans)

        return result
    except Exception as e:
        print(f"\033[31mError: {e}\033[m")   

    return None
