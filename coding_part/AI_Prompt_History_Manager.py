import json
from pathlib import Path
from datetime import datetime

HISTORY_FILE = Path("prompt_history.json")


# 1. Analyze and validate prompts
def analyze_prompt(prompt):

    character_count = len(prompt.strip())
    word_count = len(prompt.split())

    if not prompt.strip():
        status = "Empty"

    elif character_count < 5:
        status = "Too short"

    elif character_count > 100:
        status = "Too long"

    else:
        status = "Accepted"

    return {
        "prompt": prompt,
        "character_count": character_count,
        "word_count": word_count,
        "status": status,
        "created_at": datetime.now().isoformat()
    }


# 2. Load previous history
def load_history():

    if not HISTORY_FILE.exists():
        return []

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            history = json.load(file)

        if not isinstance(history, list):
            raise ValueError("History must be a list")

        return history

    except (json.JSONDecodeError, ValueError) as error:
        raise RuntimeError(f"Invalid history file: {error}") from error

    except OSError as error:
        raise RuntimeError(f"Could not read history: {error}") from error


# 3. Save history
def save_history(history):

    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as file:
            json.dump(history, file, indent=4)

    except OSError as error:
        print("Error saving history:", error)


# 4. Add a new prompt
def add_prompt(history):

    prompt = input("\nEnter your AI prompt: ")

    result = analyze_prompt(prompt)

    history.append(result)

    save_history(history)

    print("\nPrompt status:", result["status"])
    print("Characters:", result["character_count"])
    print("Words:", result["word_count"])
    print("Prompt saved successfully!")


# 5. View prompt history
def view_history(history):

    if not history:
        print("\nNo prompt history found.")
        return

    print("\n--- PROMPT HISTORY ---")

    for index, record in enumerate(history, start=1):

        print(f"\nPrompt #{index}")
        print("Prompt:", record["prompt"])
        print("Status:", record["status"])
        print("Characters:", record["character_count"])
        print("Words:", record["word_count"])
        print("Created:", record["created_at"])


# 6. Show statistics
def show_summary(history):

    total = len(history)

    accepted = sum(
        1 for record in history
        if record["status"] == "Accepted"
    )

    rejected = total - accepted

    print("\n--- HISTORY SUMMARY ---")
    print("Total prompts:", total)
    print("Accepted prompts:", accepted)
    print("Other prompts:", rejected)


# 7. Clear history
def clear_history(history):

    if not history:
        print("\nHistory is already empty.")
        return

    confirmation = input(
        "Are you sure you want to delete all history? Type YES: "
    )

    if confirmation == "YES":

        history.clear()
        save_history(history)

        print("History cleared!")

    else:
        print("Operation cancelled.")


# 8. Main application
def main():

    try:
        history = load_history()

    except RuntimeError as error:
        print("Error:", error)
        print("Your existing history was not overwritten.")
        return

    print("\n=== AI PROMPT HISTORY MANAGER ===")
    print("Previous records loaded:", len(history))

    while True:

        print("\n--- MENU ---")
        print("1. Add new prompt")
        print("2. View prompt history")
        print("3. Show statistics")
        print("4. Clear history")
        print("5. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":

            add_prompt(history)

        elif choice == "2":

            view_history(history)

        elif choice == "3":

            show_summary(history)

        elif choice == "4":

            clear_history(history)

        elif choice == "5":

            save_history(history)

            print("\nThank you for using AI Prompt Manager!")
            break

        else:

            print("Invalid choice. Please try again.")


# Start application
if __name__ == "__main__":
    main()