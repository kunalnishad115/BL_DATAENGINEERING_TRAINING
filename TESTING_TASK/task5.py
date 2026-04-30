import re
class InputSanitizationError(Exception):
    pass


def sanitize_input(text):

    
    cleaned_text = re.sub(r"[^a-zA-Z0-9\s-]", "", text)

    
    cleaned_text = cleaned_text.strip()

    if cleaned_text == "":
        raise InputSanitizationError("Cleaned text is empty")

    return cleaned_text