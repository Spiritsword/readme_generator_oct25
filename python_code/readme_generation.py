#TOP-LEVEL README GENERATOR

def create_readme(readme_content):
    """ Creates a formatted readme file from a readme_content object.
    
        Args: readme_content object

        Returns:
            (str): Github-compatible readme text markdown file content

    """
    content_tuple = (make_string_title(readme_content.title),
                    make_string_description(readme_content.description),
                    make_string_installation_instructions(readme_content.installation_instructions),
                    make_string_usage_information(readme_content.usage_information),
                    make_string_licence(readme_content.licence),
                    make_string_author(readme_content.author_first_name, readme_content.author_last_name),
                    make_string_hr(),
                    make_string_email_address(readme_content.email_address),
                    make_string_telephone_number(readme_content.telephone_number),
                    make_string_linkedin_url(readme_content.linkedin_url)
                    )
    final_string = "".join(content_tuple)
    print(final_string)
    return final_string

#HELPERS FOR GENERATING README (GENERAL)
    
def make_string_base_section(heading, content, size="large"):
    """ Creates a string that represents the formatted heading and content of a section of the readme.
    
        Args:
            heading(str): section heading
            content(str): section content
            size(str): 'large' or 'small' heading size indicator (defaults to 'large')          

        Returns:
            (str): formatted heading and content of a section as a single string

    """
    if (content == ""):
        return ""
    return_string = f'\n ##{"" if size == "large" else "#"} {heading} \n {content} \n '
    print(return_string)
    return return_string

def make_string_para(para):
    """ Creates a string that represents a formatted paragraph (for a section without a title).
    
        Args:
            para(str): the content of the paragraph     

        Returns:
            (str): formatted paragraph

    """
    if (para == ""):
        return ""
    return f'{para} \n'

def make_string_hr():
    """ Creates a horizontal rule.
    
        Args: (None)        

        Returns:
            (str): string instructing creation a horizontal rule

    """
    return (f'\n *** \n ')

#HELPERS FOR GENERATING README (PARTICULAR SECTIONS)

def make_string_title(title):
    """ Creates the marked-up title string. 
    
        Args:
            title(str): project title

        Returns:
            (str): marked up project title

    """
    if (title == "n" or title == "N"):
        return ""
    return (f'\n # {title} \n')

def make_string_description(description):
    """ Creates the marked-up project description. 
    
        Args:
            description(str): project description

        Returns:
            (str): marked up project description

    """
    return make_string_para(f'> {description}')

def make_string_installation_instructions(instructions):
    """ Creates the marked-up installation instructions. 
    
        Args:
            instructions(list): project installation instructions as a list

        Returns:
            (str): marked up project installation instructions (including heading)

    """
    formatted_instructions = []
    for i in range (len(instructions)):
        formatted_instructions.append((f' - Step {i+1}: {instructions[i]} \n'))
    return make_string_base_section("Installation Instructions", "".join(formatted_instructions))

def make_string_usage_information(info):
    """ Creates the marked-up usage information. 
    
        Args:
            info(str): project usage information

        Returns:
            (str): marked up project usage information (including heading)

    """
    return make_string_base_section("Usage Information", info)

def make_string_licence(licence):
    """ Creates the marked-up licence. 
    
        Args:
            licence(str): project licence type

        Returns:
            (str): marked up project licence type (including heading)

    """
    return make_string_base_section("Licence", licence)

def make_string_author(first_name, last_name):
    """ Creates the marked-up author name. 
    
        Args:
            first_name(str): author first name
            first_name(str): author last name

        Returns:
            (str): marked up author full name (including heading)

    """
    if ((first_name == "n" or first_name == "N") and (last_name == "n" or last_name == "N")):
        return ""
    return f'\n ## Author \n {first_name} {last_name} \n'

def make_string_email_address(email):
    """ Creates the marked-up contact email address. 
    
        Args:
            email(str): contact email address

        Returns:
            (str): marked up contact email address (including heading)

    """
    return make_string_base_section("Email Address", email, "small")

def make_string_telephone_number(tel):
    """ Creates the marked-up contact telephone number. 
    
        Args:
            tel(str): contact telephone number

        Returns:
            (str): marked up contact telephone number (including heading)

    """
    return make_string_base_section("Telephone Number", tel, "small")

def make_string_linkedin_url(url):
    """ Creates the marked-up author linkedin url. 
    
        Args:
            url(str): author linkedin url

        Returns:
            (str): marked up author linkedin url (including heading)

    """
    link = f'[Profile link]({url})'
    return make_string_base_section("LinkedIn Profile", link, "small")

