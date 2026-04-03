from github import Github
from config import config as cfg

# API key
apikey = cfg["githubkey"]

# conectar ao GitHub
g = Github(apikey)

# 1. listar repos
print("\nYour repositories:")
for repo in g.get_user().get_repos():
    print(repo.name)

# 2. pegar repo
repo = g.get_repo("Nebulosa-max/test_lab04")

# 3. mostrar clone URL
print("\nClone URL:")
print(repo.clone_url)

# 4. pegar ficheiro test.txt
fileInfo = repo.get_contents("test.txt")

# 5. mostrar download URL
urlOfFile = fileInfo.download_url
print("\nDownload URL:")
print(urlOfFile)