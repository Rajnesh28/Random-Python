import re
import string


def is_palindrome(phrase):

    """Checks if a phrase is a palindrome or not, neglecting whitespace and punctuation

        Args:
            String phrase

        Returns boolean

    """

    
    phrase = phrase.lower()

    no_punctuation_phrase = re.sub(r'[^\w\s]', '', phrase)
    
    no_whitespace_phrase = re.sub(r"\s+", "", no_punctuation_phrase)
    
    reversed_phrase = no_whitespace_phrase[::-1]
                                           

    if no_whitespace_phrase == reversed_phrase:
        return True
    else:
        return False
    return no_whitespace_phrase
    

        
