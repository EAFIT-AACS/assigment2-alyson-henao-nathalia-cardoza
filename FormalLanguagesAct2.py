import random 
from nltk import CFG
from nltk.parse import ChartParser

# Function to generate accepted strings of the form a^n b^n
def accepted_strings(num_strings, string_list):
    for _ in range(num_strings):
        num_character = random.randint(0, 5)  
        string = 'a' * num_character + 'b' * num_character  # Generate string with equal number of 'a's and 'b's
        print(f"String: '{string}'")
        string_list.append(string)  
    return string_list # Return the list of accepted strings


# Function to generate rejected strings with random characters from the alphabet
def rejected_strings(alphabet, num_strings, string_list):
    for _ in range(num_strings):
        num_character = random.randint(1, 10) 
        string = ''.join(random.choice(alphabet) for _ in range(num_character))  # Generate random string

        # Reject the string if the number of 'a's does not equal the number of 'b's
        if not string.count('a') == string.count('b'):
            print(f"String: '{string}'") 
            string_list.append(string)  
    return string_list  # Return the updated list of rejected strings

# Function to simulate a PDA and check if strings are accepted or rejected
def pda_M(string_list, alphabet):
    N = {"Q": "q0", "sigma": alphabet, "stack_alphabet": ['S', 'A'], "s": "q0"}  # Define the PDA

    for string in string_list:
        stack = ['S']  # Initialize the stack with the initial symbol
        valid = True  # Flag to check if the string follows the pattern a^n b^n

        for symbol in string:
            # Handle 'a' and push 'A' onto the stack
            if (symbol == 'a' and stack[-1] == 'S') or (symbol == 'a' and stack[-1] == 'A'):
                stack.append('A')
            # Handle 'b' and pop 'A' from the stack
            elif symbol == 'b' and stack[-1] == 'A':
                stack.pop()
            else:
                valid = False  # Invalid string if there's more 'b' than 'a'
                break

        if valid and stack == ['S']:
            print(f"The string '{string}' is accepted by the automaton.")
        else:
            print(f"The string '{string}' is rejected by the automaton.")

# Function to generate and print syntax trees for valid strings
def tree(string_list):
    for string in string_list:
        grammar = CFG.fromstring("""
            S -> 'a' S 'b' |  # Define the grammar for the language a^n b^n
        """)
        
        parser = ChartParser(grammar)  # Create a parser for the grammar
        characters = list(string)
        
        # Generate and display the derivation trees
        for tree in parser.parse(characters):
            print("Tree")
            tree.pretty_print()

# Function to simulate and show the sentential form and configuration of the string processing
def sf_c(string_list):
    for string in string_list:
        stack = ['S']  # Initialize the stack with the initial symbol
        sentential_form = ""  
        print(f"\nSentential form and Configuration of '{string}':\nS           (q0, '{string}', S)")
        symbol = list(string) 
        
        while symbol:  # Continue while there are symbols to process
            if symbol[0] == 'a' and stack[-1] == 'S':  # Handle 'a' and stack 'S'
                stack.append('A')
                sentential_form += symbol[0]
                del symbol[0]  
                string = ''.join(symbol)
                stack_ = ''.join(stack)
                print(f"{sentential_form}{stack_}           (q0, '{string}', {stack_})")
            elif symbol[0] == 'a' and stack[-1] == 'A':  # Handle 'a' and stack 'A'
                stack.append('A')
                sentential_form += symbol[0]
                del symbol[0]  
                string = ''.join(symbol)
                stack_ = ''.join(stack)
                print(f"{sentential_form}{stack_}           (q0, '{string}', {stack_})")
            elif symbol[0] == 'b' and stack[-1] == 'A':  # Handle 'b' and pop 'A'
                stack.pop()
                sentential_form += symbol[0]
                del symbol[0]  
                string = ''.join(symbol)
                stack_ = ''.join(stack)
                print(f"{sentential_form}{stack_}           (q0, '{string}', {stack_})")
        
        # Final configuration if no symbols are left and stack is reduced to just 'S'
        if not symbol and stack[-1] == 'S':
            stack.pop()
            stack_ = ''.join(stack)
            print(f"{sentential_form}{stack_}           (q0, '{string}', '{stack_}')")


"""
    Transitions:
        i. ((q0, a, S), (q0, AS))  
        ii. ((q0, a, A), (q0, AA))  
        iii. ((q0, b, A), (q0, e))  
        iv. ((q0, e, S), (q0, e))   
"""
    
alphabet = ['a', 'b']
num_strings = random.randint(2, 3)

# Initialize the lists for accepted and rejected strings
accepted_list = []
rejected_list = []

# Algorithm 1: Generate accepted and rejected strings
accepted_strings = accepted_strings(num_strings, accepted_list)
rejected_strings = rejected_strings(alphabet, num_strings, rejected_list)

print()

# Algorithm 2: Run PDA on accepted and rejected strings
pda_M(accepted_strings, alphabet)
pda_M(rejected_strings, alphabet)

print()

# Algorithm 3: Generate trees and sentential forms for accepted strings
tree(accepted_strings)
sf_c(accepted_strings)