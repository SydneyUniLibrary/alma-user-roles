# -*- coding: utf-8 -*-


import logging
import json
import sys

import alma


logger = logging.getLogger('user_roles.get_user_roles')


def get_user_roles(alma_client: alma.ApiClient, user_id: str,
                   include_inactive: bool = False, verbose: bool = False):
    logger.debug('Getting roles of user %s', user_id)
    user = alma_client.get_user_details(user_id)
    primary_id = user['primary_id']
    logger.debug('Got user %r', primary_id)
    user_role_list = [
        user_role
        for user_role in user.get('user_role') or []
        if include_inactive or alma.is_user_role_active(user_role)
    ]
    json.dump(user_role_list, sys.stdout, indent=2 if verbose else None)
