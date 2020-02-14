#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i, w in enumerate(weights):
        hash_table_insert(ht, w, i)

    answer = None
    for i, w in enumerate(weights):
        pair = limit - w
        index2 = hash_table_retrieve(ht, pair)
        if index2:
            answer = (index2, i)
            break

    print_answer(answer)
    return answer


def print_answer(answer):
    if answer is not None:
        print(str(answer[0]) + " " + str(answer[1]))
    else:
        print("None")
