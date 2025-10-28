def create_readme(readme_content):
    content_tuple = (make_string_title(readme_content.title),
                    make_string_description(readme_content.description),
                    make_string_installation_instructions(readme_content.installation_instructions),
                    make_string_usage_information(readme_content.usage_information),
                    make_string_licence(readme_content.licence),
                    make_string_hr(),
                    make_string_author(readme_content.author_first_name, readme_content.author_last_name),
                    make_string_email_address(readme_content.email_address),
                    make_string_telephone_number(readme_content.telephone_number),
                    make_string_linkedin_url(readme_content.linkedin_url)
                    )
    final_string = "".join(content_tuple)
    print(final_string)
    return final_string
    
def make_string_base_section(title, description):
    if (description == "n" or description == "N"):
        return ""
    return_string = f'\n ## {title} \n {description} \n '
    print(return_string)
    return return_string

def make_string_para(para):
    if (para == "n" or para == "N"):
        return ""
    return f'{para} '

def make_string_hr():
    return (f'\n *** \n ')

def make_string_title(title):
    if (title == "n" or title == "N"):
        return ""
    return (f'\n # {title} \n')

def make_string_description(description):
    return make_string_para(f'> description)

def make_string_installation_instructions(instructions):
    formatted_instructions = []
    for i in range (len(instructions)):
        formatted_instructions.append((f'> - Step {i+1}: {instructions[i]} \n'))
    return make_string_base_section("Installation Instructions", "".join(formatted_instructions))

def make_string_usage_information(info):
    return make_string_base_section("Usage Information", info)

def make_string_licence(licence):
    return make_string_base_section("Licence", licence)

def make_string_author(first_name, last_name):
    if ((first_name == "n" or first_name == "N") and (last_name == "n" or last_name == "N")):
        return ""
    return f'\n ## Author \n {first_name} {last_name} \n'

def make_string_email_address(email):
    return make_string_base_section("Email Address", email)

def make_string_telephone_number(tel):
    return make_string_base_section("Telephone Number", tel)

def make_string_linkedin_url(url):
    link = f'[Profile link]({url})'
    return make_string_base_section("LinkedIn Profile", link)

