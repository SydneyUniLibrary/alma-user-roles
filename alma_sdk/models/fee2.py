# coding: utf-8

"""
    Ex Libris APIs

    For more information on how to use these APIs, including how to create an API key required for authentication, see [Alma REST APIs](https://developers.exlibrisgroup.com/alma/apis).  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from alma_sdk.models.transactions2 import Transactions2  # noqa: F401,E501


class Fee2(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'link': 'str',
        'id': 'str',
        'type': 'object',
        'status': 'object',
        'user_primary_id': 'object',
        'balance': 'float',
        'remaining_vat_amount': 'float',
        'original_amount': 'float',
        'original_vat_amount': 'float',
        'creation_time': 'date',
        'status_time': 'date',
        'comment': 'str',
        'owner': 'object',
        'title': 'str',
        'barcode': 'object',
        'transaction': 'Transactions2',
        'bursar_transaction_id': 'str'
    }

    attribute_map = {
        'link': 'link',
        'id': 'id',
        'type': 'type',
        'status': 'status',
        'user_primary_id': 'user_primary_id',
        'balance': 'balance',
        'remaining_vat_amount': 'remaining_vat_amount',
        'original_amount': 'original_amount',
        'original_vat_amount': 'original_vat_amount',
        'creation_time': 'creation_time',
        'status_time': 'status_time',
        'comment': 'comment',
        'owner': 'owner',
        'title': 'title',
        'barcode': 'barcode',
        'transaction': 'transaction',
        'bursar_transaction_id': 'bursar_transaction_id'
    }

    def __init__(self, link=None, id=None, type=None, status=None, user_primary_id=None, balance=None, remaining_vat_amount=None, original_amount=None, original_vat_amount=None, creation_time=None, status_time=None, comment=None, owner=None, title=None, barcode=None, transaction=None, bursar_transaction_id=None):  # noqa: E501
        """Fee2 - a model defined in Swagger"""  # noqa: E501
        self._link = None
        self._id = None
        self._type = None
        self._status = None
        self._user_primary_id = None
        self._balance = None
        self._remaining_vat_amount = None
        self._original_amount = None
        self._original_vat_amount = None
        self._creation_time = None
        self._status_time = None
        self._comment = None
        self._owner = None
        self._title = None
        self._barcode = None
        self._transaction = None
        self._bursar_transaction_id = None
        self.discriminator = None
        if link is not None:
            self.link = link
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if user_primary_id is not None:
            self.user_primary_id = user_primary_id
        if balance is not None:
            self.balance = balance
        if remaining_vat_amount is not None:
            self.remaining_vat_amount = remaining_vat_amount
        if original_amount is not None:
            self.original_amount = original_amount
        if original_vat_amount is not None:
            self.original_vat_amount = original_vat_amount
        if creation_time is not None:
            self.creation_time = creation_time
        if status_time is not None:
            self.status_time = status_time
        if comment is not None:
            self.comment = comment
        if owner is not None:
            self.owner = owner
        if title is not None:
            self.title = title
        if barcode is not None:
            self.barcode = barcode
        if transaction is not None:
            self.transaction = transaction
        if bursar_transaction_id is not None:
            self.bursar_transaction_id = bursar_transaction_id

    @property
    def link(self):
        """Gets the link of this Fee2.  # noqa: E501


        :return: The link of this Fee2.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this Fee2.


        :param link: The link of this Fee2.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def id(self):
        """Gets the id of this Fee2.  # noqa: E501

        Identifier of the fee in Alma. Should be used in subsequent queries regarding the fee. Output parameter.  # noqa: E501

        :return: The id of this Fee2.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Fee2.

        Identifier of the fee in Alma. Should be used in subsequent queries regarding the fee. Output parameter.  # noqa: E501

        :param id: The id of this Fee2.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Fee2.  # noqa: E501

        The fine / fee type. Mandatory.  # noqa: E501

        :return: The type of this Fee2.  # noqa: E501
        :rtype: object
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Fee2.

        The fine / fee type. Mandatory.  # noqa: E501

        :param type: The type of this Fee2.  # noqa: E501
        :type: object
        """

        self._type = type

    @property
    def status(self):
        """Gets the status of this Fee2.  # noqa: E501

        The fine / fee status.  # noqa: E501

        :return: The status of this Fee2.  # noqa: E501
        :rtype: object
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Fee2.

        The fine / fee status.  # noqa: E501

        :param status: The status of this Fee2.  # noqa: E501
        :type: object
        """

        self._status = status

    @property
    def user_primary_id(self):
        """Gets the user_primary_id of this Fee2.  # noqa: E501

        Primary ID of the charged user. Output parameter.  # noqa: E501

        :return: The user_primary_id of this Fee2.  # noqa: E501
        :rtype: object
        """
        return self._user_primary_id

    @user_primary_id.setter
    def user_primary_id(self, user_primary_id):
        """Sets the user_primary_id of this Fee2.

        Primary ID of the charged user. Output parameter.  # noqa: E501

        :param user_primary_id: The user_primary_id of this Fee2.  # noqa: E501
        :type: object
        """

        self._user_primary_id = user_primary_id

    @property
    def balance(self):
        """Gets the balance of this Fee2.  # noqa: E501

        The fine / fee balance. Output parameter.  # noqa: E501

        :return: The balance of this Fee2.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this Fee2.

        The fine / fee balance. Output parameter.  # noqa: E501

        :param balance: The balance of this Fee2.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def remaining_vat_amount(self):
        """Gets the remaining_vat_amount of this Fee2.  # noqa: E501

        The fine / fee remaining vat amount. Output parameter.  # noqa: E501

        :return: The remaining_vat_amount of this Fee2.  # noqa: E501
        :rtype: float
        """
        return self._remaining_vat_amount

    @remaining_vat_amount.setter
    def remaining_vat_amount(self, remaining_vat_amount):
        """Sets the remaining_vat_amount of this Fee2.

        The fine / fee remaining vat amount. Output parameter.  # noqa: E501

        :param remaining_vat_amount: The remaining_vat_amount of this Fee2.  # noqa: E501
        :type: float
        """

        self._remaining_vat_amount = remaining_vat_amount

    @property
    def original_amount(self):
        """Gets the original_amount of this Fee2.  # noqa: E501

        The fine / fee original amount. Mandatory for POST.  # noqa: E501

        :return: The original_amount of this Fee2.  # noqa: E501
        :rtype: float
        """
        return self._original_amount

    @original_amount.setter
    def original_amount(self, original_amount):
        """Sets the original_amount of this Fee2.

        The fine / fee original amount. Mandatory for POST.  # noqa: E501

        :param original_amount: The original_amount of this Fee2.  # noqa: E501
        :type: float
        """

        self._original_amount = original_amount

    @property
    def original_vat_amount(self):
        """Gets the original_vat_amount of this Fee2.  # noqa: E501

        The fine / fee original vat amount. Output parameter.  # noqa: E501

        :return: The original_vat_amount of this Fee2.  # noqa: E501
        :rtype: float
        """
        return self._original_vat_amount

    @original_vat_amount.setter
    def original_vat_amount(self, original_vat_amount):
        """Sets the original_vat_amount of this Fee2.

        The fine / fee original vat amount. Output parameter.  # noqa: E501

        :param original_vat_amount: The original_vat_amount of this Fee2.  # noqa: E501
        :type: float
        """

        self._original_vat_amount = original_vat_amount

    @property
    def creation_time(self):
        """Gets the creation_time of this Fee2.  # noqa: E501

        Date the fine / fee was created.  # noqa: E501

        :return: The creation_time of this Fee2.  # noqa: E501
        :rtype: date
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this Fee2.

        Date the fine / fee was created.  # noqa: E501

        :param creation_time: The creation_time of this Fee2.  # noqa: E501
        :type: date
        """

        self._creation_time = creation_time

    @property
    def status_time(self):
        """Gets the status_time of this Fee2.  # noqa: E501

        Date the fine / fee was last changed.  # noqa: E501

        :return: The status_time of this Fee2.  # noqa: E501
        :rtype: date
        """
        return self._status_time

    @status_time.setter
    def status_time(self, status_time):
        """Sets the status_time of this Fee2.

        Date the fine / fee was last changed.  # noqa: E501

        :param status_time: The status_time of this Fee2.  # noqa: E501
        :type: date
        """

        self._status_time = status_time

    @property
    def comment(self):
        """Gets the comment of this Fee2.  # noqa: E501

        Fine / fee comment.  # noqa: E501

        :return: The comment of this Fee2.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Fee2.

        Fine / fee comment.  # noqa: E501

        :param comment: The comment of this Fee2.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def owner(self):
        """Gets the owner of this Fee2.  # noqa: E501

        The fine / fee owner. Mandatory for POST.  # noqa: E501

        :return: The owner of this Fee2.  # noqa: E501
        :rtype: object
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Fee2.

        The fine / fee owner. Mandatory for POST.  # noqa: E501

        :param owner: The owner of this Fee2.  # noqa: E501
        :type: object
        """

        self._owner = owner

    @property
    def title(self):
        """Gets the title of this Fee2.  # noqa: E501

        The item title.  # noqa: E501

        :return: The title of this Fee2.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Fee2.

        The item title.  # noqa: E501

        :param title: The title of this Fee2.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def barcode(self):
        """Gets the barcode of this Fee2.  # noqa: E501

        The item barcode.  # noqa: E501

        :return: The barcode of this Fee2.  # noqa: E501
        :rtype: object
        """
        return self._barcode

    @barcode.setter
    def barcode(self, barcode):
        """Sets the barcode of this Fee2.

        The item barcode.  # noqa: E501

        :param barcode: The barcode of this Fee2.  # noqa: E501
        :type: object
        """

        self._barcode = barcode

    @property
    def transaction(self):
        """Gets the transaction of this Fee2.  # noqa: E501


        :return: The transaction of this Fee2.  # noqa: E501
        :rtype: Transactions2
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this Fee2.


        :param transaction: The transaction of this Fee2.  # noqa: E501
        :type: Transactions2
        """

        self._transaction = transaction

    @property
    def bursar_transaction_id(self):
        """Gets the bursar_transaction_id of this Fee2.  # noqa: E501

        The unique sequence used for the fine/fee identification when communicating with the Bursar system.  # noqa: E501

        :return: The bursar_transaction_id of this Fee2.  # noqa: E501
        :rtype: str
        """
        return self._bursar_transaction_id

    @bursar_transaction_id.setter
    def bursar_transaction_id(self, bursar_transaction_id):
        """Sets the bursar_transaction_id of this Fee2.

        The unique sequence used for the fine/fee identification when communicating with the Bursar system.  # noqa: E501

        :param bursar_transaction_id: The bursar_transaction_id of this Fee2.  # noqa: E501
        :type: str
        """

        self._bursar_transaction_id = bursar_transaction_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Fee2, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Fee2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other