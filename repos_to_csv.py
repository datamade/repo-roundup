import csv
import requests

def get_repo_list():

    # change these things for your org
    org_name = 'datamade'
    pages_to_fetch = 2 # number of repos you have, divided by 100. kinda hack-y!

    api_url = 'https://api.github.com/orgs/%s/repos?per_page=100' % org_name
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

    for page in range(1,(pages_to_fetch + 1)):
        print("Page %s" % page)
        repos = requests.get(api_url + "&page=" + str(page))
        if repos.status_code is 200:
            for r in repos.json():
                repos_list.append([r[key] for key in fields])

    print("Repo list created. Length: %s" % len(repos_list))

    outp = open(('%s_repos.csv' % org_name), 'w')
    writer = csv.writer(outp)
    writer.writerow(fields) # header
    writer.writerows(repos_list) # data
    outp.close()

    print("File written: %s" % ('%s_repos.csv' % org_name))
    print("done")

if __name__ == "__main__":
    get_repo_list()
