#!/usr/bin/env python3
"""Simple validator for the AME Beta playbook structure.

Checks for required files and simple content hints. This is a lightweight structural
check — it does not execute actions or modify the system.
"""
import os
import sys

ROOT = os.path.dirname(__file__)

def exists(path):
    return os.path.exists(os.path.join(ROOT, path))

def read(path):
    with open(os.path.join(ROOT, path), 'r', encoding='utf-8') as f:
        return f.read()

errors = []

# playbook.conf
pc = 'playbook.conf'
if not exists(pc):
    errors.append('Missing playbook.conf at playbook root')
else:
    s = read(pc)
    if '<Playbook>' not in s or '</Playbook>' not in s:
        errors.append('playbook.conf does not contain a <Playbook> root element')
    if 'UniqueId' in s and 'YOUR_UNIQUE_ID_HERE' in s:
        errors.append('playbook.conf contains placeholder UniqueId (replace with a UUID)')

# main.yml
main = 'Configuration/main.yml'
if not exists(main):
    errors.append('Missing Configuration/main.yml')
else:
    s = read(main)
    if 'actions:' not in s:
        errors.append('Configuration/main.yml missing actions:')
    if '!task' not in s:
        errors.append('Configuration/main.yml does not reference any !task entries')

# tasks
for t in ['Configuration/Tasks/registry.yml', 'Configuration/Tasks/appx.yml']:
    if not exists(t):
        errors.append(f'Missing {t}')
    else:
        s = read(t)
        if 'actions:' not in s:
            errors.append(f'{t} missing actions:')

if errors:
    print('VALIDATION FAILED')
    for e in errors:
        print('- ' + e)
    print('\nFix the above issues and re-run this script.')
    sys.exit(2)

print('VALIDATION PASSED: playbook structure looks good for AME Beta.')
print('Reminder: replace the UniqueId in playbook.conf with a real UUID before deploying.')
sys.exit(0)
