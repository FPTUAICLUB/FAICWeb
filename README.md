```

        ███████╗ █████╗ ██╗ ██████╗    ██╗    ██╗███████╗██████╗ ███████╗██╗████████╗███████╗
        ██╔════╝██╔══██╗██║██╔════╝    ██║    ██║██╔════╝██╔══██╗██╔════╝██║╚══██╔══╝██╔════╝
        █████╗  ███████║██║██║         ██║ █╗ ██║█████╗  ██████╔╝███████╗██║   ██║   █████╗  
        ██╔══╝  ██╔══██║██║██║         ██║███╗██║██╔══╝  ██╔══██╗╚════██║██║   ██║   ██╔══╝  
        ██║     ██║  ██║██║╚██████╗    ╚███╔███╔╝███████╗██████╔╝███████║██║   ██║   ███████╗
        ╚═╝     ╚═╝  ╚═╝╚═╝ ╚═════╝     ╚══╝╚══╝ ╚══════╝╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚══════╝

```

## :robot: Backend development branch

### :hammer_and_wrench: Requirements

- python == 3.11

### :package: Installation
- :octocat: Clone the repo and change to branch remotes/origin/front_end_nightly

```sh
git clone https://github.com/FPTUAICLUB/AI-Web.git
cd AI-Web
git checkout remotes/origin/front_end_nightly
```

- :wrench: Install dependencies and initialize environment

```sh
python -m pip install pipenv
pipenv install --dev
pipenv shell
```

- :rocket: Start to develop

```py
python manage.py runserver
```
