from spell_corrector import correct_spelling

def test_spell():
    assert correct_spelling("I amm happyy") == "I am happy"
