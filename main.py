import os,sys
from github import Github
path="C://Users//HP//MyProjects//"

os.chdir(path)

def github_repo_creation(name):
    user = Github("d8aa91ee9b70d5d5db35275f3d3f55328db8f32d").get_user()
    user.create_repo(name)
    print("Repository Created With Name {}".format(name))

def remote_url(name):
    name = name.replace(" ", "-")
    remote = "git remote add origin git@github.com:keshav-ladha/"+name+".git"
    return remote

def create_dir(name,remote):
    os.mkdir(path+name)
    os.chdir(path+name)
    os.system('git init')
    os.system('echo "# {}" > README.md'.format(path+name))
    os.system('git add README.md')
    os.system('git commit -m "Initial commit"')
    os.system(remote)
    os.system("git push -u origin master")
    os.system("code .")

if __name__ == "__main__":
    name = sys.argv[1]
    github_repo_creation(name)
    remote = remote_url(name)
    create_dir(name,remote)
