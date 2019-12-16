Problem A: Happy and Unhappy Numbers

Several numbers in various states of unhappiness. Image by Sylfida (Shutterstock), Used under license 
It turns out there are such things as happy numbers and unhappy numbers. We’re going to assume that you have been using these
poor little lovable creatures your whole life with absolutely no consideration for their feelings and general well-being. Perhaps
today we can convince you to have some empathy and to stop and think about whether or not your numbers are happy. Who
ever said that a programming competition cannot be a lesson in numerical ethics?

A happy number is a positive integer that, when repeatedly replaced with the sum of the squares of its digits, eventually
reaches the number 1. Alternatively, if this process repeats endlessly, the number is unhappy.
Slightly more formally (taken fromWikipedia), given a positive integer n = n0, define a sequence n0, n1, n2...,
where nj+1 is the sum of the squares of the base-10 digits of nj , for j >= 0. Then n is happy if and only if there exists
i >= 0 such that ni = 1; otherwise, n is unhappy.
If you are still confused, take a look at the process for the number 19, which is happy:

12 + 92 = 82

82 + 22 = 68

62 + 82 = 100

12 + 02 + 02 = 1

Given two positive integers A and B (with A <= B), your challenge is to determine how many happy
numbers there are between A and B (inclusive).

Input:
The first line of input contains a single integer T (1 <= T <= 10 000), the number of test cases. This is
followed by T lines, one per test case. Each test case is specified by two space-separated integers, A and B (1 <= A <= B <= 106).

Output
For each test case, output a single line containing the number of happy numbers between A and B, inclusive. 

Sample Input Sample Output Sample Output, with visualized whitespace are provided in files
