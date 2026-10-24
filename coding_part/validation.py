prompt = input("Enter prompt: ")

character = len(prompt)

if not prompt.strip():
    print("prompt accepted")
    
elif character < 5:
    print("prompt rejected its not enough characters", character)
elif character > 10:
    print("prompt rejected its reached the limit", character)
elif prompt == "Hello":
    print("Welcome to AI engineering!")

else:
    print("prompt accepted")
  