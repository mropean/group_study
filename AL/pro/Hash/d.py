import re
answer = True
phone_book = ["119", "97674223", "1195524421"]
temp = " " + " ".join(phone_book)
for i in phone_book:
    word = " "+ i
    print(word)
    if len(list(re.finditer(word, temp))) > 1:
           answer = False
           break

print(answer)
