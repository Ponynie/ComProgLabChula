word = input("Next word")
concate_word = word
while word != "." :
    word = input("Next word")
    concate_word = concate_word + " " + word
print("Sentence:",concate_word.strip("."))