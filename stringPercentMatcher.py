from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

similar('Action, Adventure,  Fantasy, Magic', 'Drama, ')