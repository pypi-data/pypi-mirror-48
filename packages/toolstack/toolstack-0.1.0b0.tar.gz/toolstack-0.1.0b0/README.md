# ToolStack

A set of tools for Mining Intelligence.

Requirements
------------

-  Python 3.5 or higher
-  Pandas
-  NumPy
-  NLTK


Installation
------------

Using PIP via PyPI

    pip install toolstack

Anaconda

    conda install -c mkhan7 toolstack
    
    
    
Examples
--------

    >>> from toolstack import text_preprocessing as tp
    >>> import pandas as pd
    >>> import numpy as np
    >>>
    >>> # Import some text data
    >>> df = pd.read_csv('amazon-review-300.csv', header=-1)
    >>>
    >>> # Return the word and occurrence
    >>> tp.count_word(df, 1, sw=True, sort='descending')
