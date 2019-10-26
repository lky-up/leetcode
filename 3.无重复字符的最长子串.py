"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
python 解释
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength=0
        retResult=[]
        for i in range(len(s)):
            if s[i] not in retResult:
                retResult.append(s[i])
            else:
                if len(retResult)>maxLength:
                    maxLength=len(retResult)

                for j in range(len(retResult)):
                    if retResult[0]!=s[i]:
                        retResult.remove(retResult[0])
                    else:
                        retResult.remove(retResult[0])
                        retResult.append(s[i])
                        break
        if len(retResult)>maxLength:
            return len(retResult)
        else:
            return maxLength
