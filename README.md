```

        ███████╗ █████╗ ██╗ ██████╗    ██╗    ██╗███████╗██████╗ ███████╗██╗████████╗███████╗
        ██╔════╝██╔══██╗██║██╔════╝    ██║    ██║██╔════╝██╔══██╗██╔════╝██║╚══██╔══╝██╔════╝
        █████╗  ███████║██║██║         ██║ █╗ ██║█████╗  ██████╔╝███████╗██║   ██║   █████╗  
        ██╔══╝  ██╔══██║██║██║         ██║███╗██║██╔══╝  ██╔══██╗╚════██║██║   ██║   ██╔══╝  
        ██║     ██║  ██║██║╚██████╗    ╚███╔███╔╝███████╗██████╔╝███████║██║   ██║   ███████╗
        ╚═╝     ╚═╝  ╚═╝╚═╝ ╚═════╝     ╚══╝╚══╝ ╚══════╝╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚══════╝

```

## :robot: Development branch
- This branch serves as the integration branch for ongoing development work.
- Developers merge their feature branches into the development branch.
- Regular testing and code reviews are conducted here before merging into the master/main branch.


## :hammer_and_wrench: Requirements

- python == 3.11

## :package: Installation

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

## :rocket: Development

__Start a development server__

- The `--insecure` attribute allows loading static files in development when `debug = False`

```py
python manage.py runserver --insecure
```

__Running test cases:__

- Open in root directory to run all the unit test cases

```py
python manage.py test
```
