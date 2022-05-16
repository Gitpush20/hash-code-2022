
# def parse(file):
#     with open(file,'r') as f:
#         data = f.read().split('\n')


import json

f = open('a_an_example.in.txt.json')

data = json.load(f)
# print(data)
projects = data['projects']
contributors = data['contributors']
n_projects = {}
# for item in projects:

def sort_projects(projects):
    def loss(days, roles, score):
        return 2 * score - 5 * days - 5 * roles
    proj_s = {}
    i = 0
    for item in projects:
        name = item['name']
        days = item['days']
        score = item['score']
        roles = len(item['roles'])
        proj_s[name] = loss(days, roles, score)
        n_projects[name] = item
        i += 1
    return sorted(proj_s.items(), key=lambda x: x[1])  
     


def sort_skills(contributors):
    skills = {}
    for item in contributors:
        name = item['name']
        skill  = item['skills']
        for it in skill:
            name_s = it['name']
            level = it['level']
            try:
                skills[name_s] += [(name,level)]
            except:
                skills[name_s] = [(name,level)]
    for key in skills.keys():
        skills[key] = sorted(skills[key], key=lambda x: x[1])
    return skills


projects_l = sort_projects(projects)
skills = sort_skills(contributors)
print(json.dumps(projects, indent=4))
print(skills)

# print(projects)

working_c = []
def has_the_requirement(project):
    for role in project['roles']:
        for item in skills[role]
            if item[0] not in working_c:
                


while len(projects_l) > 0:
    for i, p in enumerate(projects_l):
        if has_the_requirement(n_projects[p]):
            projects_l.pop(i)

