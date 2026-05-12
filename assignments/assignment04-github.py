from github import Github
from getpass import getpass

# Assignment 04 - GitHub API
# This program uses the GitHub API to read a file from a repository,
# replace the text "Andrew" with my name, and commit the change back.

ACCESS_TOKEN = getpass("Paste your GitHub token here: ")

REPO_NAME = "Nebulosa-max/test_lab04"
FILE_PATH = "README.md"
MY_NAME = "Sophia Godoy"

g = Github(ACCESS_TOKEN)
repo = g.get_repo(REPO_NAME)

file = repo.get_contents(FILE_PATH)
content = file.decoded_content.decode("utf-8")

updated_content = content.replace("Andrew", MY_NAME)

if content != updated_content:
    repo.update_file(
        path=FILE_PATH,
        message="Replace Andrew with Sophia Godoy",
        content=updated_content,
        sha=file.sha
    )
    print("File updated and pushed successfully.")
else:
    print("No changes needed. Andrew was not found.")
