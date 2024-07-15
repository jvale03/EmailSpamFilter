import os
from TextCleaner import clean_text

spam_path = "../DataSet/spam"
email_path = "../DataSet/email"

number = 0

def preprocess_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            text = clean_text(text)
        
        with open(file_path, "w") as file:
            file.write(text)

        number+=1
    except:
        print(f"\033[31mError at {file_path}!\033[m")
    
def preprocess_dataset(dataset_path):
    number = 0
    for file_path in os.listdir(dataset_path):
        file = os.path.join(dataset_path,file_path)
        if os.path.isfile(file):
            preprocess_file(file)

    
if __name__=="__main__":
    preprocess_dataset(spam_path)
    preprocess_dataset(email_path)
    print(f"\033[32m{number} files processed!\033[m")
