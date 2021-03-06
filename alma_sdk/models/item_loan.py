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


class ItemLoan(object):
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
        'circ_desk': 'object',
        'library': 'object'
    }

    attribute_map = {
        'circ_desk': 'circ_desk',
        'library': 'library'
    }

    def __init__(self, circ_desk=None, library=None):  # noqa: E501
        """ItemLoan - a model defined in Swagger"""  # noqa: E501
        self._circ_desk = None
        self._library = None
        self.discriminator = None
        self.circ_desk = circ_desk
        self.library = library

    @property
    def circ_desk(self):
        """Gets the circ_desk of this ItemLoan.  # noqa: E501

        The circulation desk code that is responsible of the loan. Mandatory.  # noqa: E501

        :return: The circ_desk of this ItemLoan.  # noqa: E501
        :rtype: object
        """
        return self._circ_desk

    @circ_desk.setter
    def circ_desk(self, circ_desk):
        """Sets the circ_desk of this ItemLoan.

        The circulation desk code that is responsible of the loan. Mandatory.  # noqa: E501

        :param circ_desk: The circ_desk of this ItemLoan.  # noqa: E501
        :type: object
        """
        if circ_desk is None:
            raise ValueError("Invalid value for `circ_desk`, must not be `None`")  # noqa: E501

        self._circ_desk = circ_desk

    @property
    def library(self):
        """Gets the library of this ItemLoan.  # noqa: E501

        The library code that is responsible of the loan. Mandatory.  # noqa: E501

        :return: The library of this ItemLoan.  # noqa: E501
        :rtype: object
        """
        return self._library

    @library.setter
    def library(self, library):
        """Sets the library of this ItemLoan.

        The library code that is responsible of the loan. Mandatory.  # noqa: E501

        :param library: The library of this ItemLoan.  # noqa: E501
        :type: object
        """
        if library is None:
            raise ValueError("Invalid value for `library`, must not be `None`")  # noqa: E501

        self._library = library

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
        if issubclass(ItemLoan, dict):
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
        if not isinstance(other, ItemLoan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
