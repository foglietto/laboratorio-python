# Esercizio 06.1.1
# Conteggio vocali

#  Use a function to count the number of vowels in a string.

def main():
    input_str = input("Enter a string: ")
    print("The string contains", count_vowels(input_str), "vowels")


def count_vowels(string):
    """
    Count the number of vowels in a string.

    :param string: the string of characters to process
    :return: the number of vowels
    """
    count = 0
    for ch in string:
        if ch.upper() in "AEIOU":
            count = count + 1
    return count


# Call the main function.
main()
