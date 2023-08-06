Sentiment Lexicon
=================

Sentiment lexicon wrapper and generator.

Installation
------------
::

  pip install sentiment-lexicon


Usage
-----
The module provides a single class, ``Lexicon``, that can be used as a simple wrapper around sentiment lexicon data.
The sentiment value of a given word can be accessed via the ``value`` instance method.

.. code:: python

  from sentiment_lexicon import Lexicon

  lexicon = Lexicon(words, values)

  lexicon.value('good') # => 1


The class can also generate a sentiment lexicon based on positive and negative input documents.

.. code:: python

  lexicon = Lexicon.from_labelled_text(positive_documents, negative_documents)

More information is available in the `documentation
<https://emilbaekdahl.github.io/sentiment_lexicon>`_.
