from InquirerPy import prompt

questions = [
    {"type": "input", "message": "What's your name:", "name": "name"},
    {
        "type": "list",
        "message": "What's your favourite programming language:",
        "choices": ["Go", "Python", "Rust", "JavaScript"],
    },
    {"type": "confirm", "message": "Confirm?"},
]

def intake (questions):
    result = prompt(questions)
    name = result["name"]
    fav_lang = result[1]
    confirm = result[2]
    if confirm == False:
        intake (questions)
    print(name)
    print(fav_lang)
    print(confirm)

