from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator
from InquirerPy.base.control import Choice

def main() -> None:

    title = inquirer.text(message="Enter project title:").execute()
    description = inquirer.text(message="Enter project description:").execute()
    installation_instructions = inquirer.text(message="Enter installation instructions:").execute()
    usage_information = inquirer.text(message="Enter usage information:").execute()
    licence = inquirer.select(message="Select a licence:",
        choices=[
            Choice("Open"),
            Choice("Closed"),
        ],
        multiselect=False                             
        ).execute()
    print(title)

if __name__ == "__main__":
    main()
