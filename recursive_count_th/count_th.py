"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""


def count_th(word):
    # declare a local function that also uses a counter
    def total_count(word, count):
        # find the index at which 'th' appears
        index = word.find("th")
        # if it finds it
        if index >= 0:
            word = word[index + 2 :]
            # call again with an increased count
            return total_count(word, count + 1)
        return count  # defaults to 0, which is num passed in

    return total_count(word, 0)

    #! another way
    # count = word.count("th")
    # print(count)
    # return count
    # count = 0
    # if len(word) >= 2:
    #     if word[0] == "t" and word[1] == "h":
    #         count += 1
    #         return count + count_th(word[1:])
    #     else:
    #         return count_th(word[1:])
    # else:
    #     return count


# print(f'count is {count_th("another")}')
