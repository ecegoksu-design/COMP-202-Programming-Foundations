import pickle

def read_text(text_path):
    
    text_list = []
    
    try:
        file_object = open(text_path, 'r')
        
        for line in file_object:
            user_separation = line.find(',')
            sentence_index = user_separation + 1
            text_list.append(line[sentence_index:])

        file_object.close()
            
    except FileNotFoundError:
        print('File does not exist')
        
        
    return text_list

        
def read_pickle(path_to_pkl):
    
    file_object = open(path_to_pkl, 'rb')
    word_dict = pickle.load(file_object)
    file_object.close()
    return word_dict


def sentiment_frequencies(text, dictionary_word):
    text_list = text.split()
    
    dict_frequency = dict.fromkeys(dictionary_word, 0)
    
    for word in text_list:
        for sentiment_type, sentiments in dictionary_word.items():
            if word in sentiments:
                dict_frequency[sentiment_type] += 1

    word_count = len(text_list)

    for sentiment_type in dict_frequency:
        dict_frequency[sentiment_type] = round((dict_frequency[sentiment_type])/
        word_count, 2)

    return dict_frequency

def compute_polarity(dict_frequency):
    highest_value = 0
    polarity = ''
    
    for sentiment_type, frequency in dict_frequency.items():
        if frequency > highest_value:
            polarity = sentiment_type
            highest_value = frequency
            
    return polarity

def analyse_text(text_path, dict_path):
    text = read_text(text_path)
    dictionary = read_pickle(dict_path)
    list_polarity = []
    
    stop_words = ['!', '.', '?', ';', '\n']
    
    for line in text:
        line = line.lower().strip()
        for item in stop_words:
            line = line.replace(item, '')
        
        # Analyze each line individually
        frequency_dictionary = sentiment_frequencies(line, dictionary)
        polarity = compute_polarity(frequency_dictionary)
        list_polarity.append(polarity)
        
    return list_polarity
