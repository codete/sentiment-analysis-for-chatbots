from typing import Iterable


class BagOfWordsVectorizer(object):

    def __init__(self):
        self._dictionary = []

    def fit(self, documents: Iterable[str]):
        pass

    def vectorize(self, document: str):
        pass
