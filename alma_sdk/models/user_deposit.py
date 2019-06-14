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


class UserDeposit(object):
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
        'title': 'str',
        'deposit_profile': 'str',
        'notes': 'list[object]',
        'mms_id': 'str',
        'rep_id': 'str'
    }

    attribute_map = {
        'link': 'link',
        'title': 'title',
        'deposit_profile': 'deposit_profile',
        'notes': 'notes',
        'mms_id': 'mms_id',
        'rep_id': 'rep_id'
    }

    def __init__(self, link=None, title=None, deposit_profile=None, notes=None, mms_id=None, rep_id=None):  # noqa: E501
        """UserDeposit - a model defined in Swagger"""  # noqa: E501
        self._link = None
        self._title = None
        self._deposit_profile = None
        self._notes = None
        self._mms_id = None
        self._rep_id = None
        self.discriminator = None
        if link is not None:
            self.link = link
        self.title = title
        self.deposit_profile = deposit_profile
        if notes is not None:
            self.notes = notes
        self.mms_id = mms_id
        self.rep_id = rep_id

    @property
    def link(self):
        """Gets the link of this UserDeposit.  # noqa: E501


        :return: The link of this UserDeposit.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this UserDeposit.


        :param link: The link of this UserDeposit.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def title(self):
        """Gets the title of this UserDeposit.  # noqa: E501

        The title of the requested deposit.  # noqa: E501

        :return: The title of this UserDeposit.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UserDeposit.

        The title of the requested deposit.  # noqa: E501

        :param title: The title of this UserDeposit.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def deposit_profile(self):
        """Gets the deposit_profile of this UserDeposit.  # noqa: E501

        The deposit profile that determines how the deposit activity is processed. Mandatory. A list of available deposit profiles can be retrieved using the /almaws/v1/conf/deposit-profiles API.  # noqa: E501

        :return: The deposit_profile of this UserDeposit.  # noqa: E501
        :rtype: str
        """
        return self._deposit_profile

    @deposit_profile.setter
    def deposit_profile(self, deposit_profile):
        """Sets the deposit_profile of this UserDeposit.

        The deposit profile that determines how the deposit activity is processed. Mandatory. A list of available deposit profiles can be retrieved using the /almaws/v1/conf/deposit-profiles API.  # noqa: E501

        :param deposit_profile: The deposit_profile of this UserDeposit.  # noqa: E501
        :type: str
        """
        if deposit_profile is None:
            raise ValueError("Invalid value for `deposit_profile`, must not be `None`")  # noqa: E501

        self._deposit_profile = deposit_profile

    @property
    def notes(self):
        """Gets the notes of this UserDeposit.  # noqa: E501

        List of related notes. In the PUT action the incoming list will replace the existing list. If the incoming list is empty, the existing list will be deleted.  # noqa: E501

        :return: The notes of this UserDeposit.  # noqa: E501
        :rtype: list[object]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this UserDeposit.

        List of related notes. In the PUT action the incoming list will replace the existing list. If the incoming list is empty, the existing list will be deleted.  # noqa: E501

        :param notes: The notes of this UserDeposit.  # noqa: E501
        :type: list[object]
        """

        self._notes = notes

    @property
    def mms_id(self):
        """Gets the mms_id of this UserDeposit.  # noqa: E501

        MMS_ID of the record associated with the deposit. Mandatory. Record will be suppressed.  # noqa: E501

        :return: The mms_id of this UserDeposit.  # noqa: E501
        :rtype: str
        """
        return self._mms_id

    @mms_id.setter
    def mms_id(self, mms_id):
        """Sets the mms_id of this UserDeposit.

        MMS_ID of the record associated with the deposit. Mandatory. Record will be suppressed.  # noqa: E501

        :param mms_id: The mms_id of this UserDeposit.  # noqa: E501
        :type: str
        """
        if mms_id is None:
            raise ValueError("Invalid value for `mms_id`, must not be `None`")  # noqa: E501

        self._mms_id = mms_id

    @property
    def rep_id(self):
        """Gets the rep_id of this UserDeposit.  # noqa: E501

        PID of the representation associated with the deposit. Mandatory.  # noqa: E501

        :return: The rep_id of this UserDeposit.  # noqa: E501
        :rtype: str
        """
        return self._rep_id

    @rep_id.setter
    def rep_id(self, rep_id):
        """Sets the rep_id of this UserDeposit.

        PID of the representation associated with the deposit. Mandatory.  # noqa: E501

        :param rep_id: The rep_id of this UserDeposit.  # noqa: E501
        :type: str
        """
        if rep_id is None:
            raise ValueError("Invalid value for `rep_id`, must not be `None`")  # noqa: E501

        self._rep_id = rep_id

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
        if issubclass(UserDeposit, dict):
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
        if not isinstance(other, UserDeposit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
