import requests

#Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Store API response in a variable.
response_dict = r.json()
print("Total reposutories:", response_dict['total_count'])

#Explore teh first reposuriry.
repo_dicts = response_dict['items']
print("Repositirues returned:",len(repo_dicts))

#Examine informatiion about the repositories
# repo_dict = repo_dicts[0]
# print("\n Keys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])
# Process results.
#print(response_dict.keys())
