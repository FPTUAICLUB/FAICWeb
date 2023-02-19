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

- :octocat: Clone the repo and change to branch remotes/origin/back_end_develop

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

### :rocket: Development

__Start a development server__

The `--insecure` attribute allows loading static files in development when `debug = False`

```py
python manage.py runserver --insecure
```

__Running test cases: (Open in root directory to run all the tests)__

```py
python manage.py test
```
