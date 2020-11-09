def get_indices_of_item_weights(weights, length, limit, cache={}):
    """
    YOUR CODE HERE
    """
    # Your code here
    for index in range(len(weights)):
        cache[weights[index]] = index
    for index in range(len(weights)):
        lw = limit - weights[index]
        if lw in cache:
            return (max(index, cache[lw]), min(index, cache[lw]))
