with open("story.txt", "r") as f:
  story = f.read()

words = set()
# "-1" Means we have not found the beginning of the word
start_of_word = -1

print(f"Choose the words to complete this story: \n{story}")

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
  if char == target_start:
    start_of_word = i

  if char == target_end and start_of_word != -1:
    # for the end in the slicing takes into account current index by "i+1"
    word = story[start_of_word: i + 1]
    words.add(word)
    start_of_word = -1

answers = {}

for word in words:
  answer = input("Enter a word for " + word + ": ")
  answers[word] = answer

for word in words:
  story = story.replace(word, answers[word])

print(story)
