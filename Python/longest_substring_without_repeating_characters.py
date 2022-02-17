def lengthOfLongestSubstring(s: str) -> int:
    longer = 0
    actual = 0
    substring = ''
    for letter in s:
        if letter not in substring:
            substring += letter
            actual+=1
            longer = actual if actual > longer else longer
        else:
            substring = substring[(substring.index(letter)+1):] + letter
            actual = len(substring)
    return longer
    


print(lengthOfLongestSubstring("aabaab!bb"))