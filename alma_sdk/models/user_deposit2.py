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
from alma_sdk.models.rest_notes import RestNotes  # noqa: F401,E501


class UserDeposit2(object):
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
        'user_primary_id': 'str',
        'deposit_id': 'str',
        'title': 'str',
        'deposit_profile': 'str',
        'status': 'str',
        'notes': 'RestNotes',
        'mms_id': 'str',
        'rep_id': 'str',
        'delivery_url': 'str',
        'submission_date': 'date',
        'modification_date': 'date'
    }

    attribute_map = {
        'link': 'link',
        'user_primary_id': 'user_primary_id',
        'deposit_id': 'deposit_id',
        'title': 'title',
        'deposit_profile': 'deposit_profile',
        'status': 'status',
        'notes': 'notes',
        'mms_id': 'mms_id',
        'rep_id': 'rep_id',
        'delivery_url': 'delivery_url',
        'submission_date': 'submission_date',
        'modification_date': 'modification_date'
    }

    def __init__(self, link=None, user_primary_id=None, deposit_id=None, title=None, deposit_profile=None, status=None, notes=None, mms_id=None, rep_id=None, delivery_url=None, submission_date=None, modification_date=None):  # noqa: E501
        """UserDeposit2 - a model defined in Swagger"""  # noqa: E501
        self._link = None
        self._user_primary_id = None
        self._deposit_id = None
        self._title = None
        self._deposit_profile = None
        self._status = None
        self._notes = None
        self._mms_id = None
        self._rep_id = None
        self._delivery_url = None
        self._submission_date = None
        self._modification_date = None
        self.discriminator = None
        if link is not None:
            self.link = link
        self.user_primary_id = user_primary_id
        self.deposit_id = deposit_id
        self.title = title
        self.deposit_profile = deposit_profile
        self.status = status
        if notes is not None:
            self.notes = notes
        self.mms_id = mms_id
        self.rep_id = rep_id
        self.delivery_url = delivery_url
        self.submission_date = submission_date
        if modification_date is not None:
            self.modification_date = modification_date

    @property
    def link(self):
        """Gets the link of this UserDeposit2.  # noqa: E501


        :return: The link of this UserDeposit2.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this UserDeposit2.


        :param link: The link of this UserDeposit2.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def user_primary_id(self):
        """Gets the user_primary_id of this UserDeposit2.  # noqa: E501

        The primary identifier of the requesting user. Output parameter.  # noqa: E501

        :return: The user_primary_id of this UserDeposit2.  # noqa: E501
        :rtype: str
        """
        return self._user_primary_id

    @user_primary_id.setter
    def user_primary_id(self, user_primary_id):
        """Sets the user_primary_id of this UserDeposit2.

        The primary identifier of the requesting user. Output parameter.  # noqa: E501

        :param user_primary_id: The user_primary_id of this UserDeposit2.  # noqa: E501
        :type: str
        """
        if user_primary_id is None:
            raise ValueError("Invalid value for `user_primary_id`, must not be `None`")  # noqa: E501

        self._user_primary_id = user_primary_id

    @property
    def deposit_id(self):
        """Gets the deposit_id of this UserDeposit2.  # noqa: E501

        The identifier of the deposit in Alma. Should be used in subsequent queries regarding the deposit. Output parameter.  # noqa: E501

        :return: The deposit_id of this UserDeposit2.  # noqa: E501
        :rtype: str
        """
        return self._deposit_id

    @deposit_id.setter
    def deposit_id(self, deposit_id):
        """Sets the deposit_id of this UserDeposit2.

        The identifier of the deposit in Alma. Should be used in subsequent queries regarding the deposit. Output parameter.  # noqa: E501

        :param deposit_id: The deposit_id of this UserDeposit2.  # noqa: E501
        :type: str
        """
        if deposit_id is None:
            raise ValueError("Invalid value for `deposit_id`, must not be `None`")  # noqa: E501

        self._deposit_id = deposit_id

    @property
    def title(self):
        """Gets the title of this UserDeposit2.  # noqa: E501

        The title of the requested deposit.  # noqa: E501

        :return: The title of this UserDeposit2.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UserDeposit2.

        The title of the requested deposit.  # noqa: E501

        :param title: The title of this UserDeposit2.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def deposit_profile(self):
        """Gets the deposit_profile of this UserDeposit2.  # noqa: E501

        The deposit profile that determines how the deposit activity is processed. Mandatory. A list of available deposit profiles can be retrieved using the /almaws/v1/conf/deposit-profiles API.  # noqa: E501

        :return: The deposit_profile of this UserDeposit2.  # noqa: E501
        :rtype: str
        """
        return self._deposit_profile

    @deposit_profile.setter
    def deposit_profile(self, deposit_profile):
        """Sets the deposit_profile of this UserDeposit2.

        The deposit profile that determines how the deposit activity is processed. Mandatory. A list of available deposit profiles can be retrieved using the /almaws/v1/conf/deposit-profiles API.  # noqa: E501

        :param deposit_profile: The deposit_profile of this UserDeposit2.  # noqa: E501
        :type: str
        """
        if deposit_profile is None:
            raise ValueError("Invalid value for `deposit_profile`, must not be `None`")  # noqa: E501

        self._deposit_profile = deposit_profile

    @property
    def status(self):
        """Gets the status of this UserDeposit2.  # noqa: E501

        Status of the deposit. Possible values are: PENDING, RETURNED, DECLINED, WITHDRAWN, APPROVED.  # noqa: E501

        :return: The status of this UserDeposit2.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserDeposit2.

        Status of the deposit. Possible values are: PENDING, RETURNED, DECLINED, WITHDRAWN, APPROVED.  # noqa: E501

        :param status: The status of this UserDeposit2.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def notes(self):
        """Gets the notes of this UserDeposit2.  # noqa: E501


        :return: The notes of this UserDeposit2.  # noqa: E501
        :rtype: RestNotes
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this UserDeposit2.


        :param notes: The notes of this UserDeposit2.  # noqa: E501
        :type: RestNotes
        """

        self._notes = notes

    @property
    def mms_id(self):
        """Gets the mms_id of this UserDeposit2.  # noqa: E501

        MMS_ID of the record associated with the deposit. Mandatory. Record will be suppressed.  # noqa: E501

        :return: The mms_id of this UserDeposit2.  # noqa: E501
        :rtype: str
        """
        return self._mms_id

    @mms_id.setter
    def mms_id(self, mms_id):
        """Sets the mms_id of this UserDeposit2.

        MMS_ID of the record associated with the deposit. Mandatory. Record will be suppressed.  # noqa: E501

        :param mms_id: The mms_id of this UserDeposit2.  # noqa: E501
        :type: str
        """
        if mms_id is None:
            raise ValueError("Invalid value for `mms_id`, must not be `None`")  # noqa: E501

        self._mms_id = mms_id

    @property
    def rep_id(self):
        """Gets the rep_id of this UserDeposit2.  # noqa: E501

        PID of the representation associated with the deposit. Mandatory.  # noqa: E501

        :return: The rep_id of this UserDeposit2.  # noqa: E501
        :rtype: str
        """
        return self._rep_id

    @rep_id.setter
    def rep_id(self, rep_id):
        """Sets the rep_id of this UserDeposit2.

        PID of the representation associated with the deposit. Mandatory.  # noqa: E501

        :param rep_id: The rep_id of this UserDeposit2.  # noqa: E501
        :type: str
        """
        if rep_id is None:
            raise ValueError("Invalid value for `rep_id`, must not be `None`")  # noqa: E501

        self._rep_id = rep_id

    @property
    def delivery_url(self):
        """Gets the delivery_url of this UserDeposit2.  # noqa: E501

        Delivery URL of the representation associated with the deposit. Output parameter.  # noqa: E501

        :return: The delivery_url of this UserDeposit2.  # noqa: E501
        :rtype: str
        """
        return self._delivery_url

    @delivery_url.setter
    def delivery_url(self, delivery_url):
        """Sets the delivery_url of this UserDeposit2.

        Delivery URL of the representation associated with the deposit. Output parameter.  # noqa: E501

        :param delivery_url: The delivery_url of this UserDeposit2.  # noqa: E501
        :type: str
        """
        if delivery_url is None:
            raise ValueError("Invalid value for `delivery_url`, must not be `None`")  # noqa: E501

        self._delivery_url = delivery_url

    @property
    def submission_date(self):
        """Gets the submission_date of this UserDeposit2.  # noqa: E501

        The date the deposit activity was created. Output parameter.  # noqa: E501

        :return: The submission_date of this UserDeposit2.  # noqa: E501
        :rtype: date
        """
        return self._submission_date

    @submission_date.setter
    def submission_date(self, submission_date):
        """Sets the submission_date of this UserDeposit2.

        The date the deposit activity was created. Output parameter.  # noqa: E501

        :param submission_date: The submission_date of this UserDeposit2.  # noqa: E501
        :type: date
        """
        if submission_date is None:
            raise ValueError("Invalid value for `submission_date`, must not be `None`")  # noqa: E501

        self._submission_date = submission_date

    @property
    def modification_date(self):
        """Gets the modification_date of this UserDeposit2.  # noqa: E501

        The date the deposit activity was modified. Output parameter.  # noqa: E501

        :return: The modification_date of this UserDeposit2.  # noqa: E501
        :rtype: date
        """
        return self._modification_date

    @modification_date.setter
    def modification_date(self, modification_date):
        """Sets the modification_date of this UserDeposit2.

        The date the deposit activity was modified. Output parameter.  # noqa: E501

        :param modification_date: The modification_date of this UserDeposit2.  # noqa: E501
        :type: date
        """

        self._modification_date = modification_date

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
        if issubclass(UserDeposit2, dict):
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
        if not isinstance(other, UserDeposit2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other