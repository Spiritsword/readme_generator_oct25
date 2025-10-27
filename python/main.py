from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator, NumberValidator
from InquirerPy.base.control import Choice
import re

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
    author_first_name = inquirer.text(message="Enter your first name:", validate = EmptyInputValidator(), invalid_message = "First name cannot be empty.").execute()
    author_last_name = inquirer.text(message="Enter your last name:", validate = EmptyInputValidator(), invalid_message = "Last name cannot be empty.").execute()
    email = inquirer.text(message="Enter your email address:", validate=(lambda text: (True if "@" in text else False)), invalid_message="Please enter a valid email address.").execute()
    tel = inquirer.text(message="Enter your telephone number:", validate=NumberValidator(float_allowed = False), invalid_message = "Please input an integer without spaces.").execute()
    LinkedIn = inquirer.text(message="Enter your LinkedIn url:").execute()

    print(title)

if __name__ == "__main__":
    main()
