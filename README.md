This is a collection of scripts for tagging components on AWS without having to go through the web UI

## Setup

Virtualenv:
```
virtualenv venv
. venv/bin/activate
```

Then install requirements:
```
pip install -r requirements.txt
```

## Example usage

```
$ ./tag_instance.py --region us-east-2 --instanceid i-0aa25268495ea9c0c --verbose
Current tags:
Lifecycle: 20210201
Owner: John Kinsella
Name: website
Jira:
Department: dept
Email: jlk@blah.com

Updated tags (may have duplicates - AWS will dedupe):
Lifecycle: 20191101
Owner: John Kinsella
Name: website
Jira:
Department: dept
Email: jlk@blah.com
Owner: John Kinsella
Email: jlk@blah.com
Department: dept
Lifecycle: 20210201
Jira:

Updating...
Done.
```
