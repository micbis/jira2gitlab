#!/bin/bash

eval $( cat jira2gitlab_secrets.py | sed 's/ = /=/' )

PROJECT_ID=1
GITLAB_URL="https://git.byteworks.ch/api/v4"

labels=$(curl --header "PRIVATE-TOKEN: $GITLAB_TOKEN" --url "$GITLAB_URL/projects/$PROJECT_ID/labels?per_page=100")

# Parse issue IDs from the JSON response
label_ids=$(echo $labels | jq -r '.[].id')

# Loop through each issue ID and delete the issue
for label_id in $label_ids; do
  echo "Deleting label ID: $label_id"
  curl --request DELETE \
    --header "PRIVATE-TOKEN: $GITLAB_TOKEN" \
    --url "$GITLAB_URL/projects/$PROJECT_ID/labels/$label_id"
done
