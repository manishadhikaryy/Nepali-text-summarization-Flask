from flask import Flask, request, render_template
import math
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

app = Flask(__name__)

# Your summarization code
def frequency_matrix(sentences):
    freq_matrix = {}
    nep_stopwords = set(stopwords.words("nepali"))
    
    for sentence in sentences:
        freq_table = {}
        words = sentence.split()
        
        for word in words:
          if word not in nep_stopwords:  
            if word in freq_table:
                freq_table[word] += 1
            else:
                freq_table[word] = 1               
                
        freq_matrix[sentence[:8]] = freq_table
    return freq_matrix

def tf_matrix(freq_matrix):
    tf_matrix = {}
    
    for sentence, freq in freq_matrix.items():
        tf_table = {}
        words_sentence = len(freq)

        for word, count in freq.items():
            tf_table[word] = count/words_sentence

        tf_matrix[sentence] = tf_table
    
    return tf_matrix

def documents_per_words(freq_matrix):
    word_per_document_matrix = {}
    
    for sentence, freq in freq_matrix.items():
        for word, count in freq.items():
            word_per_document_matrix[word] = word_per_document_matrix.get(word, 0) + 1
    return word_per_document_matrix

def idf_matrix(freq_matrix, doc_per_words, doc_size):
    idf_matrix = {}
    
    for sentence, freq in freq_matrix.items():
        idf_table = {}
        
        for word in freq.keys():
            idf_table[word] = math.log10(doc_size/float(doc_per_words[word]))
        
        idf_matrix[sentence] = idf_table 

    return idf_matrix

def tf_idf_matrix(tf_matrix, idf_matrix):
    tf_idf_matrix = {}
    
    for (sentence1, freq1), (sentence2, freq2) in zip(tf_matrix.items(), idf_matrix.items()):

        tf_idf_table = {}

        for (word1, count1), (word2, count2) in zip(freq1.items(), freq2.items()):  # here, keys are the same in both the table
            tf_idf_table[word1] = float(count1 * count2)

        tf_idf_matrix[sentence1] = tf_idf_table

    return tf_idf_matrix

def score_sentences(tf_idf_matrix):
    sentence_val = {}
    
    for sentence, freq in tf_idf_matrix.items():
        score_per_sentence = 0 
        
        words_in_sentence = len(freq)
        
        for word, score in freq.items():
            score_per_sentence += score
        
        if words_in_sentence != 0: 
            sentence_val[sentence] = score_per_sentence/words_in_sentence
    
    return sentence_val

def average_score(score_sentences):
    sum_values = 0 
    
    for key, value in score_sentences.items():
        sum_values += value 
    
    return (sum_values/len(score_sentences))

def summary(sentences, score_sentences, average):
    summary = []
    
    for sentence in sentences:
        if sentence[:8] in score_sentences and score_sentences[sentence[:8]] >= average:
            summary.append(sentence)
            
    return summary 

def result_summary(summary):
    result = '|'.join(summary)
    return result

# Route for handling the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling the summarization
@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    text = text.replace('\n', '').replace('\r', '')
    text = text.strip()

    sentences = text.split('।' or '?')

    freq_matrix = frequency_matrix(sentences)
    tf_matrix_data = tf_matrix(freq_matrix)
    doc_per_words = documents_per_words(freq_matrix)
    idf_matrix_data = idf_matrix(freq_matrix, doc_per_words, len(sentences))
    tf_idf_matrix_data = tf_idf_matrix(tf_matrix_data, idf_matrix_data)
    score_sentences_data = score_sentences(tf_idf_matrix_data)
    average = average_score(score_sentences_data)
    summary_data = summary(sentences, score_sentences_data, average)
    result = result_summary(summary_data)
    
    return render_template('result.html', summary=result)

if __name__ == '__main__':
    app.run(debug=True)
