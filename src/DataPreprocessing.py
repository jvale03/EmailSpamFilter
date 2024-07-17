import re
import os
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from langdetect.lang_detect_exception import LangDetectException
from langdetect import detect

# obter as stop words em inglês e português
stopwords_english = stopwords.words('english')
stopwords_portuguese = stopwords.words('portuguese')

# pontuação
punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''

# paths para o dataset
spam_path = "../DataSet/spam"
email_path = "../DataSet/email"

# resultado final dos ficheiros processados
processed_files = 0
error_files = 0

# tecnica para transformar palavras em sua forma base
lemmatizer = WordNetLemmatizer()
def word_lemmatizer(words):
   lemma_words = [lemmatizer.lemmatize(o) for o in words.split(" ")]
   return " ".join(lemma_words)

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

# processar informação de um ficheiro
def preprocess_file(file_path):
    global processed_files
    global error_files
    try:
        with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
            text = file.read()
            text = clean_text(text)
        
        with open(file_path, "w", encoding='utf-8', errors='replace') as file:
            file.write(text)

        processed_files += 1

    except FileNotFoundError:
        error_files+=1
        print(f"\033[31mFile not found: {file_path}!\033[m")
    except IOError:
        error_files+=1
        print(f"\033[31mIO error occurred while processing the file: {file_path}!\033[m")
    except Exception as e:
        error_files+=1
        print(f"\033[31mAn unexpected error occurred: {e}\033[m")
    

# processar individualmente cada ficheiro de uma diretoria
def preprocess_directory(dataset_path):
    for file_path in os.listdir(dataset_path):
        file = os.path.join(dataset_path,file_path)
        if os.path.isfile(file):
            preprocess_file(file)

# processar cada diretoria 
def preprocess_dataset():
    print("\033[32mProcessing DataSet...\033[m")
    preprocess_directory(spam_path)
    preprocess_directory(email_path)
    print(f"\033[32m{processed_files} files processed!\033[m")
    if error_files!=0:
        print(f"\033[31m{error_files} files not processed!\033[m")


if __name__=="__main__":
    text = "I am a studier at the University of Minho. I likes to playing football and watch movies. https://www.geeksforgeeks.org/remove-urls-from-string-in-python/"
    print(clean_text(text))
    preprocess_dataset()
    