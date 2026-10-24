def analyze_prompt(prompt):
    character_count = len(prompt.strip())

    if not prompt.strip():
        return "Empty prompt"
    elif character_count < 5 :
        return "Too short"
    elif character_count > 10:
        return "too long"
    else:
        return "Accepted"

prompts = ["", "machine_learning", "books", "laptops"]

accepted_count = 0
rejected_count = accepted_count < 0

for prompt in prompts:
    result = analyze_prompt(prompt)
    print(f"Prompt: '{prompt}' - Result: {result}")

    if result == "Accepted":
        accepted_count += 1
print("\n Total prompts: ", len(prompts))
print("Accepted_caounts: ", accepted_count)
print("Rejected_count", rejected_count)