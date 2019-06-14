# -*- coding: utf-8 -*-

import logging
import typing

import alma
import alma_sdk
import alma_sdk.rest


logger = logging.getLogger('user_roles.set_job_category')


def set_job_category(api_client: alma_sdk.ApiClient, user_id_list: typing.List[str], job_category_code: str):
    users_api = alma_sdk.UsersApi(api_client)
    for user_id in user_id_list:
        logger.debug('Getting user %s', user_id)
        try:
            with alma.AlmaException.wrapped():
                user = users_api.getalmawsv1usersuser_id(user_id)
        except alma.AlmaException as e:
            logger.warning('Failed to set job category of user %s: %s', user_id, e)
            continue
        primary_id = user['primary_id']
        logger.debug('Got user %r', primary_id)
        alma.fixup_alma_user(user)
        user['job_category'] = {'value': job_category_code}
        logger.debug('Setting roles of user %s', primary_id)
        try:
            with alma.AlmaException.wrapped():
                users_api.putalmawsv1usersuser_id(user, user['primary_id'])
            logger.info('%s updated', user_id)
        except alma.AlmaException as e:
            logger.warning('Failed to set job category of user %s: %s', user_id, e)
