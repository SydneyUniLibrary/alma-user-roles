# -*- coding: utf-8 -*-


import json
import logging
import typing

import alma
import alma_sdk


logger = logging.getLogger('user_roles.verify_user_roles')


def verify_user_roles(api_client: alma_sdk.ApiClient, user_id_list: typing.List[str], template_file,
                      include_inactive: bool = False, ignore_extra: bool = False):
    template = json.load(template_file)
    logger.debug('Template: %r', template)
    if ignore_extra:
        # TODO: Implement ignore_extra
        logger.warning('--ignore-extra has not been implemented yet')
    for user_id in user_id_list:
        logger.debug('Getting roles of user %s', user_id)
        user = alma_sdk.UsersApi(api_client).getalmawsv1usersuser_id(user_id)
        primary_id = user['primary_id']
        logger.debug('Got user %r', primary_id)
        user_role_list = [
            user_role
            for user_role in user.get('user_role') or []
            if include_inactive or alma.is_user_role_active(user_role)
        ]
        if user_role_list == template:
            logger.debug('%s does match the template', user_id)
        else:
            print(f'{primary_id} does not match the template')
