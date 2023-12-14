import assistant as main

# Test load_file function
def test_load_file():
    main.load_file("all-words.dat")
    assert main.file is not None

# Test show_info function
def test_show_info():
    main.file = "Line 1\nLine 2\nLine 3"
    main.show_info()

# Test use_words function
def test_use_words():
    main.file = "word1,word2\nword3,word4"
    main.use_words()
    assert main.word_list == [('word1', 'word2'), ('word3', 'word4')]

# Test search_word function
def test_search_word():
    main.word_list = [('apple', 'orange'), ('banana', 'grape')]
    assert main.search_word('apple') == "'apple' is in the list of words"
    assert main.search_word('kiwi') == "'kiwi' is not in the list of words"

# Test calculate_sum function
def test_calculate_sum():
    assert main.calculate_sum(['1', '2', '3']) == 6
    assert main.calculate_sum(['-1', '5', '10']) == 14

# Test calculate_avg function
def test_calculate_avg():
    assert main.calculate_avg(['1', '2', '3']) == 2.0
    assert main.calculate_avg(['-1', '5', '10']) == 4.666666666666667

# Test show_help function
def test_show_help():
    main.show_help()
    # Check if there are any print errors

if __name__ == "__main__":
    # Run the tests
    test_load_file()
    test_show_info()
    test_use_words()
    test_search_word()
    test_calculate_sum()
    test_calculate_avg()
    test_show_help()

    print("-------All tests passed!-------")