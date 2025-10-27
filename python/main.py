from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator, NumberValidator
from InquirerPy.base.control import Choice
from readme_generation import create_readme
from content import content_input

def main():    
    new_readme_content = content_input()
    readme_markdown = create_readme(new_readme_content)
    with open("README.md", "w") as f:
        f.write(readme_markdown)
    print(readme_markdown)
    
if __name__ == "__main__":
    main()






