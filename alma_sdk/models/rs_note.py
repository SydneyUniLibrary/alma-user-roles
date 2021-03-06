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


class RsNote(object):
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
        'content': 'str',
        'created_date': 'date',
        'created_by': 'str'
    }

    attribute_map = {
        'content': 'content',
        'created_date': 'created_date',
        'created_by': 'created_by'
    }

    def __init__(self, content=None, created_date=None, created_by=None):  # noqa: E501
        """RsNote - a model defined in Swagger"""  # noqa: E501
        self._content = None
        self._created_date = None
        self._created_by = None
        self.discriminator = None
        if content is not None:
            self.content = content
        if created_date is not None:
            self.created_date = created_date
        if created_by is not None:
            self.created_by = created_by

    @property
    def content(self):
        """Gets the content of this RsNote.  # noqa: E501

        The note's text. Mandatory.  # noqa: E501

        :return: The content of this RsNote.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this RsNote.

        The note's text. Mandatory.  # noqa: E501

        :param content: The content of this RsNote.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def created_date(self):
        """Gets the created_date of this RsNote.  # noqa: E501

        The creation date of the note. Default is the current date.  # noqa: E501

        :return: The created_date of this RsNote.  # noqa: E501
        :rtype: date
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this RsNote.

        The creation date of the note. Default is the current date.  # noqa: E501

        :param created_date: The created_date of this RsNote.  # noqa: E501
        :type: date
        """

        self._created_date = created_date

    @property
    def created_by(self):
        """Gets the created_by of this RsNote.  # noqa: E501

        The creator of the note.  # noqa: E501

        :return: The created_by of this RsNote.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this RsNote.

        The creator of the note.  # noqa: E501

        :param created_by: The created_by of this RsNote.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

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
        if issubclass(RsNote, dict):
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
        if not isinstance(other, RsNote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
