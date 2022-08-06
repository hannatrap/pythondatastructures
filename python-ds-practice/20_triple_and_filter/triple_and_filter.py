def triple_and_filter(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.
    
        >>> triple_and_filter([1, 2, 3, 4])
        [12]
        
        >>> triple_and_filter([6, 8, 10, 12])
        [24, 36]
        quit
        >>> triple_and_filter([1, 2])
        []
    """
    triples = []
    for num in nums:
        triples.append(num *3)

    by_four = []
    for num in triples:
        if num % 4 == 0:
            by_four.append(num)

    return by_four