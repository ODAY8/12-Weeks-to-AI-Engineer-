prompt = input("Enter the prompt: ")

charcater_count = len(prompt)
words_count = len(prompt.strip())


print("\n--- the prompt ai analyzer is ")
print("your charcater count is: ", charcater_count)
print("words_count: ", words_count)

if not prompt.strip():
    print("prompt rejected its empty")
elif charcater_count > 5:
       print("prompt rejected its reached the limit")
else:
    print("prompt accepted")