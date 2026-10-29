import json

result = {
    "prompt": "Explain AI",
    "status": "Accepted",
    "character_count": 10
}

with open("prompt_checking", "w", encoding="utf-8") as file:
 json.dump(result,file,indent=4)

print("prompt history saved")