def separate_and_convert(input_string):
    # Separate the string into number and letter substrings
    number_substring = ''.join(char for char in input_string if char.isdigit())
    letter_substring = ''.join(char for char in input_string if char.isalpha())

    # Convert even numbers in the number substring to ASCII Code Decimal Values
    even_numbers = [int(char) for char in number_substring if int(char) % 2 == 0]
    ascii_values_numbers = [ord(str(char)) for char in even_numbers]

    # Convert upper-case letters in the letter substring to ASCII Code Decimal Values
    uppercase_letters = [char for char in letter_substring if char.isupper()]
    ascii_values_letters = [ord(char) for char in uppercase_letters]

    return number_substring, letter_substring, even_numbers, ascii_values_numbers, uppercase_letters, ascii_values_letters

# Example Scenario
input_string = '56aAww1984sktr235270aYmn145ss785fsq31D0'
number_substring, letter_substring, even_numbers, ascii_values_numbers, uppercase_letters, ascii_values_letters = separate_and_convert(input_string)

print(f"Number Substring: {number_substring}")
print(f"Letter Substring: {letter_substring}")
print(f"Even Numbers: {even_numbers}")
print(f"ASCII Values of Even Numbers: {ascii_values_numbers}")
print(f"Uppercase Letters: {uppercase_letters}")
print(f"ASCII Values of Uppercase Letters: {ascii_values_letters}")
