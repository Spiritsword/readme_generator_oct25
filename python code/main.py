
from readme_generation import create_readme
from content import content_input

def main():
    """ Inputs readme content from the user and generates readme markdown, writing it to "AUTOREADME.md" file.
        This is the top-level function of the project.

        Args: (None)

        Returns: (None)

    """
    new_readme_content = content_input()
    readme_markdown = create_readme(new_readme_content)
    with open("AUTOREADME.md", "w") as f:
        f.write(readme_markdown)

#Run top-level function
if __name__ == "__main__":
    main()






