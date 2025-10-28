from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator, NumberValidator
from InquirerPy.base.control import Choice

class ReadmeContent:
  def __init__(self, title="", description="", installation_instructions="", usage_information="", licence="Proprietary", author_first_name="", author_last_name="", email_address="@", telephone_number="0", linkedin_url=""):
    self.title = title
    self.description = description
    self.installation_instructions = installation_instructions
    self.usage_information = usage_information
    self.licence = licence
    self.author_first_name = author_first_name
    self.author_last_name = author_last_name
    self.email_address = email_address
    self.telephone_number = telephone_number
    self.linkedin_url = linkedin_url

def content_input():
    title = inquirer.text(message="Enter project title:").execute()
    description = inquirer.text(message="Enter project description:").execute()
    installation_instructions = get_instructions()
    usage_information = inquirer.text(message="Enter usage information:").execute()
    licence = inquirer.select(message="Select a licence:",
        choices=[
            Choice("Open Source"),
            Choice("Proprietary"),
            Choice("Public Domain")
        ],
        multiselect=False                             
        ).execute()
    author_first_name = inquirer.text(message="Enter your first name:", validate = EmptyInputValidator(), invalid_message = "First name cannot be empty.").execute()
    author_last_name = inquirer.text(message="Enter your last name:", validate = EmptyInputValidator(), invalid_message = "Last name cannot be empty.").execute()
    email_address = inquirer.text(message="Enter your email address:", validate=(lambda text: (True if "@" in text else False)), invalid_message="Please enter a valid email address.").execute()
    telephone_number = inquirer.text(message="Enter your telephone number:", validate=NumberValidator(float_allowed = False), invalid_message = "Please input an integer without spaces.").execute()
    linkedin_url = inquirer.text(message="Enter your LinkedIn url:").execute()

    return ReadmeContent(title, description, installation_instructions, usage_information, licence, author_first_name, author_last_name, email_address, telephone_number, linkedin_url)

def get_instructions():
        instructions = []
        while True:
            instruction = inquirer.text(message="Enter installation instructions next step (or 'n' for no more steps):").execute()
            print(instruction)
            if ((instruction == "n") or (instruction == "N")):
                return instructions
            instructions.append(instruction)