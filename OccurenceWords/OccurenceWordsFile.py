# fp = open("words.txt", "w")
# words = input("Enter a sentence: ")
# fp.write(words)
# fp.close()
# fp = open("words.txt", "r")
# str=list(fp.read().split())
# str1=list(set(str))
# for word in str1:
#     print(word," : ",str.count(word))
# fp.close()
with open("words.txt", "w") as fp:
    words = input("Enter a sentence: ")
    fp.write(words)
with open("words.txt", "r") as fp:
    word_list = list(fp.read().split())
    word_counts = {word: word_list.count(word) for word in set(word_list)}
for word, count in word_counts.items():
    print(word, ":", count)