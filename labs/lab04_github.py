from github import Github
from config import config as cfg
import requests

# API key
apiKey = cfg["githubkey"]
g = Github(apiKey)

# 1. listar repos
print("\nYour repositories:")
for repo in g.get_user().get_repos():
    print(repo.name)

# 2. pegar repo
repo = g.get_repo("Nebulosa-max/test_lab04")

print("\nClone URL:")
print(repo.clone_url)

# 3. pegar arquivo test.txt
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url

print("\nDownload URL:")
print(urlOfFile)

# 4. ler conteúdo
response = requests.get(urlOfFile)
contentOfFile = response.text

print("\nFile content:")
print(contentOfFile)

# 5. modificar conteúdo
newContents = contentOfFile + "\n more stuff\n"

# 6. atualizar arquivo no GitHub
repo.update_file(
    fileInfo.path,
    "updated by script",
    newContents,
    fileInfo.sha
)

print("\nFile updated successfully!")