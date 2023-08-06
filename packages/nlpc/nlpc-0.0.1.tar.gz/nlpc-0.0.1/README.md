# nlpc
**nlpc** is a super fast c++ library which adopts dynamic programming(DP) algorithm to solve classic nlp problems as below .  
  
[The longest common subsequence](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem) problem is the problem of finding the longest subsequence common to all sequences in a set of sequences (often just two sequences).  
  
[The longest common substring](https://en.wikipedia.org/wiki/Longest_common_substring_problem) problem is to find the longest string (or strings) that is a substring (or are substrings) of two or more strings.  

We also support Chinese(or any UTF-8) string 


Install
-------

To install, simply do ``pip install nlpc`` to pull down the latest version from [PyPI](https://pypi.org/project/nlpc/).


Python code example
-------------------

```python
import nlpc

#  finding the longest common subsequence length of string A and string B
A = 'We are shannonai'
B = 'We like shannonai'
nlpc.lcs(A, B)
"""
>>> nlpc.lcs(A, B)
14
"""

#  finding the longest common subsequence length of string A and a list of string B
A = 'We are shannonai'
B = ['We like shannonai', 'We work in shannonai', 'We are not shannonai']
nlpc.lcs_of_list(A, B)
"""
>>> nlpc.lcs_of_list(A, B)
[14, 14, 16]
"""

# finding the longest common substring length of string A and string B
A = 'We are shannonai'
B = 'We like shannonai'
nlpc.lcs2(A, B)
"""
>>> nlpc.lcs2(A, B)
11
"""

#  finding the longest common substring length of string A and a list of string B
A = 'We are shannonai'
B = ['We like shannonai', 'We work in shannonai', 'We are not shannonai']
nlpc.lcs2_of_list(A, B)
"""
>>> nlpc.lcs2_of_list(A, B)
[11, 10, 10]
"""

