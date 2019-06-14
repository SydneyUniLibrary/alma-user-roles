# -*- coding: utf-8 -*-


import json
import logging
import typing

import alma
import alma_sdk


logger = logging.getLogger('user_roles.replace_user_roles')


def replace_user_roles(api_client: alma_sdk.ApiClient, user_id_list: typing.List[str], template_file):
    users_api = alma_sdk.UsersApi(api_client)
    template = json.load(template_file)
    logger.debug('Template: %r', template)
    for user_id in user_id_list:
        logger.debug('Getting roles of user %s', user_id)
        user = users_api.getalmawsv1usersuser_id(user_id)
        if user is None:
            logger.warning('User %s was not found', user_id)
            continue
        primary_id = user['primary_id']
        logger.debug('Got user %r', primary_id)
        alma.fixup_alma_user(user)
        user['user_role'] = template
        logger.debug('Setting roles of user %s', primary_id)
        users_api.putalmawsv1usersuser_id(user, user['primary_id'])
        print(f'{user_id} updated')
