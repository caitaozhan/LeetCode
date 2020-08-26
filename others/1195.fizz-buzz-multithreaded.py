#
# @lc app=leetcode id=1195 lang=python3
#
# [1195] Fizz Buzz Multithreaded
#
# https://leetcode.com/problems/fizz-buzz-multithreaded/description/
#
# concurrency
# Medium (67.47%)
# Likes:    164
# Dislikes: 97
# Total Accepted:    11.4K
# Total Submissions: 16.6K
# Testcase Example:  '15'
#
# Write a program that outputs the string representation of numbers from 1 to
# n, however:
# 
# 
# If the number is divisible by 3, output "fizz".
# If the number is divisible by 5, output "buzz".
# If the number is divisible by both 3 and 5, output "fizzbuzz".
# 
# 
# For example, for n = 15, we output: 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz,
# buzz, 11, fizz, 13, 14, fizzbuzz.
# 
# Suppose you are given the following code:
# 
# 
# class FizzBuzz {
# public FizzBuzz(int n) { ... }               // constructor
# ⁠ public void fizz(printFizz) { ... }          // only output "fizz"
# ⁠ public void buzz(printBuzz) { ... }          // only output "buzz"
# ⁠ public void fizzbuzz(printFizzBuzz) { ... }  // only output "fizzbuzz"
# ⁠ public void number(printNumber) { ... }      // only output the numbers
# }
# 
# Implement a multithreaded version of FizzBuzz with four threads. The same
# instance of FizzBuzz will be passed to four different threads:
# 
# 
# Thread A will call fizz() to check for divisibility of 3 and outputs
# fizz.
# Thread B will call buzz() to check for divisibility of 5 and outputs
# buzz.
# Thread C will call fizzbuzz() to check for divisibility of 3 and 5 and
# outputs fizzbuzz.
# Thread D will call number() which should only output the numbers.
# 
# 
#


# @lc code=start

import threading

class FizzBuzz:
    '''this is essentially a single thread task, but manually changing it into a multithread task
       four threads running concurrently. only one thread can print at a single moment (or else printing random stuff)
    '''
    def __init__(self, n: int):
        self.n = n
        self.done = False
        self.f_lock = threading.Lock()
        self.b_lock = threading.Lock()
        self.fb_lock = threading.Lock()
        self.main = threading.Lock()
        self.f_lock.acquire()    # at the beginning, only the number thread (acting as the main thread here) is not blocked
        self.b_lock.acquire()
        self.fb_lock.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.f_lock.acquire()
            if self.done:
                return
            printFizz()
            self.main.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.b_lock.acquire()
            if self.done:
                return
            printBuzz()
            self.main.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fb_lock.acquire()
            if self.done:
                return
            printFizzBuzz()
            self.main.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            self.main.acquire()
            if i % 15 == 0:
                self.fb_lock.release()
            elif i % 3 == 0:
                self.f_lock.release()
            elif i % 5 == 0:
                self.b_lock.release()
            else:
                printNumber(i)
                self.main.release()

        self.main.acquire()        # if this line removed, then runtime error or TLE, WHY?
        self.done = True           # Because need to block before the previous print is finished, wait for the self.main to be released
        self.f_lock.release()
        self.b_lock.release()
        self.fb_lock.release()


def test():
    l = threading.Lock()
    while True:
        l.acquire()
        print('hello')

test()

# @lc code=end

