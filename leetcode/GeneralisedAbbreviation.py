
def generateAbbreviations():
    """
    :type word: str
    :rtype: List[str]
    """
    word = 'word'
    def generateAbbreviationsHelper(word, i, cur, res):
        if i == len(word):
            res.append("".join(cur))
            return
        cur.append(word[i])
        generateAbbreviationsHelper(word, i + 1, cur, res)
        cur.pop()
        if not cur or not cur[-1][-1].isdigit():
            for l in range(1, len(word) - i + 1):
                cur.append(str(l))
                generateAbbreviationsHelper(word, i + l, cur, res)
                cur.pop()

    res, cur = [], []
    generateAbbreviationsHelper(word, 0, cur, res)
    print(res)

generateAbbreviations()