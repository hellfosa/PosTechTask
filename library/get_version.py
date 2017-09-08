#!/usr/bin/python

from ansible.module_utils.basic import *

def main():

    fields = {
        'program': {'required': True, 'type': 'str'}
    }
    res = {}

    module = AnsibleModule(argument_spec=fields)
    try:
        bashCommand = '{0} --version'.format(module.params['program'])
        output = subprocess.check_output(['bash', '-c', bashCommand])
        string = output.strip().split()
    except(Exception):
        res['msg'] = 'Program {0} is not installed'.format(module.params['program'])
        module.exit_json(result=res)

    try:
        ver = '{0} {1}'.format(string[1], string[2])
    except(LookupError):
        ver = string[1]
    res[string[0]] = ver
    module.exit_json(result=res)


if __name__ == '__main__':
    main()