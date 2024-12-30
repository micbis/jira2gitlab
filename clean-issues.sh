#!/bin/bash

eval $( cat jira2gitlab_secrets.py | sed 's/ = /=/' )

PROJECT_ID=1
GITLAB_URL="https://git.byteworks.ch/api/v4"

#for PROJECT_ID in {1..141}; do
for PROJECT_ID in 74 75; do
	# Fetch all issues from the project
	issues=$(curl --header "PRIVATE-TOKEN: $GITLAB_TOKEN" --url "$GITLAB_URL/projects/$PROJECT_ID/issues?per_page=100")
	
	# Parse issue IDs from the JSON response
	issue_ids=$(echo $issues | jq -r '.[].iid')
	
	# Loop through each issue ID and delete the issue
	for issue_id in $issue_ids; do
	  echo "Deleting issue ID: $issue_id"
	  curl --request DELETE \
	    --header "PRIVATE-TOKEN: $GITLAB_TOKEN" \
	    --url "$GITLAB_URL/projects/$PROJECT_ID/issues/$issue_id"
	done
done
