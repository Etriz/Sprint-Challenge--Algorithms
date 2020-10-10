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
        return count  # defaults to 0

    return total_count(word, 0)


# print(f'count is {count_th("another")}')
