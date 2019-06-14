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


class Phone(object):
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
        'preferred': 'bool',
        'preferred_sms': 'bool',
        'segment_type': 'str',
        'phone_number': 'str',
        'phone_type': 'list[object]'
    }

    attribute_map = {
        'preferred': 'preferred',
        'preferred_sms': 'preferred_sms',
        'segment_type': 'segment_type',
        'phone_number': 'phone_number',
        'phone_type': 'phone_type'
    }

    def __init__(self, preferred=None, preferred_sms=None, segment_type=None, phone_number=None, phone_type=None):  # noqa: E501
        """Phone - a model defined in Swagger"""  # noqa: E501
        self._preferred = None
        self._preferred_sms = None
        self._segment_type = None
        self._phone_number = None
        self._phone_type = None
        self.discriminator = None
        if preferred is not None:
            self.preferred = preferred
        if preferred_sms is not None:
            self.preferred_sms = preferred_sms
        if segment_type is not None:
            self.segment_type = segment_type
        if phone_number is not None:
            self.phone_number = phone_number
        if phone_type is not None:
            self.phone_type = phone_type

    @property
    def preferred(self):
        """Gets the preferred of this Phone.  # noqa: E501

        Indication whether the phone number is the preferred one. Only one address can be defined as preferred.  # noqa: E501

        :return: The preferred of this Phone.  # noqa: E501
        :rtype: bool
        """
        return self._preferred

    @preferred.setter
    def preferred(self, preferred):
        """Sets the preferred of this Phone.

        Indication whether the phone number is the preferred one. Only one address can be defined as preferred.  # noqa: E501

        :param preferred: The preferred of this Phone.  # noqa: E501
        :type: bool
        """

        self._preferred = preferred

    @property
    def preferred_sms(self):
        """Gets the preferred_sms of this Phone.  # noqa: E501

        Indication whether the phone number is the preferred one for SMS sending. Only one phone number can be defined as preferred.  # noqa: E501

        :return: The preferred_sms of this Phone.  # noqa: E501
        :rtype: bool
        """
        return self._preferred_sms

    @preferred_sms.setter
    def preferred_sms(self, preferred_sms):
        """Sets the preferred_sms of this Phone.

        Indication whether the phone number is the preferred one for SMS sending. Only one phone number can be defined as preferred.  # noqa: E501

        :param preferred_sms: The preferred_sms of this Phone.  # noqa: E501
        :type: bool
        """

        self._preferred_sms = preferred_sms

    @property
    def segment_type(self):
        """Gets the segment_type of this Phone.  # noqa: E501

        The type of the segment (Internal or External). Relevant only for User API (and not for SIS). For internal users, all the segments are considered internal. External users might have internal or external segments. Empty or illegal segment_type for external user will be considered as external.  # noqa: E501

        :return: The segment_type of this Phone.  # noqa: E501
        :rtype: str
        """
        return self._segment_type

    @segment_type.setter
    def segment_type(self, segment_type):
        """Sets the segment_type of this Phone.

        The type of the segment (Internal or External). Relevant only for User API (and not for SIS). For internal users, all the segments are considered internal. External users might have internal or external segments. Empty or illegal segment_type for external user will be considered as external.  # noqa: E501

        :param segment_type: The segment_type of this Phone.  # noqa: E501
        :type: str
        """

        self._segment_type = segment_type

    @property
    def phone_number(self):
        """Gets the phone_number of this Phone.  # noqa: E501

        The phone number. Mandatory.  # noqa: E501

        :return: The phone_number of this Phone.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this Phone.

        The phone number. Mandatory.  # noqa: E501

        :param phone_number: The phone_number of this Phone.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def phone_type(self):
        """Gets the phone_type of this Phone.  # noqa: E501

        The different Phone types. Mandatory.  # noqa: E501

        :return: The phone_type of this Phone.  # noqa: E501
        :rtype: list[object]
        """
        return self._phone_type

    @phone_type.setter
    def phone_type(self, phone_type):
        """Sets the phone_type of this Phone.

        The different Phone types. Mandatory.  # noqa: E501

        :param phone_type: The phone_type of this Phone.  # noqa: E501
        :type: list[object]
        """

        self._phone_type = phone_type

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
        if issubclass(Phone, dict):
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
        if not isinstance(other, Phone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other