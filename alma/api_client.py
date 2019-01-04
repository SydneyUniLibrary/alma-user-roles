# -*- coding: utf-8 -*-

import json
import logging
import requests
import typing


logger = logging.getLogger('alma.api_client')


class ApiClientError(Exception):

    def __init__(self, error_code: str, error_message: str, tracking_id: typing.Optional[str]=None):
        super().__init__(f'{error_message} (code {error_code})')
        self.error_code = error_code
        self.error_message = error_message
        self.tracking_id = tracking_id


class InvalidApiKeyError(ApiClientError):

    ERROR_CODE = 'INVALID_API_KEY'

    def __init__(self):
        super().__init__(InvalidApiKeyError.ERROR_CODE, 'Invalid API Key')


def _raise_for_status(resp):
    if resp.ok:
        return
    try:
        json_resp = resp.json()
    except json.JSONDecodeError as e:
        json_resp = None
    if json_resp is None and resp.content == b'Invalid API Key':
        raise InvalidApiKeyError()
    if json_resp is None or not isinstance(json_resp, dict) or not json_resp.get('errorsExist'):
        logger.warning('Unknown API response: %s', resp.content)
        resp.raise_for_status()
    else:
        error_list = (json_resp.get('errorList') or {}).get('error') or []
        if len(error_list) == 0:
            resp.raise_for_status()
        if len(error_list) > 1:
            logger.warning('Multiple errors: %r', error_list)
        error = error_list[0]
        raise ApiClientError(error.get('errorCode'), error.get('errorMessage') or '«unknown»', error.get('trackingId'))


class ApiClient:

    def create_user(self, alma_user: dict, **kwargs) -> dict:
        raise NotImplementedError()

    def get_user_details(self, user_id: str, **kwargs) -> typing.Optional[dict]:
        raise NotImplementedError()

    def update_user_details(self, alma_user: dict, **kwargs) -> dict:
        raise NotImplementedError()


class RequestsApiClient(ApiClient):

    def __init__(self, api_server: str, api_key: str):
        self.api_server = api_server
        self.session = requests.Session()
        self.session.headers = {'Accept': 'application/json', 'Authorization': f'apikey {api_key}'}

    def create_user(self, alma_user: dict, **kwargs) -> dict:
        user_id = alma_user["primary_id"]
        logger.debug('Create user %s as %r', user_id, alma_user)
        resp = self.session.post(f'https://{self.api_server}/almaws/v1/users', json=alma_user, params=kwargs)
        _raise_for_status(resp)
        alma_user = resp.json()
        logger.debug('Got created user %r', alma_user)
        return alma_user

    def get_user_details(self, user_id: str, **kwargs) -> typing.Optional[dict]:
        logger.debug('Getting user %s from %s', user_id, self.api_server)
        resp = self.session.get(f'https://{self.api_server}/almaws/v1/users/{user_id}', params=kwargs)
        try:
            _raise_for_status(resp)
        except ApiClientError as e:
            logger.debug('Got error %r', e)
            if e.error_code == '401890' or e.error_code == '401861' or e.error_code == '4019990' or e.error_code == '4019998':
                logger.debug('User %s not found', user_id)
                return None
            else:
                raise e
        user = resp.json()
        logger.debug('Got user %r', user)
        return user

    def update_user_details(self, alma_user: dict, **kwargs) -> dict:
        user_id = alma_user["primary_id"]
        logger.debug('Updating user %s to %r', user_id, alma_user)
        resp = self.session.put(f'https://{self.api_server}/almaws/v1/users/{user_id}',
                                json=alma_user, params=kwargs)
        _raise_for_status(resp)
        alma_user = resp.json()
        logger.debug('Got updated user %r', alma_user)
        return alma_user

    def test_user_read_permissions(self):
        resp = self.session.get(f'https://{self.api_server}/almaws/v1/users/operation/test')
        _raise_for_status(resp)

    def test_user_write_permissions(self):
        resp = self.session.post(f'https://{self.api_server}/almaws/v1/users/operation/test')
        _raise_for_status(resp)
