import re

def clean_text(text):
    """
    Cleans raw text by converting to lowercase and removing special characters.
    """
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text
