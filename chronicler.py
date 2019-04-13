#!/usr/bin/env python3
"""
Manages the manifest.json file

-- Versioning --
Versioning follows the `major.minor.commit` format
	- major change signifies a change in programmatic structure for site
	- minor change signifies a change in content for website
	- commit is the number of commits since last version change
"""
import argparse
import json
import os
from pprint import pprint
from subprocess import Popen, PIPE

def bump_version(major, minor):
	assert os.path.isfile('manifest.json')
	with open('manifest.json', 'r') as manifest:
		contents = json.load(manifest)

	assert 'version' in contents.keys()
	assert 'lastupdated' in contents.keys()
	major_version, minor_version, commits = contents['version'].split('.')
	lastupdated = contents['lastupdated']

	if major:
		major_version = int(major_version) + 1
	if minor:
		minor_version = int(minor_version) + 1
	cmd = 'git rev-list HEAD --count'
	proc = Popen(cmd, stdout=PIPE, shell=True)
	stdout, stderr = proc.communicate()
	if major or minor:
		contents['lastupdated'] = int(stdout)
		commits = 0
	else:
		commits = int(stdout) - int(lastupdated)

	contents['version'] = f'{major_version}.{minor_version}.{commits}'
	with open('manifest.json', 'w') as manifest:
		json.dump(contents, manifest)

def build_parser():
	"""
	Build CLI parser
	"""
	parser = argparse.ArgumentParser(description=__doc__, formatter_class = argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('-M', '--major', action='store_true', required=False, default=False, help="if included, chronicler will bump the major version")
	parser.add_argument('-m', '--minor', action='store_true', required=False, default=False, help="if included, chronicler will bump the minor version")
	return parser

def main():
	parser = build_parser()
	args = parser.parse_args()

	bump_version(args.major, args.minor)

if __name__ == '__main__':
	main()