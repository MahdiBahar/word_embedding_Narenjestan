# word_embedding_Narenjestan
### Note: In order to use Hazm library, I force to install python 3.11.11 for campatibality.

## In preprocessing part:
## We use Final_clean_dataset_narenjestan.ipynb code
## From dataset folder: 
## narenjestan_khowledgebase_editable.xlsx
## V_4_deduplicated_sentences.xlsx
## MEC-Narenjestan_cleaned-V0.5
## or MEC-Narenjestan_cleaned-merged_output-V0.2
### With punctuation
## MEC-Narenjestan_cleaned_with_punc-V0.6
## or MEC-Narenjestan_cleaned_with_punc-merged_output-V0.3


## every pos tagging codes are running on venv11-hazm environment
## After checking Hazm, Dadmatools, Stanza and Parsivar, we can conclude that:
## 1- For lemmetization and stemming, Parsivar and Stanza have better performance.
## 2- For POS tagging HAZM has the best performaance between all options.

## Tagged_token_example.txt is the final results which consists of lemmatization, poss_tagging and converting verb-compond 