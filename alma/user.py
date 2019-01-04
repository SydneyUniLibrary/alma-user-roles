# -*- coding: utf-8 -*-

import logging


__all__ = [
    'fixup_alma_user'
]


logger = logging.getLogger('alma.user')


def fixup_alma_user(alma_user: dict) -> None:
    try:
        user_title_value = alma_user['user_title']['value']
        alma_user['user_title']['value'] = user_title_value.upper()
        if user_title_value != alma_user['user_title']['value']:
            logger.debug('Change user title value from %r to %r', user_title_value, alma_user['user_title']['value'])
    except KeyError:
        pass
