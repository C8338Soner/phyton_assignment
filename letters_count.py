sentences = input("Please enter some word or sentences: ")
counter = list(map(sentences.count, sentences))
result = dict(set(zip(data,counter)))
print(result)
