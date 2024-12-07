import pandas as pd
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import warnings

warnings.filterwarnings("ignore")

# Ma'lumotlarni yuklash va tayyorlash
df = pd.read_csv("spam.csv")
df["Spam"] = df["Category"].apply(lambda x: 1 if x == "spam" else 0)

# Mashg'ulot va test to'plamini ajratish
X_train, X_test, y_train, y_test = train_test_split(df.Message, df.Spam, test_size=0.25)

# Modelni baholash funksiyasi
def evaluate_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    roc_auc_train = roc_auc_score(y_train, y_pred_train)
    roc_auc_test = roc_auc_score(y_test, y_pred_test)
    cr_train = classification_report(y_train, y_pred_train, output_dict=True)
    cr_test = classification_report(y_test, y_pred_test, output_dict=True)
    precision_train = cr_train["weighted avg"]["precision"]
    precision_test = cr_test["weighted avg"]["precision"]
    recall_train = cr_train["weighted avg"]["recall"]
    recall_test = cr_test["weighted avg"]["recall"]
    acc_train = accuracy_score(y_true=y_train, y_pred=y_pred_train)
    acc_test = accuracy_score(y_true=y_test, y_pred=y_pred_test)
    F1_train = cr_train["weighted avg"]["f1-score"]
    F1_test = cr_test["weighted avg"]["f1-score"]
    model_score = [
        precision_train, precision_test, recall_train, recall_test,
        acc_train, acc_test, roc_auc_train, roc_auc_test, F1_train, F1_test,
    ]
    return model_score

# Model yaratish
clf = Pipeline([("vectorizer", CountVectorizer()), ("nb", MultinomialNB())])

# Model bahosi
MultinomialNB_score = evaluate_model(clf, X_train, X_test, y_train, y_test)

# Spamni aniqlash funksiyasi
def detect_spam(email_text):
    prediction = clf.predict([email_text])
    if prediction == 0:
        return "This is a Ham Email!"
    else:
        return "This is a Spam Email!"

# Sinov e-mail matnlar
sample_email = "Congratulations! You have WON a $1000 Gift Card!"
result = detect_spam(sample_email)
print(result)

sample_email = "My name is Tulganoy"
result = detect_spam(sample_email)
print(result)
