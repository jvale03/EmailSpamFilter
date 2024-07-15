import os
from TextCleaner import clean_text

spam_path = "../DataSet/spam"
email_path = "../DataSet/email"

processed_files = 0
error_files = 0

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
    

def preprocess_dataset(dataset_path):
    for file_path in os.listdir(dataset_path):
        file = os.path.join(dataset_path,file_path)
        if os.path.isfile(file):
            preprocess_file(file)

    
if __name__=="__main__":
    preprocess_dataset(spam_path)
    preprocess_dataset(email_path)
    #preprocess_file("../DataSet/email/00001.1a31cc283af0060967a233d26548a6ce")
    print(f"\033[32m{processed_files} files processed!\033[m")
    print(f"\033[31m{error_files} files not processed!\033[m")