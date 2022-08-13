# Predictive-text
Generate sentences given training text and starting words.

This package contains the module 'markov', this provides 2 methods to take a text file as training data and output sentences that follow the style of the text.
Method 1 uses a markov chain approach, a dictionary is created with keys as every word that appears in the training text, the value of ech key is a list of all words that appear after in the text. Then given a starting word (that appears in the text at least once) its value list is sampled (with higher probability for more frequent words) to select a word that followed it in the text.
This is a simple approach that can generate a variety of new sentences from even small text inputs. However, due to the memoryless property of markov chains sentences can easily 'get lost' and lose structure:

Method 2 uses the same principle but instead pairs of successive words are used as dictionary keys, then given a starting pair of words (which appear in the text at least once) the same sampling approach is used to generate sentences.
This method gives more structured and understandable sentences as it retains memory of 2 previous words. This approach could be extended to use keys with longer sequences of words but combined with small text inputs this often leads to a problem of 'overfitting' where the ouput is simply the original text with very little variation. 
