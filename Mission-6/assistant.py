# Global variables initialization
file = None
word_list = []

# Function to load a file
def load_file(file_name):
    """
    Pre: Takes a file name as a parameter.
    
    Post: Reads the file content and assigns it to the global variable 'file'.
          Prints the number of lines and characters in the file.
    """
    global file
    try:
        file = open(file_name, "r").read()
        print(f"Loaded {file_name}")
    except FileNotFoundError:
        print("The specified file does not exist")

# Function to display information about the file
def show_info():
    """
    Pre: Requires the global variable 'file' with the file content.
    
    Post: Displays the number of lines and characters in the file.
    """
    global file
    try:
        len_lines = len(file.split("\n"))
        len_characters = len(file.replace("\n", "").replace(" ", ""))
        print(f"{len_lines} lines")
        print(f"{len_characters} characters")
    except AttributeError:
        print("You haven't specified a file. Use 'file <name>'")

# Function to use the file as a list of words
def use_words():
    """
    Pre: Requires the global variable 'file' with the file content.
    
    Post: Converts the file content into a list of tuples representing each line.
          Prints a message indicating that the file is now used as a list of words.
    """
    global file, word_list
    try:
        for line in file.split("\n"):
            coord_tuple = tuple(n for n in line.strip().split(","))
            word_list.append(coord_tuple)
        print("The file is now used as a list of words")
    except AttributeError:
        print("You haven't specified a file. Use 'file <name>'")

# Function to search for a word in the list of words
def search_word(word):
    """
    Pre: Takes a string parameter (a word).
    
    Post: Returns a bool indicating whether the word is in the global list of words.
    """
    global word_list
    try:
        is_in = any(word in t for t in word_list)
        if is_in:
            return f"'{word}' is in the list of words"
        else:
            return f"'{word}' is not in the list of words"
    except AttributeError:
        print("You haven't specified a file or used the 'words' command")

# Function to calculate the sum of specified numbers
def calculate_sum(numbers):
    """
    Pre: Takes a list of numbers as a parameter.
    
    Post: Returns an integer that is the sum of all the numbers.
    """
    try:
        numbers = [int(num) for num in numbers]
        total_sum = sum(numbers)
        return total_sum
    except ValueError:
        print("Invalid parameters. Use 'sum <number1> ... <numbern>'")

# Function to calculate the average of specified numbers
def calculate_avg(numbers):
    """
    Pre: Takes a list of numbers as a parameter.
    
    Post: Returns a float that is the average of all the numbers.
    """
    try:
        numbers = [int(num) for num in numbers]
        avg = sum(numbers) / len(numbers)
        return avg
    except (ValueError, ZeroDivisionError):
        print("Invalid parameters. Use 'avg <number1> ... <numbern>'")

# Function to display help
def show_help():
    """
    Pre: None.
    
    Post: Displays the list of allowed commands in the terminal.
    """
    print("The allowed commands are:")
    print("file <name> (specifies the name of a file that the tool should work on from now on)")
    print("info (shows the number of lines and characters in the file)")
    print("words (use the file as a list of words from now on)")
    print("search <word> (determine if the word is in the list of words)")
    print("sum <number1> ... <numbern> (calculates the sum of the specified numbers)")
    print("avg <number1> ... <numbern> (calculates the average of the specified numbers)")
    print("help (shows instructions to the user)")
    print("exit (stops the tool)")

if __name__ == "__main__":
    print("Welcome to your personalized tool!")
    # Main program loop
    while True:
        user_input = input("> ")
        splited_command = user_input.strip().split(" ")

        try:
            command = splited_command[0].lower()

            # Execution of the corresponding command
            if command == "file":
                load_file(splited_command[1])
            elif command == "info":
                show_info()
            elif command == "words":
                use_words()
            elif command == "search":
                print(search_word(splited_command[1]))
            elif command == "sum":
                print(calculate_sum(splited_command[1:]))
            elif command == "avg":
                print(calculate_avg(splited_command[1:]))
            elif command == "help":
                show_help()
            elif command == "exit":
                break
            else:
                print("Command not found! To get more information, try 'help'")
        
        except IndexError:
            print("Incomplete command. Please enter a valid command.")
        except Exception as e:
            print(f"{e}")