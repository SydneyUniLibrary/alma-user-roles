# -*- coding: utf-8 -*-

from __future__ import annotations

from abc import abstractmethod
from typing import Sequence

import alma_sdk.rest
import collections.abc
import contextlib
import json
import typing

__all__ = (
    'AlmaException',
)


class AlmaError(typing.NamedTuple):
    error_code: str
    error_message: str
    tracking_id: str

    @staticmethod
    def from_api_exception(api_exception_error_list: typing.Dict[str ,str]) -> AlmaError:
        error_code = api_exception_error_list.get('errorCode') or ''
        error_message = api_exception_error_list.get('errorMessage') or ''
        tracking_id = api_exception_error_list.get('trackingId') or ''
        return AlmaError(error_code, error_message, tracking_id)


class AlmaException(Exception, collections.abc.Sequence):

    @staticmethod
    def from_api_exception(api_exception: alma_sdk.rest.ApiException) -> AlmaException:
        body = api_exception.body or ''
        try:
            json_body = json.loads(body)
            error_list = json_body['errorList']['error']
        except:
            error_list = [{
                'errorCode': '',
                'errorMessage': str(body),
                'trackingId': '',
            }]
        return AlmaException([AlmaError.from_api_exception(x) for x in error_list])

    @staticmethod
    @contextlib.contextmanager
    def wrapped():
        try:
            yield
        except alma_sdk.rest.ApiException as e:
            raise AlmaException.from_api_exception(e)

    def __init__(self, error_list: typing.List[AlmaError]):
        super().__init__()
        self.error_list = error_list

    @property
    def error_code(self) -> str:
        try:
            return self.error_list[0].error_code
        except IndexError:
            return ''

    @property
    def error_message(self) -> str:
        try:
            return self.error_list[0].error_message
        except IndexError:
            return ''

    @property
    def tracking_id(self) -> str:
        try:
            return self.error_list[0].tracking_id
        except IndexError:
            return ''

    def __str__(self) -> str:
        return f'{self.error_message} ({self.error_code})'

    def __repr__(self) -> str:
        return f'AlmaException({self.error_list!r})'

    @typing.overload
    @abstractmethod
    def __getitem__(self, i: int) -> AlmaError: ...

    @typing.overload
    @abstractmethod
    def __getitem__(self, s: slice) -> Sequence[AlmaError]: ...

    def __getitem__(self, i: int) -> AlmaError:
        return self.error_list[i]

    def __len__(self) -> int:
        return len(self.error_list)
