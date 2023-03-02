"""
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is.

When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position.

Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.

Given the secret number 'secret' and your friend's guess 'guess', return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows.

Note that both secret and guess may contain duplicate digits.
"""
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        frequency = {}
        position = []
        for char in secret:
            frequency[char] = 1 + frequency.get(char,0)
            position.append(char)
        correct_pos = wrong_pos = 0
        another_str = ""
        for index, char in enumerate(guess):
            if position[index] == char:
                correct_pos += 1
                frequency[char] -= 1
            else:
                another_str += char
        for char in another_str:
            if char in frequency and frequency[char] > 0:
                frequency[char] -= 1
                wrong_pos += 1
        return f"{correct_pos}A{wrong_pos}B"

if __name__=="__main__":
    print(Solution().getHint("1122","1222"))