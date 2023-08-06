# git-repo-master

Simple application to manage your Azure DevOps git repository

## Installation

``` bash
git clone https://github.com/mustafmst/git-repo-master.git
python git-repo-master/setup.py install
```

## Usage

```bash
$ grm -h

usage: __main__.py [-h] [-organization ORGANIZATION] [-project PROJECT]
                   [-repository REPOSITORY [REPOSITORY ...]] [-token TOKEN]
                   [-action {lock-branch,unlock-branch,create-pull-request}]
                   [-branch BRANCH] [-source SOURCE] [-target TARGET]
                   [-title TITLE] [-description DESCRIPTION]

optional arguments:
  -h, --help            show this help message and exit

All arguments:
  -organization ORGANIZATION
                        Azure DevOps organization
  -project PROJECT      Azure DevOps project in given organization
  -repository REPOSITORY [REPOSITORY ...]
                        Repo for action
  -token TOKEN          Personal access token for Azure DevOps
  -action {lock-branch,unlock-branch,create-pull-request}
                        Action to perform

Branch lock and unlock actions arguments:
  -branch BRANCH        Branch to perform action on

Create pull request action arguments:
  -source SOURCE        Branch name from which action has to be done
  -target TARGET        Branch name to which action has to be done
  -title TITLE          Pull request title
  -description DESCRIPTION
                        Pull request description

```
