def lengthOfLongestSubstring(s):
    """Longest Substring Without Repeating Characters

    Given a string, find the length of the longest substring without repeating characters.

    Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
    
    :type s: str
    :rtype: int
    """
    d = dict()
    ans = 0
    i = 0
    for index, letter in enumerate(s):
        if letter in d:
            if d[letter]>=i:
                i = d[letter] + 1
        d[letter] = index
        ans = max(ans, index-i+1)
    return ans

lengthOfLongestSubstring("abcabcbb")
