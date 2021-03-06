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


class ResearcherEducation2(object):
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
        'organization_code': 'str',
        'organization_name': 'str',
        'degree': 'str',
        'year': 'int',
        'field_of_study': 'str'
    }

    attribute_map = {
        'organization_code': 'organization_code',
        'organization_name': 'organization_name',
        'degree': 'degree',
        'year': 'year',
        'field_of_study': 'field_of_study'
    }

    def __init__(self, organization_code=None, organization_name=None, degree=None, year=None, field_of_study=None):  # noqa: E501
        """ResearcherEducation2 - a model defined in Swagger"""  # noqa: E501
        self._organization_code = None
        self._organization_name = None
        self._degree = None
        self._year = None
        self._field_of_study = None
        self.discriminator = None
        if organization_code is not None:
            self.organization_code = organization_code
        if organization_name is not None:
            self.organization_name = organization_name
        if degree is not None:
            self.degree = degree
        if year is not None:
            self.year = year
        if field_of_study is not None:
            self.field_of_study = field_of_study

    @property
    def organization_code(self):
        """Gets the organization_code of this ResearcherEducation2.  # noqa: E501

        The researcher's education organization code.  # noqa: E501

        :return: The organization_code of this ResearcherEducation2.  # noqa: E501
        :rtype: str
        """
        return self._organization_code

    @organization_code.setter
    def organization_code(self, organization_code):
        """Sets the organization_code of this ResearcherEducation2.

        The researcher's education organization code.  # noqa: E501

        :param organization_code: The organization_code of this ResearcherEducation2.  # noqa: E501
        :type: str
        """

        self._organization_code = organization_code

    @property
    def organization_name(self):
        """Gets the organization_name of this ResearcherEducation2.  # noqa: E501

        The researcher's education organization name.  # noqa: E501

        :return: The organization_name of this ResearcherEducation2.  # noqa: E501
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """Sets the organization_name of this ResearcherEducation2.

        The researcher's education organization name.  # noqa: E501

        :param organization_name: The organization_name of this ResearcherEducation2.  # noqa: E501
        :type: str
        """

        self._organization_name = organization_name

    @property
    def degree(self):
        """Gets the degree of this ResearcherEducation2.  # noqa: E501

        The researcher's education degree.  # noqa: E501

        :return: The degree of this ResearcherEducation2.  # noqa: E501
        :rtype: str
        """
        return self._degree

    @degree.setter
    def degree(self, degree):
        """Sets the degree of this ResearcherEducation2.

        The researcher's education degree.  # noqa: E501

        :param degree: The degree of this ResearcherEducation2.  # noqa: E501
        :type: str
        """

        self._degree = degree

    @property
    def year(self):
        """Gets the year of this ResearcherEducation2.  # noqa: E501

        The researcher's education year.  # noqa: E501

        :return: The year of this ResearcherEducation2.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this ResearcherEducation2.

        The researcher's education year.  # noqa: E501

        :param year: The year of this ResearcherEducation2.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def field_of_study(self):
        """Gets the field_of_study of this ResearcherEducation2.  # noqa: E501

        The researcher's education field_of_study.  # noqa: E501

        :return: The field_of_study of this ResearcherEducation2.  # noqa: E501
        :rtype: str
        """
        return self._field_of_study

    @field_of_study.setter
    def field_of_study(self, field_of_study):
        """Sets the field_of_study of this ResearcherEducation2.

        The researcher's education field_of_study.  # noqa: E501

        :param field_of_study: The field_of_study of this ResearcherEducation2.  # noqa: E501
        :type: str
        """

        self._field_of_study = field_of_study

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
        if issubclass(ResearcherEducation2, dict):
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
        if not isinstance(other, ResearcherEducation2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
