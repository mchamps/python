from jira import JIRA
import pandas as pd
jiraOptions = {'server': "https://jira.atlassian.com"}

# Get a JIRA client instance, pass,
# Authentication parameters
# and the Server name.
jira = JIRA(options=jiraOptions, basic_auth=("USER_NAME_HERE", "YOUR_PASSWORD_HERE"))

block_size = 1000
block_num = 0
allissues = []
while True:
    start_idx = block_num*block_size
    issues = jira.search_issues("project = 'FULL_PROJECT_NAME_HERE'", start_idx, block_size)
    if len(issues) == 0:
        # Retrieve issues until there are no more to come
        break
    block_num += 1
    for issue in issues:
        #log.info('%s: %s' % (issue.key, issue.fields.summary))
        allissues.append(issue)
issues = pd.DataFrame()
for issue in allissues:
        d = {
            'key': issue.key,
            'assignee': issue.fields.assignee,
            'creator' : issue.fields.creator,
            'reporter': issue.fields.reporter,
            'created' : issue.fields.created,
            'components': issue.fields.components,
            'description': issue.fields.description,
            'summary': issue.fields.summary,
            'fixVersions': issue.fields.fixVersions,
            'subtask': issue.fields.issuetype.subtask,
            'issuetype': issue.fields.issuetype.name,
            'priority': issue.fields.priority.name,
            'resolution': issue.fields.resolution,
            'resolution.date': issue.fields.resolutiondate,
            'status.name': issue.fields.status.name,
            'status.description': issue.fields.status.description,
            'updated': issue.fields.updated,
            #'versions': issue.fields.versions,
            #'watches': issue.fields.watches.watchCount,
            #'storypoints': issue.fields.customfield_10142
        }
        issues = issues.append(d, ignore_index=True)
        
print(issues)
