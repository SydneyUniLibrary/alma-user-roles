# -*- coding: utf-8 -*-

import argparse
import logging
import os
import sys

import alma
import alma_sdk
import alma_sdk.rest

from .get_user_roles import get_user_roles
from .replace_user_roles import replace_user_roles
from .verify_user_roles import verify_user_roles


logger = logging.getLogger('user_roles.__main__')


def parse_args():
    parser = argparse.ArgumentParser(
        prog='user-roles',
        description='''Maintains the roles in Alma's users.'''
    )
    parser.add_argument('--verbose', '-v', action='store_true', default=False,
                        help='raise the log level to DEBUG')
    parser.add_argument('--alma-api-server', metavar='SERVER', default=os.environ.get('ALMA_API_SERVER'),
                        help='send API requests to SERVER'
                             ' (fully-qualified domain name: the abc.com of https://abc.com/)')
    parser.add_argument('--alma-api-key', metavar='API-KEY', default=os.environ.get('ALMA_API_KEY'),
                        help='use KEY when sending API-KEY requests to Alma')

    commands_subparsers = parser.add_subparsers(title='commands')

    subparser = commands_subparsers.add_parser('get', help='get the roles of a user')
    subparser.add_argument('user', metavar='ID',
                           help='The primary id or one of the identifiers of the user.')
    subparser.add_argument('--include-inactive', action='store_true', default=False,
                           help='Including inactive user roles. Excludes inactive user roles by default.')
    subparser.set_defaults(cmd='get')

    subparser = commands_subparsers.add_parser('replace', help='replace the roles of users with the template')
    subparser.add_argument('users', metavar='ID', nargs='+',
                           help='The primary id or one of the identifiers of each user.')
    subparser.add_argument('--template', metavar='PATH', type=argparse.FileType(),
                           help='Use the roles stores in file at PATH to verify the users, defaults to stdin')
    subparser.set_defaults(cmd='replace')

    subparser = commands_subparsers.add_parser('verify', help='verify that the roles of users match a template')
    subparser.add_argument('users', metavar='ID', nargs='+',
                           help='The primary id or one of the identifiers of each user.')
    subparser.add_argument('--template', metavar='PATH', type=argparse.FileType(),
                           help='Use the roles stores in file at PATH to verify the users, defaults to stdin')
    subparser.add_argument('--include-inactive', action='store_true', default=False,
                           help='Including inactive user roles. Excludes inactive user roles by default.')
    subparser.add_argument('--ignore-extras', action='store_true', default=False,
                           help='Ignore if users have extra roles beyond the template.')
    subparser.set_defaults(cmd='verify')

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    logging.basicConfig(level=logging.INFO, stream=sys.stderr,
                        format='%(process)-6d %(asctime)-28s %(name)-35s %(levelname)-7s %(message)s')
    logging.getLogger('user_roles').setLevel(logging.DEBUG if args.verbose else logging.INFO)
    logger.debug('Start run: args = %r', args)

    configuration = alma_sdk.Configuration()
    configuration.api_key['apikey'] = args.alma_api_key
    configuration.host = f'https://{args.alma_api_server}'
    api_client = alma_sdk.ApiClient(configuration)

    if args.cmd == 'get':
        get_user_roles(api_client, args.user, args.include_inactive, args.verbose)
    elif args.cmd == 'replace':
        replace_user_roles(api_client, args.users, args.template)
    elif args.cmd == 'verify':
        verify_user_roles(api_client, args.users, args.template, args.include_inactive, args.ignore_extras)

    logger.debug('End run')


if __name__ == '__main__':
    main()
