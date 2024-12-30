################################################################
# Jira options
################################################################

JIRA_URL = 'https://portal.byteworks.ch/jira'
JIRA_API = f'{JIRA_URL}/rest/api/2'

# Bitbucket URL, if available, is only used in pattern-matching
# to translate issue references to commits.
#BITBUCKET_URL = 'https://portal.byteworks.ch/bitbucket'

# How many items to request at a time from Jira (usually not more than 1000)
JIRA_PAGINATION_SIZE = 100

# the Jira Epic custom field
JIRA_EPIC_FIELD = ''

# the Jira story points custom field
JIRA_STORY_POINTS_FIELD = ''

# Custom JIRA fields
JIRA_CUSTOM_FIELDS = {
    #'customfield_14200': 'Metadata 1',
    #'customfield_14201': 'Metadata 2',
}

################################################################
# Gitlab options
################################################################

GITLAB_URL = 'https://git.byteworks.ch'
GITLAB_API = f'{GITLAB_URL}/api/v4'

# Support Gitlab Premium features (e.g. epics and "blocks" issue links)
GITLAB_PREMIUM = True

################################################################
# Import options
################################################################

# Name of the file storing the status of imports
IMPORT_STATUS_FILENAME = 'import_status.pickle'

# Set this to false if JIRA / Gitlab is using self-signed certificate.
VERIFY_SSL_CERTIFICATE = True

# PREFIX_LABEL is used with all existing Jira labels
PREFIX_LABEL = 'Jira::'

# PREFIX_COMPONENT is used with existing Jira components when no match is found in ISSUE_COMPONENT_MAP
# NOTE: better NOT to use a prefix for components, otherwise only 1 component will be imported in Gitlab
PREFIX_COMPONENT = ''

# PREFIX_PRIORITY is used with existing Jira priorities when no match is found in ISSUE_PRIORITY_MAP
PREFIX_PRIORITY = 'P::'

# Whether to migrate issue attachments
MIGRATE_ATTACHMENTS = True

# Whether to migrate worklogs as issue comment with /spend quick-action.
MIGRATE_WORLOGS = True

# Jira users are mapped to Gitlab users according to USER_MAP, with the following two exceptions:
# - Jira user 'jira' is mapped to Gitlab user 'root'
# - Jira users that are not in USER_MAP are mapped to Gitlab user 'root'
# If MIGRATE_USERS is True, mapped Gitlab users that don't exist yet in Gitlab will be migrated automatically
# If MIGRATE_USERS is False, all actions performed by a non-existing Gitlab user will be performed by Gitlab user 'root'
MIGRATE_USERS = False

# When MIGRATE_USERS is True, new users can be created in Gitlab.
# This is the *temporary* password they get.
NEW_GITLAB_USERS_PASSWORD = 'changeMe'

# If (new or existing) Gitlab users are not made admins during the import,
# the original timestamps of all user actions cannot be imported. Instead, the timestamp of the import will be used.
# When this option is enabled, users are made admin and changed back to their original role after the import. 
# If users cannot be changed back to non-admin, this is reported at the end of the import.
# This feature is recommended, but to be used with caution. Check users' status in Gitlab after the import.
MAKE_USERS_TEMPORARILY_ADMINS = True

# Prefix issue titles with "[PROJ-123]" (Jira issue-key)
ADD_JIRA_KEY_TO_TITLE = True

# REFERECE_BITBUCKET_COMMITS = True -> tries to translate Jira issue references in Bitbucket to Gitlab issue references
# Disable if the Jira instance does not have an active link to Bitbucket at the moment of the import
# Disable if not needed, to increase performance (more calls are needed for each issue)
# Limitations:
# - Bitbucket repositories need to be imported in Gitlab with the same project name (the group name can change)
# - This feature only works if the issue project and the commit project are in the same Gitlab group
REFERECE_BITBUCKET_COMMITS = False

# Try force converting broken jira tables (tables that have no headers)
FORCE_REPAIR_JIRA_TABLES = True

# Set this to True if you want to keep original attachments filenames.
# Diacritics are removed, but no full normalisation to ASCII is performed.
# Therefore this may cause 500 errors on some unicode characters.
# When set to False, filenames are replaced with UUIDs.
KEEP_ORIGINAL_ATTACHMENT_FILENAMES = True


################################################################
# Import mappings
################################################################

# Jira - Gitlab group/project mapping
# Groups are not created. They must already exist in Gitlab.
PROJECTS = {
    #'BW - Diverses': '',
    #'BW - Infrastruktur - Extern (Hosting)': '',
    #'BW - Infrastruktur - Intern': '',
    #'BW - Internes': '',

    'License Portal': 'products/data-manager/licence-portal',

    'Mission Guard - App': 'products/mission-guard/app/app',
    'Mission Guard - Console': 'products/mission-guard/console',
    'Mission Guard - Data Manager': 'products/mission-guard/data-manager',
    'Mission Guard - Data Provider Bundle': 'products/mission-guard/components/symfony/data-bundle',
    'Mission Guard - Device Client': 'products/mission-guard/device-client',
    'Mission Guard - Endpoint Manager': 'products/mission-guard/endpoint-manager',
    'Mission Guard - Mission Provider Bundle': 'products/mission-guard/components/symfony/mission-bundle',
    'Mission Guard - Portal': 'products/mission-guard/portal',
    #'Mission Guard - Diverses': '',

    #'GVZ - Diverses': '',
    'GVZ - GRISU': 'clients/gvz/grisu',
    'GVZ - IDP': 'clients/gvz/idp',
    'GVZ - Kursfeedback': 'clients/gvz/kursfeedback/backend',
    'GVZ - Pager Admin': 'clients/gvz/pager-admin',
    'GVZ - Pager Log': 'products/pager-log/backend',
    #'GVZ - SPA-IF Ersatz': '',
    'GVZ - Statusportal': 'clients/gvz/status-portal',

    'Gübelin': 'clients/gubelin/guebelin-backend',
    'tibits': 'clients/tibits/backend',

    'Maxon - Bike Drive': 'clients/maxon/bike-drive/backend',
    'Maxon - Drive Tech': 'clients/maxon/drive-tech/backend',
}

# Bitbucket - Gitlab mapping
# *Not* used to migrate Bitbucket repos (use Gitlab's integration for that)
# Used to map references from issues to commits in Bitbucket repos that are migrated to Gitlab
# Make sure you use the correct casing for Bitbucket: project key is all upper-case, repository is all lower-case
PROJECTS_BITBUCKET = {
    #'PROJ1/repository1': 'group1/project1',
}

# Jira - Gitlab username mapping
USER_MAP = {
  'admin': 'root',
  'bismic' : 'michael.bischof',
  'wiechr' : 'christoph.wieseke',

  'binron': 'ronny.binder',
  'christian.nuessli@zuerich.ch': 'christian.nuessli',

  'michael.messmer@gvz.ch': 'michael.messmer',
  'vasco.avanzini@gvz.ch': 'vasco.avanzini',
  'william.ihde@gvz.ch': 'william.ihde',

  'michel.riedmann@maxongroup.com': 'michel.riedmann',
  'mario.warthmann@maxongroup.com': 'mario.warthmann',
  'adrian.hofstetter@maxongroup.com': 'adrian.hofstetter',

  'alexander.dardel@gubelin.com': 'alexander.dardel',
}

# Map Jira issue types to Gitlab labels
# Unknown issue types are mapped as generic labels
ISSUE_TYPE_MAP = {
    'Aufgabe': 'Type::Task',
    'Neue Funktion': 'Type::Feature',
    'Verbesserung': 'Type::Improvement',
    'Bug': 'Type::Bug',
    'Improvement': 'Type::Improvement',
    'New Feature': 'Type::Feature',
    'Epic': 'Type::Epic',
    'Task': 'Type::Task',
    'Sub-Task': 'Type::Task',
    #'Spike': 'Type::Spike',
    'Story': 'Type::Story',
}

# Map Jira components to labels
# NOTE: better NOT to use a prefix for components, otherwise only 1 component will be imported in Gitlab
ISSUE_COMPONENT_MAP = {
    #'Component1': 'component1',
    #'Component2': 'component2'
}

# Map Jira priorities to labels
ISSUE_PRIORITY_MAP = {
    'Critical': 'Priority::Critical',
    'Highest': 'Priority::High',
    'High': 'Priority::High',
    'Medium': 'Priority::Medium',
    'Lowest': 'Priority::Low',
    'Low': 'Priority::Low',

    'Hoch': 'Priority::High',
    'Niedrig': 'Priority::Low',
}

# Map Jira resolutions to labels
ISSUE_RESOLUTION_MAP = {
    'Cannot Reproduce': 'State::Can\'t reproduce',
    'Duplicate': 'State::Duplicate',
    'Incomplete': 'State::Incomplete',
    'Won\'t Do': 'State::Won\'t do',
    'Won\'t Fix': 'State::Won\'t fix',
#    'Unresolved': 'S::unresolved',
#    'Done': 'S::done',
#    'Fixed': 'S::fixed',
}

# Map Jira statuses to labels
ISSUE_STATUS_MAP = {
    'Approved': 'State::Approved',
    'Awaiting documentation': 'State::Waiting',
    'In Progress': 'State::In progress',
    'In Review': 'State::In review',
    'In Arbeit': 'State::In progress',

    # 'Awaiting payment': '',
    # 'Backlog': '',
    # 'Cancelled': '',
    # 'Closed: '',
    # 'Done': '',
    # 'Open': '',
    # 'Paid': '',
    # 'Rejected': '',
    # 'Reopened': '',
    # 'Resolved': '',
    # 'Selected for Development': '',
}

# These Jira statuses will cause the corresponding Gitlab issue to be closed
ISSUE_STATUS_CLOSED = {
    #'Awaiting documentation',
}

# Set colors for single labels or group of labels
LABEL_COLORS = {
    'Source::Jira': '#e6e6fa',
}

for key, value in ISSUE_TYPE_MAP.items():
    LABEL_COLORS[value] = '#6699cc'

for key, value in ISSUE_PRIORITY_MAP.items():
    LABEL_COLORS[value] = '#ed9121' #'#8fbc8f'

for key, value in ISSUE_STATUS_MAP.items():
    LABEL_COLORS[value] = '#009966'

for key, value in ISSUE_RESOLUTION_MAP.items():
    LABEL_COLORS[value] = '#009966'

# TODO: Disable once finished testing
#for key, value in PROJECTS.items():
#    PROJECTS[key] = 'test-1/test-1.2/test-1.2.1'

