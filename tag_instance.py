#!/usr/bin/env python
#

import argparse
import boto3
import sys

# Arguments: instance_id

cli_parser = argparse.ArgumentParser()
cli_parser.add_argument("-R", "--region", help="region to find instance in", default="us-west-2")
cli_parser.add_argument("-I", "--instanceid", help="instance to set tags on", required=True)
cli_parser.add_argument("-V", "--verbose", help="enable verbose logging", action="count")
cli_parser.add_argument("-L", "--lifecycle", help="enable verbose logging", default="20191101")
cli_args = cli_parser.parse_args()

my_ec2_tags = [{'Key':'Owner', 'Value':'John Kinsella'},
        {'Key':'Email', 'Value':'jlk@blah.com'},
        {'Key':'Department', 'Value':'dept'},
        {'Key':'Lifecycle', 'Value':'20202101'},
        {'Key':'Jira', 'Value':''}]

# print_tags() - prints out AWS tags from a python dict
def print_tags(tags):
    for tag in tags:
        print("{}: {}".format(tag["Key"], tag["Value"]))

ec2_resource = boto3.resource('ec2', region_name=cli_args.region)

try:
    instance = ec2_resource.Instance(cli_args.instanceid)
    instance.tags
except Exception as e:
    print("Exception loading instance: %s" % e)
    sys.exit(-1)

if cli_args.verbose:
    print "Current tags:"
    print_tags(instance.tags)
    print ""

instance.tags.extend(my_ec2_tags)

if cli_args.verbose:
    print "Updated tags (may have duplicates - AWS will dedupe):"
    print_tags(instance.tags)
    print ""

if cli_args.verbose:
    print "Updating..."

ec2_client = boto3.client('ec2', region_name=cli_args.region)

ec2_client.create_tags(Resources=[cli_args.instanceid], Tags=instance.tags)

if cli_args.verbose:
    print "Done."

