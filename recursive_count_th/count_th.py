'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # base case
    if word == "":
        return 0

    # recursive case
    if word[1] and word[0] + word[1] == "th":
        return 1 + count_th(word[2:])
    else:
        return 0 + count_th(word[2:])
    

print(count_th("wordthththth"))