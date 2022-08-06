
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    # freq1 = {}

    # freq2 = {}

    # for num in num1:
    #     if item in freq1:
    #         freq1[num] += 1

    #     else:
    #         freq1[num] = 1


    # for num in num2:
    #     if item in freq2:
    #         freq2[num] += 1

    #     else:
    #         freq2[num] = 1

    # if freq1 == freq2:
    #     return True

    # else:
    #     return False

    def freq_counter(coll):

    counts = {}

    for x in coll:
        counts[x] = counts.get(x, 0) + 1

    return counts

    def same_frequency(num1, num2):
    

        return freq_counter(str(num1)) == freq_counter(str(num2))