#!/usr/bin/python

import sys
import os
import os.path

import argparse

import json

try:
    from foreman import FHosts
    from foreman import PTable
except ImportError, e:
    print('you didn\'t install python-foreman')
    print(e)
    sys.exit(1)


def prepare_parser(parser=None):
    if parser is None:
        parser = argparse.ArgumentParser(prog='foreman-cli')
    parser.add_argument('--foreman-url', default=None, action='store',
                        metavar='http://your.foreman.tld/',
                        dest='foreman_url', help='Foreman Web URL',
                        required=True)
    parser.add_argument('--foreman-user', default=None, action='store',
                        metavar='USERNAME', dest='foreman_user',
                        help='Your Foreman Username', required=True)
    parser.add_argument('--foreman-password', default=None, action='store',
                        metavar='PASSWORD', dest='foreman_password',
                        help='Your Foreman Password', required=True)
    parser.add_argument('-O', '--ofile', metavar='FILENAME',
                        dest='output_filename', action='store',
                        help='Filename for output file')
    parser.add_argument('-F', '--format', dest='output_format',
                        choices=['json', 'txt', 'pretty'],
                        default='txt')
    subparser = parser.add_subparsers(help='Foreman Resource Commands', dest='resource_cmd')
    prepare_parser_hosts(subparser)

def prepare_parser_hosts(subparser=None):
    if subparser is None:
        return False
    parser = subparser.add_parser('hosts', help='Foreman Hosts Commands')
    parser.add_argument('-l', '--list', default=False, action='store_true',
                        dest='host_list', help='List all Hosts in Foreman')
    parser.add_argument('-s', '--search', default=None, action='store',
                        dest='host_search', help='Find Hosts in foreman')
    parser.add_argument('-g', '--get', default=None, action='store',
                        dest='host_get', help='Get host Record')
    parser.add_argument('--parameters', default=False, action='store_true',
                        dest='host_parameters', help='Print Host Parameters')

def do_process_hosts(args=None):
    if args is None:
        return False
    h = FHosts(args.foreman_url, args.foreman_user,
               args.foreman_password)
    if args.host_list:
        hlist = []
        if args.host_search is None:
            hlist = h.list()
        else:
            hlist = h.search(args.host_search)
        if args.output_format == 'txt':
            if args.output_filename is None:
                for i in hlist:
                    print i['host']['name']
            else:
                fp = open(args.output_filename, 'wb')
                for i in hlist:
                    fp.write('{0}\n'.format(i['host']['name']))
                fp.close()
        if args.output_format == 'pretty':
            print('       No.| Hostname\n'
                  '----------+----------------------------------------')
            counter = 0
            for i in hlist:
                counter += 1
                print('{0:10d}| {1:40s}').format(counter, i['host']['name'])
            print('----------+----------------------------------------')
            print('Amount of Hosts: {0:d}').format(counter)
            if args.host_search is not None:
                print('Your search string was:\n\t\t{0}'.
                      format(args.host_search))

        if args.output_format == 'json':
            if args.output_filename is None:
                print(json.dumps(hlist))
            else:
                fp = open(args.output_filename, 'wb')
                json.dump(hlist, fp)
                fp.close()
    if args.host_get is not None:
        record = h.get(args.host_get)
        for key, value in record['host'].iteritems():
            print('{0} => {1}'.format(key, value))
        # if args.host_parameters is True:
        #    pt = PTable(args.foreman_url, args.foreman_user,
        #                args.foreman_password)
        #    parameters = pt.list(record['host']['ptable_id'])
        #    print parameters

def do_process(args=None):
    if args is None:
        return False

    if (args.foreman_url is not None and
        args.foreman_user is not None and
        args.foreman_password is not None):
        if args.resource_cmd == 'hosts':
            result = do_process_hosts(args)
            if result is not False:
                return result
    else:
        return False
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='foreman-cli')
    prepare_parser(parser)

    args = parser.parse_args()
    result = do_process(args)
    if result is False:
        print('Something went wrong')
        sys.exit(1)

