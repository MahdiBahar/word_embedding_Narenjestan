import re
from typing import List, Optional
import string

def _multiple_replace(mapping, text):
    pattern = "|".join(map(re.escape, mapping.keys()))
    return re.sub(pattern, lambda m: mapping[m.group()], str(text))

def convert_fa_numbers(input_str):
    mapping = {
        '۰': '0',
        '۱': '1',
        '۲': '2',
        '۳': '3',
        '۴': '4',
        '۵': '5',
        '۶': '6',
        '۷': '7',
        '۸': '8',
        '۹': '9',
        '.': '.',
    }
    return _multiple_replace(mapping, input_str)

def convert_en_numbers(input_str):
    mapping = {
         '0': '۰',
         '1' : '۱',
         '2' :'۲',
        '3'  :'۳',
        '4'  :'۴',
        '5' :'۵',
        '6' :'۶',
        '7' :'۷',
        '8' :'۸',
        '9' :'۹',
        '.' :'.'
    }
    return _multiple_replace(mapping, input_str)

def convert_ar_characters(input_str):
    """
    Converts Arabic chars to related Persian unicode char
    """
    mapping = {
        'ك': 'ک',
        'ى': 'ی',
        'ي': 'ی',
        'ئ':'ی',
        'إ':'ا',
        'أ':'ا',
        'ة':'ه',
        'ؤ':'و'
    }
    return _multiple_replace(mapping, input_str)

#-------------------------------------------------------------------------------------------


def merge_mi_prefix(text):
    zwnj = '\u200C'    # zero-width non-joiner
    # note: replacement is NOT a raw string, so \u200C is interpreted properly
    replacement = r'\1' + zwnj + r'\2'
    return re.sub(r'\b(ن?می)\s+(\S+)', replacement, text)

def remove_diacritics(text):
    # define regex for Persian diacritics (Unicode range: \u064B-\u0652)
    diacritics_pattern = re.compile(r'[\u064B-\u0652]')
    return re.sub(diacritics_pattern, '', text)


def convert_number_to_text(text):
    
    return re.sub(r'(\d)\d*', r'\1', text)

def remove_half_space(text):

    text = text.replace('\u200c', '')
    return text

def remove_extra_charecter(text):

    return re.sub(r'(\w)\1{2,}', r'\1\1',text)

def remove_number(text):

    return re.sub(r' [\d+]', ' ',text)

def remove_punctuation(text):

    return re.sub(r'[^\w\[\]]', ' ', text)

def replace_multiple_space(text):

    return re.sub(r'[\s]{2,}', ' ', text)


def map_num_to_text(text):

    # check if the text is exactly '1', '2', '3' , '4', '5'
    mapping = {'1': 'خیلی بد', '2': 'بد', '3': 'متوسط' , '4': 'خوب' , '5': 'عالی'}
    
    if text in mapping:
        return mapping[text]  
    
    return text 
#--------------------------------------------------------------------------------------------------------

# def remove_punctuaction_except(text):
#     # start with the ASCII punctuation minus the parentheses
#     punctuation = string.punctuation.replace("(", "").replace(")", "")
#     # add common Persian punctuation characters
#     punctuation += "،؟؛«»"
#     # create a character set pattern from the punctuation characters
#     pattern = "[" + re.escape(punctuation) + "]"
#     # replace every punctuation character in the pattern with a space
#     return re.sub(pattern, " ", text)


def remove_punctuation_except_keep(
    text: str,
    keep: Optional[List[str]] = None
) -> str:
    # Determine which chars to keep 
    default_keep = []
    # default_keep = ['(', ')', '،', '؟', '؛', '«', '»']
    keep_set = set(keep) if keep is not None else set(default_keep)

    # Build the full punctuation set
    ascii_punct   = set(string.punctuation)                    # !"#$%&'()*+,...@
    persian_punct = set(list("،؟؛«»"))                         # common Persian punctuation
    all_punct     = ascii_punct | persian_punct

    # Compute which to remove
    remove_chars = all_punct - keep_set

    # Build regex and clean 
    # [chars]+ will match any run of unwanted punctuation
    pattern = re.compile("[" + re.escape("".join(remove_chars)) + "]+")
    # replace with a single space, then collapse multiple spaces
    cleaned = pattern.sub(" ", text)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned



# Split sentences on . ! ? followed by whitespace
_SENT_SPLIT = re.compile(r'(?<=[.!?])\s+')

def drop_short_sentences(text: str, min_words: int = 0) -> str:
 
    sentences = _SENT_SPLIT.split(text)
    kept = []
    for sent in sentences:
        sent = sent.strip()
        # count words by splitting on whitespace
        if sent and len(sent.split()) >= min_words:
            kept.append(sent)
        # else: drop this sentence entirely
    return ' '.join(kept)



def remove_phrases(text: str, phrases: List[str] = []) -> str:
    if not phrases:
        return text.strip()
    
    # 1) Escape and join into an alternation
    escaped = [re.escape(p) for p in phrases]
    pattern = re.compile(
        r'\s*(?:' + "|".join(escaped) + r')\s*'
    )
    
    # 2) Delete them
    cleaned = pattern.sub(' ', text)
    # 3) Collapse multiple spaces, trim
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned