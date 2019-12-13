'''
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, t
here may exist one celebrity. The definition of a celebrity is that all the other n - 1 people 
know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. 
The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" 
to get information of whether A knows B. You need to find out the celebrity 
(or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. 
Implement a function int findCelebrity(n). There will be exactly one celebrity 
if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. 
If there is no celebrity, return -1.
'''

#data = [[1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,1,1,1,0,0,1,0,1,0,0,1,1,0,1,1,1,0,0,1,1,0,0,0,1,1,1,1,1,1,0,0],[1,1,0,0,1,1,0,0,0,0,1,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,1,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,1,1,1,0,0,1,1,0,1],[0,0,1,0,1,1,0,0,1,0,1,0,0,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,1,0,0,0,0,1,1,0,1,0,1,0,1,0,0,0,1,1,1,0],[0,0,1,1,1,0,1,1,0,1,1,1,1,0,1,0,1,1,0,1,0,1,1,1,0,1,0,1,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1],[1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0,0,1,1,1,0,1,0,1,0,1,0,1,1],[1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,0,1,0,0,1,1,0,0,1,0,0,1,0,1,1,1,1,0,0,1,0,0,0,0,1,0,1,0],[0,0,1,1,1,1,1,0,0,1,1,0,1,0,1,0,0,1,0,1,0,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,0,0,0,1,0,0,1,1,1,0,1,0,0,1,1,1],[0,0,1,1,1,0,0,1,1,1,0,0,1,0,1,0,0,0,1,1,1,0,1,1,0,1,0,0,0,0,0,1,1,0,0,1,0,1,1,0,1,1,0,0,1,0,0,1,0,1,0,0],[1,1,1,1,0,0,0,1,1,1,0,0,0,0,1,0,0,0,1,1,0,0,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,1,0,0,0],[0,0,1,1,1,0,0,1,1,1,0,0,0,1,0,1,1,1,1,0,1,1,1,1,1,0,0,1,0,0,1,0,1,1,1,1,1,0,0,1,0,0,0,0,1,0,1,0,0,1,0,0],[0,1,1,0,0,0,0,1,1,0,1,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,0,1,1,1],[1,1,1,0,1,0,1,1,0,0,1,1,1,1,1,1,1,0,1,0,1,1,0,0,1,1,0,1,0,0,1,1,1,0,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,0],[0,0,1,1,0,0,0,1,0,0,1,1,1,1,0,1,1,0,1,1,1,0,0,1,1,1,0,1,1,1,0,0,1,1,0,0,0,0,0,1,1,0,1,1,0,0,1,1,0,0,0,1],[0,0,1,0,0,0,1,1,0,0,1,1,1,1,1,0,0,0,0,1,1,0,1,0,1,0,1,0,1,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,1,0,0,1,0,0,0,1,1,0,1,1,0,0,0,1,0,0,0,1,1,1,0,1,0,1,0,1,1,1,1,0,0,0,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0],[0,1,0,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,0,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,1,0,0,1,1,0,1,0,0,1,1,0,0],[1,0,1,0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,1,0],[1,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0,0,1,0,1,1],[0,0,0,0,0,0,0,1,1,0,0,0,1,1,0,1,0,0,1,0,0,1,1,0,0,0,0,0,0,1,0,1,1,0,1,1,0,0,1,0,1,1,1,0,0,1,1,1,0,1,0,0],[1,0,1,1,1,0,0,1,1,0,0,1,1,0,1,1,1,1,0,1,0,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,1,0,0,0,0,1,1,1,0,0,0,1,0,1,0],[1,0,1,0,0,0,0,1,0,0,1,1,0,1,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,1,1,1,0,1],[0,0,1,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,1,1,1,1,1,0,1,0,1,0,0,1,0,0,1,1,0,1,1,1,0,1,1,1,1,1],[1,0,1,1,1,0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0,1,0,1,1,0,0,0,1,1,1,0,0,0,1,0,0,1,1,1,0,0,0,1,1,0,1,1],[0,0,0,1,0,0,0,1,1,1,1,1,0,0,1,1,1,0,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,0,1,1,0,0,1,1,0,0,0,0,1,0,0,0,0],[1,1,1,0,1,1,0,0,0,1,1,1,1,1,1,1,0,1,0,0,0,0,1,1,1,0,1,0,0,1,0,1,1,0,1,0,1,0,0,1,1,0,1,1,0,1,0,0,0,0,1,1],[0,0,1,0,0,1,1,1,1,0,0,0,1,1,1,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0],[0,1,0,0,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,1,0,0,0,0,0,1,1,1,1,0,1,0],[1,1,0,1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,1,0,1,1,0,0,1,1,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1,1,1,0,0,1],[0,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,1,0,0,0,1,1,0,0,1,1,0,1,0,1,1,0,1,1,0,0,0,1,0,1],[0,1,0,0,0,0,0,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1,0,0,0,0,1,1,1,1,0,1,1,1,1,0,0,0,1,0,1,1,1,1,1,0,1,0,0,0,0],[0,1,0,1,1,0,1,0,1,0,0,1,0,0,1,1,0,1,1,1,0,0,1,0,1,1,0,0,1,0,1,1,1,0,0,1,0,1,1,1,0,1,1,1,0,0,1,0,0,1,0,0],[0,1,0,1,0,0,1,1,1,0,0,0,0,0,1,0,0,1,0,0,1,1,0,0,1,0,1,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,1,1,0,1,0,0,1,0,1,0,1,1,1,1,0,1,0,0,0,0,1,0,1,1,0,0,1,1,1,0,0,1,1,0,0,1,1,0,0,0,0,1,1,0,0,1,1],[0,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,0,1,0,0,1,0,0,1,1,1,1],[1,1,0,1,1,1,1,0,1,0,1,1,0,0,1,1,0,0,1,0,1,0,0,1,1,1,1,0,1,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,0,1,1,0,1,1,1,1],[1,1,0,1,1,1,0,0,1,1,0,1,1,1,0,0,1,0,0,0,1,0,0,0,1,1,0,1,1,0,1,0,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,1],[0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,1,1,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,0,0,1,0,1,0,1,0,1,0,0,1,1,0,0,1,1,0,0],[1,1,0,1,0,1,0,1,1,1,1,1,1,0,0,1,1,1,0,0,1,1,0,1,0,1,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0,1,0,0,0,1,1,1,0,0,0,1],[0,0,0,0,0,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,1,0,1,1,1,1,1,0,1,0,1,1,0,1,0],[1,0,0,0,1,1,0,0,0,0,1,0,0,1,1,1,0,1,0,0,0,0,1,1,0,0,1,1,1,0,1,1,1,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0],[1,1,1,0,1,0,1,1,1,1,0,1,0,0,0,0,1,1,1,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1,1,1,0,0,1,1,1,1,0,1,1,0,0,1,0,1],[0,1,0,1,1,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,1,0,1,1,0,0,1,0,1,0,0,1,1,0,1,1,0,1,0,1,1,1,0,0,1,1,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,1,1,0,0,1,0,0,0,1,1,0,0,1,0,0,0,1,0,1,1,0,0,1,1,0,1,0,1],[1,0,0,0,1,1,0,0,1,1,0,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1,1,0,1,1,0,0,1,1,0,0],[0,0,0,0,1,0,0,0,1,1,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,0,0,1,1,1,1,0,1,0,0,1,0,0,1,0,1,0,1,1,0,1,0,0,0,1],[1,1,0,1,0,0,1,0,0,1,1,1,1,0,1,0,0,1,1,1,0,1,1,1,0,0,1,0,0,1,1,0,1,0,1,1,0,1,0,0,1,1,1,1,0,0,1,0,1,1,1,0],[1,1,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,0,0,1,1,0,1,0,1,1,1],[0,1,0,1,1,0,0,0,1,1,1,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,1,1,0,1,0,0,1,1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,0,0,1],[1,0,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,1,1,0,1,0,1,0,0,0,1,1,0,0,1,0,1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,0,0,1,1,1],[0,1,0,0,0,0,0,0,0,1,1,0,1,0,0,1,1,1,1,0,1,0,0,1,1,0,0,0,0,1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,1,0],[0,0,0,0,1,0,0,0,1,0,0,1,1,0,1,1,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,1,0,1,1,1,1,1,1,1,0,1,1,0,0,1,1,1]]
data = [[1,1,1,1,1,1,1,1,0,0,1,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0,0,0,1,1,1,0,0,1,1,0,0,0,0,0,1,0,0,1,0,1,1,0,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0],[1,1,1,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,1,1,1,0,1,0,1,1,0,0,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1],[1,0,1,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,1,1,1,1,0,1,1,0,1,0,1,0,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,1,0,0,0,1,1,0],[1,0,0,1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,0,1,1,1,1,1,0,0,1,0,1,0,1,0,0,0,0,1,1,1,1,0,0,0,1,0,1],[1,1,0,0,1,0,0,0,0,1,0,1,1,0,0,0,0,1,1,0,1,0,0,0,1,0,1,0,0,1,1,0,1,1,1,1,1,1,1,0,1,0,0,1,0,0,0,0,1,1,1,1,1,0,1,0,0,1,1,0,0,0,0,0],[0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,1,0,1,1,0,1],[0,1,0,0,0,0,1,1,0,1,1,1,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,1,0,0,0,0,1,0,1,1,1,1,0,0,0,1,1,0,0,1,1,1,0,1,1,0,0,1,1,0,0,1,1,0,0],[0,0,0,0,1,0,1,1,1,0,0,1,1,0,1,1,1,0,0,1,0,0,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,1,1,0,0,0,1,1,1,1,0,1,1,0,1],[0,1,0,1,0,0,1,1,1,0,1,1,1,1,0,1,0,0,0,1,0,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,0,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,0,1,1,1,1],[0,0,1,1,1,1,0,1,0,1,0,0,0,0,1,0,1,1,0,1,1,1,0,0,1,0,0,1,0,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,0,1,0,1,0,0,1],[1,1,1,0,1,1,1,0,0,1,1,0,0,0,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,1,0,1,0,0,1,0,0,1,1,1,0,1,1,1,1,0,1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,1],[1,1,0,1,0,1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,1,0,0,1,1,0,1,0,0,0,0,0,0,1],[1,1,1,0,0,0,0,1,0,1,0,1,1,1,1,1,0,1,0,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,0,1,0,1,0,0,1,1,0,1,0,1,0,0,0,0,1,0,0,1,1,0,0,0,1,1],[0,1,1,1,0,1,0,0,1,1,0,1,0,1,1,1,1,1,0,0,1,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,1,0,1,1,1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,1],[0,1,0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,1,1,0,0,1,1,0,1,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1],[0,1,0,1,0,1,1,0,1,0,1,1,0,0,1,1,0,0,1,1,1,1,0,1,1,1,0,0,1,0,1,0,1,0,0,0,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,1,0,1,0,1,0,1,1],[0,1,1,0,0,1,0,0,0,1,0,1,1,1,0,1,1,0,1,0,1,0,0,1,0,1,0,0,0,0,1,1,0,0,1,1,1,1,0,1,1,1,0,0,0,0,1,1,0,0,1,0,1,0,0,1,1,1,1,0,1,1,1,0],[0,0,1,1,0,0,1,0,0,0,0,1,1,1,1,1,0,1,1,0,1,0,0,1,0,1,1,1,1,0,1,0,1,1,0,1,1,1,0,1,1,0,0,1,1,0,0,1,1,0,1,1,1,0,1,1,0,0,0,0,1,1,1,1],[0,1,0,0,0,0,1,0,0,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,0,1,1,0,1,0,0,1,0,0,0,1,0,1,1,1,1,1,0,0,1,1,0,0,1,1],[1,1,0,1,1,1,1,1,0,1,0,0,1,0,0,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,1,0,1,0,0,1,1,1,1,1,1,0,0,1],[1,1,0,1,1,1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1,0,1,0,0,1,1,1,1,0,0,0,0,0,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,0,1,1,1,1,1],[1,0,1,1,1,0,0,0,0,1,1,0,0,1,0,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1,1,0,1],[0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,1,1,1,0,1,0,0,1,0,1,0,1,1,1,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,0,1,1,1,1],[0,0,0,0,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1],[0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,1,0,1,0,1,1,1,0,0,1,1,1,0,0,0,1,1,0,0,1,1,1,0,0,1,1,0,1,1,1,0,1,0,0,1,0],[1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,0,0,1,1,0,0,0,0,1,1,1,0,0,0,0,1,1,0,1,1,1,0,0,1,0,1,0,1,1,1,0,1,1,0,0,1,1,0,1,1,0,0,0,0,0,0,0,1,1],[1,0,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,1,0,0,1,1,0,0,1,1,1,0,0,0,1,1,0,0,1,0,1,1,1,0,0,1,0,0,1,0,1,0,1,0,1,1,0,1,0],[0,1,0,1,0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,0,1,0,0,1,0,0,0,0,0,1,1,1,0,0,0,0,1,1,0,1,1,1,1,0,1,0,0,1,1,0,0,1],[0,0,1,1,1,0,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,0,0,1,0,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,0,0,1,0,1,0,0,1,0,1,0,0],[1,1,0,0,0,1,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,1,1,0,0,1,1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,1,0,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,1,1,1,0,0,1,1,0,1,0,1,1,0,0,0,0,1,0,1,1,0,1,0,1,1,1,1,1,0,0,1,1,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,0,0,1,0],[0,0,0,0,1,1,0,0,1,0,1,1,1,1,0,1,0,1,1,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0],[0,0,0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,0,0,1,1,0,1,1,0,1,1,1,0,1,0,0,0,1,0,1,0,1,0,1,1,0,0,1,0,0,1,1,1,1,0,0,0,1],[1,1,1,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,1,1,1,1,0,0,1,0,1,0,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,1,1,1,1],[0,0,1,1,1,1,0,1,0,0,1,0,0,1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,0,1,0,1,0,0,0,1,0,0,1,1,0,1,0,0,0,0,1,1,0,0,1,0,1,0,1,1,1,0,1,0],[1,1,0,0,0,1,0,0,0,1,0,0,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,1,0,1,1,0,1,1,1,0,1],[0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,0,0,1,0,0,0,1,0,0,1,0,1,0,1,1,1,1,0,0,0,0,0,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,0,0,1,0,0,1,0,0,0,1,1,1],[0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,1,0,1,1,0,0,1,0,0,1,0,0,1,0,1,0,1,1,1,1,0,0,0,1,1,0,1,1,1,1,1,0,0,1,1,0,0,1,0,1,1,0,0],[1,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,1,0,1,1,0,0,1,1,0,1,1,0,0,1,1,0,0,0,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1,0,0,0,1,0,1,0,1,1,1],[0,1,1,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,1,0,0,0,1,0,1,1,0,1,0,1,1,1,0,1,1,0,1,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0],[0,0,1,1,0,1,0,1,1,1,0,1,0,0,0,1,1,0,0,1,0,1,0,1,0,0,1,1,1,0,1,1,1,1,1,1,0,0,0,1,0,1,0,1,0,0,0,0,1,0,0,0,0,1,1,1,0,0,1,1,1,0,0,1],[1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,1,0,0,1,1,0,1,1,0,1,0,0,0,1,1,0,1,1,1,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0],[0,0,1,1,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,0,1,1,0,0,0,1,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,1,0,0,1,0,1,0,0,1,1,0,0,1,1,1,0,0,0,1,1],[0,1,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,1,0,0,1,1,1,1,1,0,1,1,0,0,1,1,0,0,1,1,0,0,1,0,0,1,1,0,1,0,1,1,0,1,0,1,0,1,0,1,1,1],[0,1,0,0,1,1,0,1,0,1,1,1,1,0,1,1,1,1,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0],[0,1,1,0,0,0,0,1,1,1,1,0,1,0,1,0,0,0,1,0,1,1,1,1,0,1,0,0,0,1,1,1,0,0,1,1,1,0,1,1,0,0,1,1,1,0,1,0,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0],[1,1,1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,0,1,0,1,0,1,1,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,0,1],[1,1,1,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,0,0,1,1,0],[0,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1],[1,0,0,0,1,1,0,1,0,0,0,0,1,1,0,0,1,1,0,1,0,1,1,0,1,0,1,0,0,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,0,1,0,0,1,0,1,1,1,0,0,0,1,1,0,0,1,1,1,0],[0,0,0,1,1,0,0,1,1,0,0,1,0,0,0,0,1,1,0,1,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,1,1,1,0,1,0,1,1,0,1,1,0,0],[0,1,0,0,0,0,1,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,1,1,0,1,0,0,0,1,1,1,0,1,1,1,1,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,1,1,0,0,1,1,0,1,0,0,0,1],[0,0,1,0,1,1,0,1,0,1,0,1,1,1,1,1,1,1,0,0,1,1,1,0,0,1,1,0,0,0,1,1,0,0,1,0,1,1,1,0,1,0,1,1,0,0,1,1,1,1,1,1,0,1,0,1,1,0,0,0,1,0,0,0],[0,1,1,0,0,1,1,1,1,1,1,0,1,0,0,0,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,1,0,1,1,0,1,0],[1,1,0,0,0,1,1,1,1,0,1,0,1,0,1,1,0,0,1,0,1,1,0,0,0,1,1,0,0,1,1,0,1,1,0,0,0,1,1,0,0,1,0,0,0,1,0,0,1,0,0,1,1,0,1,1,1,0,1,1,0,1,0,0],[0,1,0,0,0,1,0,1,1,0,0,0,0,0,0,0,1,0,1,0,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,0,1,1,1,0,1,1,1,1,1,0,0,0,1,0,1,1,0,1,0,1,1,0,0,0,1,0,0,1],[1,1,1,1,1,0,1,0,0,1,1,1,0,1,0,0,1,0,0,1,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,1,1,0,0,1,0,1,0,0,1,1,0,1,0,1,1,1,1,0,0,1,1,0],[0,1,0,0,1,0,0,0,0,0,1,1,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,0,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,0,1],[1,0,0,0,1,0,0,1,1,0,1,0,1,1,1,0,0,0,0,0,1,0,1,1,1,0,1,1,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,0,1,1,1,1,1,0,0,0,1],[1,0,1,0,0,1,0,1,1,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1,0,1,1,1,0,1,1,1,0,1,1,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,1,0],[1,0,1,0,0,1,0,1,0,1,0,0,1,1,0,0,0,0,0,0,1,0,0,0,1,0,0,1,1,0,1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,0,0,0,1,0,1],[0,1,1,1,0,1,1,0,0,0,1,1,1,1,1,0,1,1,0,0,1,1,0,1,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],[1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,0,1,0,0,0,0,1,1,1,0,0,0,1,1,0,1,0,0,0,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,0,1,1,0,1,0,1]]
#data = [[1,0],[0,1]]

print(len(data))

# The knows API is already defined for you.
# return a bool, whether a knows b
counter = 0
def knows(a: int, b: int) -> bool:
    global counter
    counter += 1
    if data[a][b] == 1:
        return True
    else:
        return False

class Solution2:
    '''O(N^2) solution that is accepted.
        counter = 249
    '''

    def confirm(self, can, n):
        for i in range(n):
            if i != can and knows(can, i):
                return -1
        for i in range(n):
            if i != can and knows(i, can) is False:
                return -1
        return can
    
    def count(self, celeberty):
        cels = []
        for i, val in enumerate(celeberty):
            if val == 1:
                cels.append(i)
        return cels

    def findCelebrity(self, n: int) -> int:
        celeberty = [1 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if celeberty[i] == 0 and celeberty[j] == 0:
                    continue
                if knows(i, j) is False:
                    celeberty[j] = 0
                else:
                    celeberty[i] = 0
            cels = self.count(celeberty)
            if len(cels) == 0:
                return -1
            elif len(cels) == 1:
                return self.confirm(cels[0], n)
        return -1



class Solution:
    '''A O(N) solution, the idea is to avoid the adjacent matrix and find the cand in ONE pass !!!
        counter = 156
    '''
    def findCelebrity(self, n: int) -> int:
        cand = 0
        for i in range(1, n):
            if knows(cand, i):  # if cand knows i, then cand must not be the celeberty, but i possible can
                cand = i
        # till now, if there is celeberty, then it must be cand. 
        # from above, we alreadyknow that cand does not know people after him (higher index people)
        # now lets further check cand.
        for i in range(0, cand):
            if knows(cand, i):
                return -1
            if knows(i, cand) is False:
                return -1
        
        for i in range(cand + 1, n):
            if knows(i, cand) is False:
                return -1
        # now the cand passed all the checking
        return cand


def test():
    s = Solution2()
    print('celeberty:', s.findCelebrity(64))
    print('counter:  ', counter)

if __name__ == '__main__':
    test()