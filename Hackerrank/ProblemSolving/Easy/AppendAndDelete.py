def appendAndDelete(s, t, k):
    def delete(word):
        word = word[:-1]
    def add(word, toAdd):
        word += toAdd
    count = 0
    border = 0
    if s == t:
        count = len(s) + len(t) + 1
        return "Yes" if count == k else "No"
    for i in range(max(len(s), len(t))):
        if border == 0:
            try:
                if s[i] is not t[i]:
                    border = i
                    break
            except:
                border = i
                break
    if len(s) > len(t):
        for i in range(len(s)):
            if s is not t[border]:
                delete(s)
    elif len(s) < len(t):
        # if add()
        if count is not k:
            for i in range(1, min(len(s), len(t))):
                count += 2 * i
                if count == k:
                    return "Yes"
                else:
                    return "No"
    else:
        count = len(s) + len(t) + 1
        return "Yes" if count == k else "No"




# print(appendAndDelete("hackerhappy", "hackerrank", 9))  # Yes # 9
# print(appendAndDelete("aba", "aba", 7))  # Yes # 7
# print(appendAndDelete("ashley", "ash", 2))  # No # 3
# print(appendAndDelete("y", "yu", 2))  # No # 1
# print(appendAndDelete("zzzzz", "zzzzzzz", 4))  # Yes # 2
print(appendAndDelete("aaa", "a", 5))  # Yes # 2
