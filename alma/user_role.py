# -*- coding: utf-8 -*-

__all__ = [
    'get_role_type_value',
    'get_scope_value',
    'is_user_role_active',
]


def get_role_type_value(user_role: dict) -> str:
    try:
        return user_role['role_type']['value']
    except KeyError:
        return ''


def get_scope_value(user_role: dict) -> str:
    try:
        return user_role['scope']['value']
    except KeyError:
        return ''


def is_user_role_active(user_role: dict) -> bool:
    try:
        return user_role['status']['value'] == 'ACTIVE'
    except KeyError:
        return False
