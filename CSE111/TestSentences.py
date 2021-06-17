from Sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_punctuation
import pytest

def test_get_determiner():
    # Test the singular determiners.
    singular_determiners = ["the", "one"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiners

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural determiners.
    plural_determiners = ["some", "many"]
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    singular_nouns = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]
    for _ in range(4):
        word = get_noun(1)
        assert word in singular_nouns
    
    plural_nouns = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]
    for _ in range(4):
        word = get_noun(2)
        assert word in plural_nouns

def test_get_verb():
    tense_past_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(4):
        word = get_verb("", "past")
        assert word in tense_past_verbs
    
    tense_present_q_1 = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        word = get_verb(1, "present")
        assert word in tense_present_q_1

    tense_present_q_many = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
        word = get_verb(2, "present")
        assert word in tense_present_q_many

    tense_future = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    for _ in range(4):
        word = get_verb("", "future")
        assert word in tense_future

def test_get_preposition():
    preps = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(4):
        prep = get_preposition()
        assert prep in preps

def test_get_prepositional_phrase():
    for _ in range(4):
        phrase = get_prepositional_phrase(1)
        assert phrase
        phrase2 = get_prepositional_phrase(2)
        assert phrase2

def test_get_punctuation():
    for _ in range(4):
        punct = get_punctuation()
        assert punct

pytest.main(["-v", "--tb=line", "-rN", "/Users/kylejohnson/Documents/Python/CSE111/TestSentences.py"])