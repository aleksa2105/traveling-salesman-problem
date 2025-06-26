from random import randint
    
def random_list_index(list_size: int, current_index: int):
    """ Return random list index that is not current_index """
    rand = randint(0, list_size - 2)
    return rand if rand < current_index else rand + 1