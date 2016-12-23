# repo-roundup

python script that pulls a list of organization repos from the GitHub API into a CSV 

## Dependencies

* python 3.x
* a GitHub account or organization
* the [GitHub API v3](https://developer.github.com/v3/)

## Installation
We recommend using [virtualenv](http://virtualenv.readthedocs.org/en/latest/virtualenv.html) and [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html) for working in a virtualized development environment. [Read how to set up virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

Once you have virtualenvwrapper set up,

```bash
mkvirtualenv readme-roundup
git clone git://github.com/datamade/readme-roundup.git
cd readme-roundup
pip install -r requirements.txt
```

Afterwards, whenever you want to work on readme-roundup,

```bash
workon readme-roundup
```

## Usage

Edit `repos_to_csv.py` and add your organization settings:

```python
# change these things for your org
org_name = 'your-org-name'
pages_to_fetch = 2 # number of repos you have, divided by 100. kinda hack-y!
```

Then, run the script:

```bash
python repos_to_csv.py
```

Creates a file called `datamade_repos.csv` as a list of all public repos from the organization with the following fields:

* name
* html_url
* stargazers_count
* forks
* description
* homepage
* language
* created_at
* updated_at

## Team

* Derek Eder, DataMade

## Errors and bugs

If something is not behaving intuitively, it is a bug and should be reported.
Report it here by creating an issue: https://github.com/datamade/readme-roundup/issues

Help us fix the problem as quickly as possible by following [Mozilla's guidelines for reporting bugs.](https://developer.mozilla.org/en-US/docs/Mozilla/QA/Bug_writing_guidelines#General_Outline_of_a_Bug_Report)

## Patches and pull requests

Your patches are welcome. Here's our suggested workflow:

* Fork the project.
* Make your feature addition or bug fix.
* Send us a pull request with a description of your work. Bonus points for topic branches!

## Copyright and attribution

Copyright (c) 2016 DataMade. Released under the [MIT License](https://github.com/datamade/readme-roundup/blob/master/LICENSE).
