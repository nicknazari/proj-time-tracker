import sys
import json
import os

# in the below description, t% means the root command. by default, it is "tracker.py"
# commands and descriptions:
# % create <project name> : create a new .log file for a project
# % delete <project name> : delete an existing .log file for a project
# % addtime <project name> <time in MINUTES> [date] : add a time to an existing project, default date is today
# % removetime <project name> <time in MINUTES> [date] : remove time from a project, default date is today

# % stats <project name> : get details about a project

# we can also use open ended tracking, which starts a timer and adds to a project the number of minutes that the timer was active
# % live <project name> : begin live tracking on a project
# % livestop <project name> : end live tracking on a project

projfilehome = './data/'
projfilename = 'projects.json'
projfilepath = projfilehome + projfilename

def load_projects():
	projects = []
	if os.path.exists(projfilepath):
		with open(projfilepath, 'r') as projectfile:
			projects = json.load(projectfile)
	else:
		os.makedirs(projfilehome)
		with open(projfilepath, 'w+') as projectfile:
			json.dump(projects, projectfile)
	return projects


def save_projects(projects):
	with open(projfilepath, 'w') as projectfile:
		json.dump(projects, projectfile)

def create_project(name): # add description component later
	if name in projects:
		print("Error: project {} already exists".format(name))
	else:
		projects.append(name)
		
if __name__ == '__main__':
	projects = load_projects()
	create_project('house')
	save_projects(projects)
