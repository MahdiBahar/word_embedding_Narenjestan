
from preprocessing_func import convert_fa_numbers, convert_ar_characters, convert_en_numbers
from preprocessing_func import  remove_diacritics, map_num_to_text, merge_mi_prefix, replace_multiple_space, remove_punctuaction_except
from preprocessing_func import remove_half_space, remove_extra_charecter, remove_number, remove_punctuation

# import re



def preprocess(text,
               convert_farsi_numbers = False,
               convert_english_numbers = False,
               convert_arabic_characters = False,
               remove_diacritic = False,
               convert_emojis = False,
               remove_halfspace = False,
               remove_removelist = False,
               remove_extra_characters = False,
               remove_numbers = False,
               remove_punctuations = False,
               remove_punctuation_exception = True,
               replace_multiple_spaces = False,
               handle_prefix = False,
               map_number_to_text = False
               
               ):
    
    text = text.strip()

    if convert_farsi_numbers:
        text = convert_fa_numbers(text)

    if convert_arabic_characters:
# convert arabic characters to persian
        text = convert_ar_characters(text)

    if remove_diacritic:
        text = remove_diacritics(text)

    if remove_removelist:
        removelist = "<>"
        # text = re.sub(r'[^\w'+removelist+']', ' ', text)
        # text = re.sub(r'[^\w]', ' ', text)
        # text = re.sub(r'((#)[\w]*)','#',text)
    
    if remove_halfspace:
# remove half space
        text = remove_half_space(text)
    
    if remove_extra_characters:
        text = remove_extra_charecter(text)

    if map_number_to_text:
        text = map_num_to_text(text)

# remove numbers
    if remove_numbers:
        text = remove_number(text)

# convert english numbers to persian
    if convert_english_numbers:
        text = convert_en_numbers(text)
    
# remove punctuations
    if remove_punctuations:
        text = remove_punctuation(text)

# remove punctuation exception
    if remove_punctuation_exception:
        text = remove_punctuaction_except(text)

# replace multiple spaces with one space
    if replace_multiple_spaces:
        text = replace_multiple_space(text)

# prefix
    if handle_prefix:
        text = merge_mi_prefix(text)
   
    return(text)