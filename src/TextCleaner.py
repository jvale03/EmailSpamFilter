import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from langdetect.lang_detect_exception import LangDetectException
from langdetect import detect

# tecnica para transformar palavras em sua forma base
lemmatizer = WordNetLemmatizer()
def word_lemmatizer(words):
   lemma_words = [lemmatizer.lemmatize(o) for o in words.split(" ")]
   return " ".join(lemma_words)

# obter as stop words em inglês e português
stopwords_english = stopwords.words('english')
stopwords_portuguese = stopwords.words('portuguese')

# pontuação
punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''

# converter o texto para minúsculas
def convert_lower_case(text):
    return text.lower()

# remover dígitos e pontuação
def remove_digits_punctuation(text):
    return "".join([i for i in text if not (i.isdigit() or i in punc)])

# remover as stop words
def remove_stopwords(text, language):
    if language == "en":
        return " ".join([i for i in text.split() if i not in stopwords_english])
    elif language == "pt":
        return " ".join([i for i in text.split() if i not in stopwords_portuguese])
    else:
        return text

# detectar o idioma do texto para remover as stop words corretas
def detect_language(text):
    try:
        # Detecta o idioma do texto
        language = detect(text)
        return language
    except LangDetectException:
        return "Language not detected"
    
# remover URLs
def remove_url(text):
    return re.sub(r"https?://\S+|www\.\S+", "", text)

def clean_text(text):
    text = convert_lower_case(text)
    language = detect_language(text)
    text = remove_url(text)
    text = remove_digits_punctuation(text)
    text = remove_stopwords(text, language)
    text = word_lemmatizer(text)
    return text


if __name__=="__main__":
    text = "I am a studier at the University of Minho. I likes to playing football and watch movies. https://www.geeksforgeeks.org/remove-urls-from-string-in-python/"
    print(clean_text(text))
    