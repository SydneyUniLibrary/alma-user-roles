# -*- coding: utf-8 -*-


__all__ = [
    'is_user_role_active'
]


def is_user_role_active(user_role: dict) -> bool:
    try:
        return user_role['status']['value'] == 'ACTIVE'
    except KeyError:
        return False
