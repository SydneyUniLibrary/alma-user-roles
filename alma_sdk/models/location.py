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


class Location(object):
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
        'quantity': 'int',
        'library': 'object',
        'shelving_location': 'str'
    }

    attribute_map = {
        'quantity': 'quantity',
        'library': 'library',
        'shelving_location': 'shelving_location'
    }

    def __init__(self, quantity=None, library=None, shelving_location=None):  # noqa: E501
        """Location - a model defined in Swagger"""  # noqa: E501
        self._quantity = None
        self._library = None
        self._shelving_location = None
        self.discriminator = None
        self.quantity = quantity
        if library is not None:
            self.library = library
        if shelving_location is not None:
            self.shelving_location = shelving_location

    @property
    def quantity(self):
        """Gets the quantity of this Location.  # noqa: E501

        The quantity per location.  # noqa: E501

        :return: The quantity of this Location.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Location.

        The quantity per location.  # noqa: E501

        :param quantity: The quantity of this Location.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def library(self):
        """Gets the library of this Location.  # noqa: E501

        The library which the location belongs to.  # noqa: E501

        :return: The library of this Location.  # noqa: E501
        :rtype: object
        """
        return self._library

    @library.setter
    def library(self, library):
        """Sets the library of this Location.

        The library which the location belongs to.  # noqa: E501

        :param library: The library of this Location.  # noqa: E501
        :type: object
        """

        self._library = library

    @property
    def shelving_location(self):
        """Gets the shelving_location of this Location.  # noqa: E501

        The location.  # noqa: E501

        :return: The shelving_location of this Location.  # noqa: E501
        :rtype: str
        """
        return self._shelving_location

    @shelving_location.setter
    def shelving_location(self, shelving_location):
        """Sets the shelving_location of this Location.

        The location.  # noqa: E501

        :param shelving_location: The shelving_location of this Location.  # noqa: E501
        :type: str
        """

        self._shelving_location = shelving_location

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
        if issubclass(Location, dict):
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
        if not isinstance(other, Location):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
