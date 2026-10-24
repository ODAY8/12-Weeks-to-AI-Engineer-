def analyze_prompt(prompt):
    character_count = len(prompt.strip())

    if not prompt.strip():
        return "Empty prompt"
    elif character_count < 5:
        return "Too short"
    else:
        return "Accepted"


result = analyze_prompt("Ali")
print(result)