import numpy as np

from typing import Iterable

from solution.exercise_01 import preprocess_text


class BagOfWordsVectorizer(object):

    def __init__(self):
        self._dictionary = None

    def fit(self, documents: Iterable[str]):
        if self._dictionary is not None:
            # Should raise an exception, as the model has been trained before
            return
        document_words = map(self._extract_preprocessed_words, documents)
        self._dictionary = list(set(sum(document_words, [])))

    def vectorize(self, document: str):
        output_vector = np.zeros(len(self._dictionary))
        document_words = self._extract_preprocessed_words(document)
        for word in document_words:
            if word not in self._dictionary:
                # There is a word that has never occurred during the training
                # so we cannot include it in the output vector
                continue
            word_index = self._dictionary.index(word)
            output_vector[word_index] = 1.0
        return output_vector

    def _extract_preprocessed_words(self, document):
        return list(set(preprocess_text(document).split()))
