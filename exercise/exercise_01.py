import re

# https://gist.github.com/Alex-Just/e86110836f3f93fe7932290526529cd1
EMOJI_REGEX = re.compile("([\U00010000-\U0010ffff])", re.UNICODE)
DUPLICATED_SYMBOL_REGEX = re.compile(r"([^a-z0-9])\1+", re.UNICODE | re.I)
PUNCTUATION_MARKS_REGEX = re.compile(r"([,\.\!\?\[\]\(\)])", re.UNICODE)


def preprocess_text(raw_text):
    # Convert all the letters to lowercase
    text = raw_text.lower()
    # Remove hashtag symbol and "at" for user mentions
    text = text.replace("#", "")
    text = text.replace("@", "")
    # Divide the emojis written in a row with spaces
    text = EMOJI_REGEX.sub("\\1 ", text)
    # Remove quotation marks
    text = text.replace("\"", "")
    text = text.replace("'", "")
    # Get rid of the misused spaces by
    text = PUNCTUATION_MARKS_REGEX.sub(" \\1 ", text)
    # Divide duplicated characters, so after text split they'll be treated
    # as if they were a single character used a couple of times
    text = DUPLICATED_SYMBOL_REGEX.sub("\\1", text)
    # Return preprocessed value
    return text
