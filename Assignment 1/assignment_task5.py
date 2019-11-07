word = input("Input a word to reverse: ")
word2 = input("Input a word to reverse: ")
for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")
for char in range(len(word2) - 1, -1, -1):
  print(word2[char], end="")
print("\n")



