def create_readme(readme_content):
    content_tuple = (make_string_title(readme_content.title),
                    make_string_description(readme_content.description),
                    make_string_installation_instructions(readme_content.installation_instructions),
                    make_string_usage_information(readme_content.usage_information),
                    make_string_licence(readme_content.licence),
                    make_string_author(readme_content.author_first_name, readme_content.author_last_name),
                    make_string_email_address(readme_content.email_address),
                    make_string_telephone_number(readme_content.telephone_number),
                    make_string_linkedin_url(readme_content.linkedin_url)
                    )
    final_string = "".join(content_tuple)
    print(final_string)
    return final_string
    
def make_string_base_section(title, description):
    return_string = f'## {title} <br/><br/> {description} <br/><br/> '
    print(return_string)
    return return_string

def make_string_para(para):
    return f'{para} <br/><br/>'

def make_string_title(title):
    return f'## {title} <br/><br/>'

def make_string_description(description):
    return make_string_para(description)

def make_string_installation_instructions(description):
    return make_string_base_section("Installation Instructions", description)

def make_string_usage_information(description):
    return make_string_base_section("Usage Information", description)

def make_string_licence(description):
    return make_string_base_section("Licence", description)

def make_string_author(first_name, last_name):
    return f'## "Author" <br/><br/> {first_name} {last_name}  <br/><br/>'

def make_string_email_address(email):
    return make_string_base_section("Email Address", email)

def make_string_telephone_number(tel):
    return make_string_base_section("Telephone Number", tel)

def make_string_linkedin_url(url):
    link = f'["Profile link"] ({url})'
    return make_string_base_section("LinkedIn Profile", link)

