sent="This is a sentence"
# print(len(list(map(str,sent.split(" ")))))
count=1
for i in sent:
    if i==" ":
        count+=1
print(count)