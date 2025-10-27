def create_readme(readme_content):
    str[0] = make_string_title(readme_content.title)
    str[1] = make_string_description(readme_content.description)
    str[2] = make_string_installation_instructions(readme_content.installation_instructions)
    str[3] = make_string_usage_information(readme_content.usage_information)
    str[4] = make_string_licence(readme_content.licence)
    str[5] = make_string_author(readme_content.author_first_name, readme_content.author_last_name)
    str[7] = make_string_email_address(readme_content.email_address)
    str[8] = make_string_linkedin_url(readme_content.linkedin_url)
    final_str = 0
    for i in range(9):
        final_str.append(str[i])
    return final_str
    
def make_string_base_section(title, description):
    return f'## {title}  {description}  '

def make_string_para(para):
    return f'{para}  '

def make_string_title(title):
    return f'## {title}  '

def make_string_description(description):
    make_string_para(description)

def make_string_installation_instructions(description):
    make_string_base_section("Installation Instructions", description)

def make_string_usage_information(description):
    make_string_base_section("Usage Information", description)

def make_string_licence(description):
    make_string_base_section("Licence", description)

def make_string_author(first_name, last_name):
    return f'## "Author"  {first_name} {last_name}  '

def make_string_email_address(email):
    make_string_base_section("Email Address", {email})

def make_string_linkedin_url(url):
    make_string_base_section("LinkedIn Profile", {url})
