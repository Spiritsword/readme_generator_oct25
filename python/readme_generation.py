def create_readme(readme_content):
    content_tuple = (str(make_string_title(readme_content.title)),
                     str(make_string_description(readme_content.description)),
                     str(make_string_installation_instructions(readme_content.installation_instructions)),
                     str(make_string_usage_information(readme_content.usage_information)),
                     str(make_string_licence(readme_content.licence)),
                     str(make_string_author(readme_content.author_first_name, readme_content.author_last_name)),
                     str(make_string_email_address(readme_content.email_address)),
                     str(make_string_telephone_number(readme_content.telephone_number)),
                     str(make_string_linkedin_url(readme_content.linkedin_url))
                    )
    final_string = "".join(content_tuple)
    print(final_string)
    return final_string
    
def make_string_base_section(title, description):
    return_string = f'## {title}  {description}  '
    print(return_string)
    return return_string

def make_string_para(para):
    return f'{para}  '

def make_string_title(title):
    return f'## {title}  '

def make_string_description(description):
    return make_string_para(description)

def make_string_installation_instructions(description):
    return make_string_base_section("Installation Instructions", description)

def make_string_usage_information(description):
    return make_string_base_section("Usage Information", description)

def make_string_licence(description):
    return make_string_base_section("Licence", description)

def make_string_author(first_name, last_name):
    return f'## "Author"  {first_name} {last_name}  '

def make_string_email_address(email):
    return make_string_base_section("Email Address", email)

def make_string_telephone_number(tel):
    return make_string_base_section("Telephone Number", tel)

def make_string_linkedin_url(url):
    return make_string_base_section("LinkedIn Profile", url)

