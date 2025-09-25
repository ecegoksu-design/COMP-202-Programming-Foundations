# 1. Please complete the following:
#   Your First name and Last Name: Ece Goksu
#   Your Student ID: 261138642

# 2. Write your program here:
#Global Constants
BACKWARD = -1
FORWARD = 1
FIRST_INDEX = 0
SECOND_INDEX = 1
TRAVERSE_CONSTANT = 1
SEPARATION = '-'

def is_outside_list(letter_list, index):
    """
    (list, int) -> (bool)
    Returns if an index is outside of a given list
    >>> is_outside_list(['A', 'B', 'C', 'D', 'E'], 4)
    False
    >>> is_outside_list(['A', 'B', 'C', 'D', 'E'], 7)
    True
    >>> is_outside_list(['A', 'B', 'C', 'D', 'E'], -3)
    True
    """
    #Return if index is outside of a list
    return not FIRST_INDEX <= index < len(letter_list)

def letter_positions(letter_list, character):
    """
    (list, str) -> (list)
    Returns the index positions of a character in a given list as a list
    >>> letter_positions(['A', 'A', 'B', 'A', 'C', 'D'], 'A')
    [0, 1, 3]
    >>> letter_positions(['A', 'A', 'B', 'A', 'C', 'D'], 'E')
    []
    >>> letter_positions(['A', 'A', 'B', 'A', 'C', 'D'], 'D')
    [5]
    """
    #Define initial empty index list
    index_list = []
    
    #Update index list if the character is found at a given index
    for index in range(len(letter_list)):
        if letter_list[index] == character:
            index_list.append(index)
            
    return index_list

def valid_word_pos_direction(letter_list, word, index, direction):
    """
    (list, str, int, int) -> (bool)
    Returns if a given word can be found in the list in the given direction
    >>> valid_word_pos_direction(['F', 'A', 'I','R', 'Y'], 'AIR', 1, 1)
    True
    >>> valid_word_pos_direction(['A', 'B', 'C','D', 'E'], 'ABD', 0, 1)
    False
    >>> valid_word_pos_direction(['A', 'B', 'C','D', 'E'], 'EDC', 4, -1)
    True
    """
    #Start at first index
    word_index = FIRST_INDEX
    
    #Without going out of the list, traverse through every word character
    while not is_outside_list(letter_list, index) and word_index < len(word):
        if letter_list[index] != word[word_index]:
            return False
        word_index += TRAVERSE_CONSTANT
        index += direction
        
    return word_index == len(word)

def direction_word_given_position(letter_list, word, index):
    """
    (list, str, int) -> (list)
    Returns the directions which a word can be found in an index of a list
    >>> direction_word_given_position(['P', 'R', 'S', 'T', 'S', 'P'], 'TS', 3)
    [-1, 1]
    >>> direction_word_given_position(['P', 'R', 'S', 'T', 'S', 'P'], 'PST', 5)
    [-1]
    >>> direction_word_given_position(['P', 'R', 'S', 'T', 'S', 'P'], 'TSA', 3)
    []
    """
    #Define an initial empty direction list
    direction_list = []
    
    #Update list with directions a word can be found at
    if letter_list[index] == word[FIRST_INDEX]:
        for direction in [BACKWARD, FORWARD]:
            if valid_word_pos_direction(letter_list, word, index, direction):
                direction_list.append(direction)
                
    return direction_list

def position_direction_word(letter_list, word):
    """
    (list, str) -> (list)
    Returns the indices and directions a word is found in a given list
    >>> position_direction_word(['C', 'D', 'C', 'D', 'C','D'], 'DC')
    [[1, -1], [1, 1], [3, -1], [3, 1], [5, -1]]
    >>> position_direction_word(['P', 'R', 'S', 'T', 'S','R'], 'AB')
    []
    >>> position_direction_word(['P', 'R', 'S', 'T', 'S','R'], 'TSR')
    [[3, -1], [3, 1]]
    """
    #Define an empty inital index and direction list
    index_direction_list =[]
    index_list = letter_positions(letter_list, word[FIRST_INDEX])
    
    #Create a nested list with indices and directions a word is found 
    for index in index_list:
        direction_list = direction_word_given_position(letter_list, word, index)
        for direction in direction_list:
            index_direction_list.append([index, direction])
            
    return index_direction_list

def cross_word_position_direction(bool_letter_list,length_word,index,direction):
    """
    (list, int, int, int) ->  (None)
    Updates the boolean list comparing to a word
    """
    #Traverse forward and update boolean list
    if direction == FORWARD:
        for item in range(index, index + length_word):
            bool_letter_list[item] = True
    
    #Traverse backword and update boolean list
    elif direction == BACKWARD:
        for item in range(index, index - length_word, BACKWARD):
            bool_letter_list[item] = True
        
def cross_word_all_position_direction(bool_letter_list,length_word,list_position_direction):
    """
    (list, int, list) -> (None)
    Updates the boolean list comparing to all words
    """
    #Update the booelean list referring to the directions and indices found
    for nested_list in range(len(list_position_direction)):
        
        #Assign idx indices in position and direction nested list
        idx = list_position_direction[nested_list][FIRST_INDEX]
        
        #Assign drctn directions in position and direction nested list
        drctn = list_position_direction[nested_list][SECOND_INDEX]
        
        #Update the boolean list according to indices and directions found
        cross_word_position_direction(bool_letter_list, length_word, idx, drctn)
            
def find_magic_word(letter_list, bool_letter_list):
    """
    (list, list) -> (str)
    Returns the uncrossed letters when the searched words are found
    >>> find_magic_word(['F','A','I','R','Y'], [True,False,False,False,True])
    'AIR'
    >>> find_magic_word(['F','A','I','R','Y'], [True,True,True,True,True])
    ''
    >>> find_magic_word(['F','A','I','R'], [True,True,True,True,True])
    Traceback (most recent call last):
    ValueError: Both lists should have the same size
    """
    #If boolean list doesn't match letter list, raise error
    if len(letter_list) != len(bool_letter_list):
        raise ValueError('Both lists should have the same size')
    
    #Define empty magic word list
    uncrossed = []
    
    #Update magic word list with characters that match to False in boolean list
    for letter in range(len(letter_list)):
        if bool_letter_list[letter] == False:
            uncrossed.append(letter_list[letter])
    
    #Join uncrossed letters in the letter list, convert to string
    return ''.join(uncrossed)

def word_search(letter_list, word_list):
    """
    (list, list) -> (str)
    Returns the uncrossed letters when a list of words is found in letter list
    >>> word_search(['M','A','I','R','O','N','K','O','T','Y'], ['AIR','OK'])
    'MONTY'
    >>> word_search(['M','A','I','R','O','N','K','O','T','Y'], ['FAIR','OP'])
    'MAIRONKOTY'
    >>> word_search(['M','A','I','R','O','N','K','O','T','Y'],['MAIRON','KOTY'])
    ''
    """
    #Create a boolean list of the same size as the letter list 
    bool_list = [False] * len(letter_list)
    
    #Cross the letters found
    for word in word_list:
        index_direction = position_direction_word(letter_list, word)
        cross_word_all_position_direction(bool_list, len(word), index_direction)
    
    #Return the uncrossed letters
    uncrossed = find_magic_word(letter_list, bool_list)
    return uncrossed

def word_search_main(letters, words):
    """
    (str, str) -> (str)
    Returns the uncrossed letters after creating letter and word lists
    >>> word_search_main('mCoMp202on++cty', 'CoMp202-C++')
    'MONTY'
    >>> word_search_main('mCoMp202on++cty', 'COmP-C++')
    'M202ONTY'
    >>> word_search_main('mCoMp202on++cty', 'MCOmP202-oN-C++-tY')
    ''
    """
    #Capitalize letters in letter list
    letter_list = list(letters.upper())
    
    #Separate word in word list by '-' and capitalize
    word_list = words.upper().split(SEPARATION)
    
    #Return the uncrossed letters after going through the letter list with words
    uncrossed = word_search(letter_list, word_list)
    return uncrossed