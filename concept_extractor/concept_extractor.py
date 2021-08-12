from abc import ABC, abstractmethod
from .concept import MathConcept
from typing import List
import re


class ConceptExtractorABC(ABC):
    """ This class will take a input string and output the concepts in the
    text """
    def __init__(self, text: str):
        self.text = text
        self.concepts = []

    @abstractmethod
    def extract(self):
        """ This method will extract concepts from the text """
        pass

class MathExtractor(ConceptExtractorABC):
    """ This class will take text input and extract math concepts """
    
    def __init__(self, text: str):
        super(MathExtractor, self).__init__(text)
        self.tokens = self.tokenize_text(text)
        self.concepts = []

    def tokenize_text(self, text: str) -> list:
        """ Tokenize text """
        # extract text only contains letters, numbers and spaces
        text = re.sub(r'[^a-zA-Z0-9 ]', '', text)

        tokens = text.split()
        return tokens

    def extract_attribute_concept(self) -> List[MathConcept]:
        """ This will extract concepts that describe the with no value """
        concept_texts = ['odd']
        concepts = [MathConcept(x, None)
                    for x in self.tokens
                    if x in concept_texts]
        return concepts

    @staticmethod
    def get_concept_value(remaining_tokens: List[str],
                          token: str) -> List[MathConcept]:
        """Use the reminder of the list to get the value of the concept"""
        
        for remaining_token in remaining_tokens:
            if remaining_token.isdigit():
                concept = MathConcept(token, int(remaining_token))
                return concept

    def extract_single_value_concepts(self) -> List[MathConcept]:
        """ This will extract concepts that have a single value """
        concepts = []
        concept_texts = ['divisible']
        for index, token in enumerate(self.tokens):
            if token in concept_texts:
                remaining_tokens = self.tokens[index+1:]
                concept = self.get_concept_value(
                    remaining_tokens=remaining_tokens,
                    token=token)
                concepts.append(concept)
        return concepts

    def extract_concepts_from_text(self) -> list:
        """ Get math concepts from text """
        attribute_concepts = self.extract_attribute_concept()
        single_value_concepts = self.extract_single_value_concepts()
        concepts = attribute_concepts + single_value_concepts
        return concepts

    def extract(self):
        """ This method will extract concepts from the text """
        if self.text:
            self.concepts = self.extract_concepts_from_text()

        return self.concepts
