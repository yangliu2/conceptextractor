import pytest
from concept_extractor.concept import MathConcept
from concept_extractor.concept_extractor import MathExtractor


math_problem = f"What is the odd number between 16 and 34 that's divisible by 5?"

@pytest.fixture
def math_extractor():    
    return MathExtractor(text=math_problem)

def test_math_extractor(math_extractor):
    concepts = [MathConcept(name='odd', value=None),
                MathConcept(name='divisible', value=5),
                # MathConcept(name='between', value=[16, 34])
                ]

    assert math_extractor.extract()[1] == concepts[1]
