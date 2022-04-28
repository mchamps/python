import pandas as pd

changelog = pd.DataFrame()

for issue in allissues:
  
  issue = jira.issue(issue.key, expand='changelog')
  achangelog = issue.changelog

  for history in achangelog.histories:
    for item in history.items:
    d = {
      'key': issue.key,
      'author': history.author,
      'date': history.created,
      'field': item.field,
      'fieldtype' : item.fieldtype,
      'from': getattr(item, 'from'), # because using item.from doesn't work
      'fromString' : item.fromString,
      'to': item.to,
      'toString': item.toString
    }
    changelog = changelog.append(d, ignore_index=True)
    
print(changelog)
