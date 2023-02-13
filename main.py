s = "Let's take LeetCode contest"
combo = s.split(" ")
for index, strings in enumerate(combo):
    helper = strings[::-1]
    combo[index] = helper
s = " ".join(combo)
print(s)