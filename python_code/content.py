from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator, NumberValidator
from InquirerPy.base.control import Choice
""" InquirerPy is a module that facilitates content input. It is compatible with Python 3.14.
    Choice class generates a dropdown for licence.
"""


#README CONTENT CLASS

class ReadmeContent:
  def __init__(self, title="", description="", installation_instructions="", usage_information="", licence="", author_first_name="", author_last_name="", email_address="", telephone_number="", linkedin_url=""):
    """ Creates a readme content object, containing the input content required by a readme file, as attributes.

        Args:
            title(str): the title of the project
            description(str): a description of the project
            installation_instructions(str): how to set up and run the project
            usage_information(str): more details of the functionality in action
            licence(str): proffered licence for use (optional)
            author_first_name(str): first name of author
            author_last_name(str): last name of author
            email_address(str): email address of author
            telephone_number(int): telephone number of author
            linkedin_url(str): linkedin url of author

        Returns:
            object of type ReadmeContent

    """
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

#TOP-LEVEL FUNCTION FOR CONTENT MODULE




def content_input():
    """ Creates a readme content object, containing the input content required by a readme file.
        Gathers information from the user, via the terminal, in order to achieve this.
        Required inputs are title and description, email_address and telephone_number. Other inputs are optional.
        
        Args: (None)

        Returns:
            (object): object of type ReadmeContent

        Raises:
            required input empty raises error
            non-empty email_address not containing "@" raises error
            non-empty telephone_number that is not an integer raises error

    """
    title = inquirer.text(message="Enter project title:", validate = EmptyInputValidator()).execute()
    description = inquirer.text(message="Enter project description:", validate = EmptyInputValidator()).execute()
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
    author_first_name = inquirer.text(message="Enter your first name:").execute()
    author_last_name = inquirer.text(message="Enter your last name:").execute()
    email_address = inquirer.text(message="Enter your email address:", validate = (lambda text: (True if ("@" in text) else False)), invalid_message="Please enter a valid email address.").execute()
    telephone_number = inquirer.text(message="Enter your telephone number:", validate = NumberValidator(float_allowed = False), invalid_message = "Please input an integer without spaces.").execute()
    linkedin_url = inquirer.text(message="Enter your LinkedIn url:").execute()

    return ReadmeContent(title, description, installation_instructions, usage_information, licence, author_first_name, author_last_name, email_address, telephone_number, linkedin_url)

#HELPER FUNCTION FOR content_input

def get_instructions():
    """ Creates a sequential list of installation instructions for the project, which are input from the user. An empty instruction from the user signals the end of the list.

        Args: (None)

        Returns:
            (list) List of installation instructions

    """
    instructions = []
    while True:
        instruction = inquirer.text(message="Enter installation instructions next step (or just press 'enter' for no more steps):").execute()
        if (instruction == ""):
            return instructions
        instructions.append(instruction)