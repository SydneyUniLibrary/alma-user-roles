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


class Fees(object):
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
        'total_record_count': 'int',
        'total_sum': 'float',
        'currency': 'str',
        'fee': 'list[object]'
    }

    attribute_map = {
        'total_record_count': 'total_record_count',
        'total_sum': 'total_sum',
        'currency': 'currency',
        'fee': 'fee'
    }

    def __init__(self, total_record_count=None, total_sum=None, currency=None, fee=None):  # noqa: E501
        """Fees - a model defined in Swagger"""  # noqa: E501
        self._total_record_count = None
        self._total_sum = None
        self._currency = None
        self._fee = None
        self.discriminator = None
        if total_record_count is not None:
            self.total_record_count = total_record_count
        if total_sum is not None:
            self.total_sum = total_sum
        if currency is not None:
            self.currency = currency
        if fee is not None:
            self.fee = fee

    @property
    def total_record_count(self):
        """Gets the total_record_count of this Fees.  # noqa: E501

        The total number of fees. This can be used when retrieving the fees list using pagination.  # noqa: E501

        :return: The total_record_count of this Fees.  # noqa: E501
        :rtype: int
        """
        return self._total_record_count

    @total_record_count.setter
    def total_record_count(self, total_record_count):
        """Sets the total_record_count of this Fees.

        The total number of fees. This can be used when retrieving the fees list using pagination.  # noqa: E501

        :param total_record_count: The total_record_count of this Fees.  # noqa: E501
        :type: int
        """

        self._total_record_count = total_record_count

    @property
    def total_sum(self):
        """Gets the total_sum of this Fees.  # noqa: E501

        The total sum of the fees.  # noqa: E501

        :return: The total_sum of this Fees.  # noqa: E501
        :rtype: float
        """
        return self._total_sum

    @total_sum.setter
    def total_sum(self, total_sum):
        """Sets the total_sum of this Fees.

        The total sum of the fees.  # noqa: E501

        :param total_sum: The total_sum of this Fees.  # noqa: E501
        :type: float
        """

        self._total_sum = total_sum

    @property
    def currency(self):
        """Gets the currency of this Fees.  # noqa: E501

        The currency code for the fees.  # noqa: E501

        :return: The currency of this Fees.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Fees.

        The currency code for the fees.  # noqa: E501

        :param currency: The currency of this Fees.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def fee(self):
        """Gets the fee of this Fees.  # noqa: E501

        Fee Object.  # noqa: E501

        :return: The fee of this Fees.  # noqa: E501
        :rtype: list[object]
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this Fees.

        Fee Object.  # noqa: E501

        :param fee: The fee of this Fees.  # noqa: E501
        :type: list[object]
        """

        self._fee = fee

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
        if issubclass(Fees, dict):
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
        if not isinstance(other, Fees):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
