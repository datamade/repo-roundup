import csv
import requests

def get_readme_list():

    api_url = 'https://api.github.com/orgs/datamade/repos?per_page=100'
    repos_list = []

    fields = ['name',
              'html_url',
              'stargazers_count',
              'forks',
              'description',
              'homepage',
              'language',
              'created_at',
              'updated_at']

    for page in range(1,3):
        print("Page %s" % page)
        repos = requests.get(api_url + "&page=" + str(page))
        if repos.status_code is 200:
            for r in repos.json():
                repos_list.append([r[key] for key in fields])

    print("Repo list created. Length: %s" % len(repos_list))

    outp = open('datamade_repos.csv', 'w')
    writer = csv.writer(outp)
    writer.writerow(fields) # header
    writer.writerows(repos_list) # data
    outp.close()

if __name__ == "__main__":
    get_readme_list()
