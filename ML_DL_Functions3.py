import numpy as np
from torch import nn as nn
def convert_words_to_indices(sents,vocab_stoi): # 10% grade
    """
    This function takes a list of sentences 
    input: list of list of words [[word,word,..,word],..,[word,..,word]] where each word is a string with no spaces
    and returns a new list with the same structure, but where each word is replaced by its index in `vocab_stoi`.
    output: list of lists of integers [[int,int,..,int],..,[int,..,int]] where each int is the idx of the word according to vocab_stoi

    Example:
    >>> convert_words_to_indices([['one', 'in', 'five', 'are', 'over', 'here'], ['other', 'one', 'since', 'yesterday'], ['you']])
    [[148, 98, 70, 23, 154, 89], [151, 148, 181, 246], [248]]
    """

    # Write your code here
    return [[vocab_stoi[word] for word in sentence] for sentence in sents]

def generate_4grams(seqs): # 10% grade
    """
    This function takes a list of sentences (list of lists) and returns
    a new list containing the 4-grams (four consequentively occuring words)
    that appear in the sentences. Note that a unique 4-gram can appear multiple
    times, one per each time that the 4-gram appears in the data parameter `seqs`.

    Example:

    >>> generate_4grams([[148, 98, 70, 23, 154, 89], [151, 148, 181, 246], [248]])
    [[148, 98, 70, 23], [98, 70, 23, 154], [70, 23, 154, 89], [151, 148, 181, 246]]
    >>> generate_4grams([[1, 1, 1, 1, 1]])
    [[1, 1, 1, 1], [1, 1, 1, 1]]
    """
    return [seq[i:i+4] for seq in seqs for i in range(len(seq) - 3)]

def make_onehot(data): # 10% grade
    """
    Convert one batch of data in the index notation into its corresponding onehot
    notation. Remember, the function should work for both xt and st.

    input - vector with shape D (1D or 2D)
    output - vector with shape (D,250)
    """
    vocab_size =250
    onehot = np.eye(vocab_size)[data]
    return onehot

class PyTorchMLP(nn.Module): # 35% grade for each model
    def __init__(self):
        super(PyTorchMLP, self).__init__()
        self.num_hidden = 1024 # TODO: choose number of hidden neurons
        self.layer1 = nn.Linear(750, self.num_hidden)
        self.layer2 = nn.Linear(self.num_hidden, 250)
        
    def forward(self, inp):
        inp = inp.reshape([-1, 750])
        # TODO: complete this function
        # Note that we will be using the nn.CrossEntropyLoss(), which computes the softmax operation internally, as loss criterion
        # Pass through the first linear layer
        x = self.layer1(inp)
        
        # Apply ReLU activation
        x = nn.functional.relu(x)
        
        # Pass through the second linear layer
        x = self.layer2(x)
        return x