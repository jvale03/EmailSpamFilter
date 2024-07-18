# EmailSpamFilter

Machine Learning project that detects if an email is **Spam** with `Naive Bayes` algorithm.

The project is organized into **3 phases**:
- Data Preprocessing
- Feature Extraction
- Algorithm Implementation

Each one will be explained later.

## Run Project

First things first, to use this **Filter** it is necessary to have an `email database` with spam and not spam emails, so I used [**Spam Assassin**](https://spamassassin.apache.org/old/publiccorpus/) data set who provides six thousand examples. You can also get DB using the following commands: 
```
wget https://spamassassin.apache.org/old/publiccorpus/20030228_easy_ham.tar.bz2

wget https://spamassassin.apache.org/old/publiccorpus/20030228_easy_ham_2.tar.bz2

wget https://spamassassin.apache.org/old/publiccorpus/20030228_spam.tar.bz2

wget https://spamassassin.apache.org/old/publiccorpus/20050311_spam_2.tar.bz2

wget https://spamassassin.apache.org/old/publiccorpus/20030228_hard_ham.tar.bz2
```

Said that, is required to organize the DB as follows: 

```
- /EmailSpamFilter
    - /src
        - ...
    - /DataSet
        - /email
            - ...
        - /spam
            - ...
    - /PreProcessedDataSet
        - /email
            - ...
        - /spam
            - ...
    - /Model
        - ...
```

- `/src` -> directory with our code
- `/DataSet` -> directory with all spam and normal emails (with no changes) in `/spam` and `/email` subdirectories
- `/PreProcessedDataSet` -> initially empty directory, that is then filled with all **preprocessed** emails, like `/DataSet`.
- `/Model` -> directory with `Count Vectorizer`, `Tfidf Transformer` and `Naive Bayes` model to use with new emails without having to constantly repeat the training and testing model.

## Phases

### Data Preprocessing

At this stage the text of each email is cleaned, removing **number**, **punctuation**, **white spaces**, **stop words**, etc. Is also used `Word Lemmatization` which converts words to is base form (e.g., studies -> study).

#### Report with Data Preprocessing:

| Class | Precision | Recall | F1-Score | Support |
|--------|-----------|--------|----------|---------|
| Normal      | 0.90      | 1.00   | 0.95     | 834     |
| Spam      | 1.00      | 0.76   | 0.86     | 376     |
| **Total**      | **0.93**      | **0.92**   | **0.92**     | **1210**     |

#### Report without Data Preprocessing

| Class | Precision | Recall | F1-Score | Support |
|--------|-----------|--------|----------|---------|
| Normal      | 0.84      | 0.98   | 0.91     | 834     |
| Spam      | 0.94      | 0.58   | 0.72     | 376     |
| **Total**      | **0.87**      | **0.86**   | **0.85**     | **1210**    |

As we can see, the results with **Text cleaning** are much better!

### Feature Extraction

Feature extraction is the middle layer that converts the words into integers/floats so that our Naive Bayes algorithm can process the data.

- Count Vectorizer -> Keep a dictionary with every **word** and its respective **Id** and this Id will relate to the word count inside the training set.
- Tfidf Vectorizer -> Besides of taking the count of every word, words that often **appears across** multiple files will be **downscaled**. 


### Algorithm Implementation

`Naive Bayes` is a simple, probabilistic machine learning algorithm and using `sklearn` library saves a lot of time. Said that, by dividing the dataset into training and testing data (80% and 20% respectively) it is possible to apply the **feature extraction** algorithms to finally apply **Naive Baye** and predict the results by comparing them with the expected.


### Refs: 
1. Spam Filter Design: [link](https://towardsdatascience.com/email-spam-detection-1-2-b0e06a5c0472)
2. Tfidf Vectorizer: [link](https://medium.com/@cmukesh8688/tf-idf-vectorizer-scikit-learn-dbc0244a911a)
3. Naive Bayes Algorithm: [link](https://scikit-learn.org/stable/modules/naive_bayes.html)


### Model
With some more effort I combined several datasets and obtained a very efficient model that I make available here.

#### Model stats 


| Class | Precision | Recall | F1-Score | Support |
|--------|-----------|--------|----------|---------|
| Normal      | 0.95      | 0.99   | 0.97     | 8661     |
| Spam      | 0.99      | 0.95   | 0.97     | 9238     |
| **Total**      | **0.97**      | **0.97**   | **0.97**     | **17899**     |


To use it, just ignore the **Dataset** steps (options 1 and 2 when running the program) and test your inputs!