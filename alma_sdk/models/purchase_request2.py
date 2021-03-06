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
from alma_sdk.models.amount2 import Amount2  # noqa: F401,E501
from alma_sdk.models.locations2 import Locations2  # noqa: F401,E501
from alma_sdk.models.resource_metadata2 import ResourceMetadata2  # noqa: F401,E501
from alma_sdk.models.rest_notes import RestNotes  # noqa: F401,E501


class PurchaseRequest2(object):
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
        'request_id': 'str',
        'created_date': 'date',
        'last_modified_date': 'date',
        'format': 'object',
        'requester': 'object',
        'created_from': 'object',
        'status': 'object',
        'owning_library': 'object',
        'estimated_cost': 'Amount2',
        'fund': 'object',
        'vendor': 'object',
        'vendor_account': 'str',
        'approved_by': 'str',
        'requester_note': 'str',
        'reject_reason': 'object',
        'resource_metadata': 'ResourceMetadata2',
        'notes': 'RestNotes',
        'location': 'Locations2'
    }

    attribute_map = {
        'request_id': 'request_id',
        'created_date': 'created_date',
        'last_modified_date': 'last_modified_date',
        'format': 'format',
        'requester': 'requester',
        'created_from': 'created_from',
        'status': 'status',
        'owning_library': 'owning_library',
        'estimated_cost': 'estimated_cost',
        'fund': 'fund',
        'vendor': 'vendor',
        'vendor_account': 'vendor_account',
        'approved_by': 'approved_by',
        'requester_note': 'requester_note',
        'reject_reason': 'reject_reason',
        'resource_metadata': 'resource_metadata',
        'notes': 'notes',
        'location': 'location'
    }

    def __init__(self, request_id=None, created_date=None, last_modified_date=None, format=None, requester=None, created_from=None, status=None, owning_library=None, estimated_cost=None, fund=None, vendor=None, vendor_account=None, approved_by=None, requester_note=None, reject_reason=None, resource_metadata=None, notes=None, location=None):  # noqa: E501
        """PurchaseRequest2 - a model defined in Swagger"""  # noqa: E501
        self._request_id = None
        self._created_date = None
        self._last_modified_date = None
        self._format = None
        self._requester = None
        self._created_from = None
        self._status = None
        self._owning_library = None
        self._estimated_cost = None
        self._fund = None
        self._vendor = None
        self._vendor_account = None
        self._approved_by = None
        self._requester_note = None
        self._reject_reason = None
        self._resource_metadata = None
        self._notes = None
        self._location = None
        self.discriminator = None
        if request_id is not None:
            self.request_id = request_id
        if created_date is not None:
            self.created_date = created_date
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date
        if format is not None:
            self.format = format
        if requester is not None:
            self.requester = requester
        if created_from is not None:
            self.created_from = created_from
        if status is not None:
            self.status = status
        if owning_library is not None:
            self.owning_library = owning_library
        if estimated_cost is not None:
            self.estimated_cost = estimated_cost
        if fund is not None:
            self.fund = fund
        if vendor is not None:
            self.vendor = vendor
        if vendor_account is not None:
            self.vendor_account = vendor_account
        if approved_by is not None:
            self.approved_by = approved_by
        if requester_note is not None:
            self.requester_note = requester_note
        if reject_reason is not None:
            self.reject_reason = reject_reason
        self.resource_metadata = resource_metadata
        if notes is not None:
            self.notes = notes
        if location is not None:
            self.location = location

    @property
    def request_id(self):
        """Gets the request_id of this PurchaseRequest2.  # noqa: E501

        Internal identifier of the request in Alma, generated by Alma. Should be used in subsequent queries regarding the request. Output parameter.  # noqa: E501

        :return: The request_id of this PurchaseRequest2.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this PurchaseRequest2.

        Internal identifier of the request in Alma, generated by Alma. Should be used in subsequent queries regarding the request. Output parameter.  # noqa: E501

        :param request_id: The request_id of this PurchaseRequest2.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def created_date(self):
        """Gets the created_date of this PurchaseRequest2.  # noqa: E501

        The request creation date. Output parameter.  # noqa: E501

        :return: The created_date of this PurchaseRequest2.  # noqa: E501
        :rtype: date
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this PurchaseRequest2.

        The request creation date. Output parameter.  # noqa: E501

        :param created_date: The created_date of this PurchaseRequest2.  # noqa: E501
        :type: date
        """

        self._created_date = created_date

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this PurchaseRequest2.  # noqa: E501

        Date by which the last change to the request was made. Output parameter.  # noqa: E501

        :return: The last_modified_date of this PurchaseRequest2.  # noqa: E501
        :rtype: date
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this PurchaseRequest2.

        Date by which the last change to the request was made. Output parameter.  # noqa: E501

        :param last_modified_date: The last_modified_date of this PurchaseRequest2.  # noqa: E501
        :type: date
        """

        self._last_modified_date = last_modified_date

    @property
    def format(self):
        """Gets the format of this PurchaseRequest2.  # noqa: E501

        Whether the item should be acquired in electronic or physical format. Possible values are listed in 'PR_RequestedFormat' [code table](https://developers.exlibrisgroup.com/blog/Working-with-the-code-tables-API). Default is Physical.  # noqa: E501

        :return: The format of this PurchaseRequest2.  # noqa: E501
        :rtype: object
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this PurchaseRequest2.

        Whether the item should be acquired in electronic or physical format. Possible values are listed in 'PR_RequestedFormat' [code table](https://developers.exlibrisgroup.com/blog/Working-with-the-code-tables-API). Default is Physical.  # noqa: E501

        :param format: The format of this PurchaseRequest2.  # noqa: E501
        :type: object
        """

        self._format = format

    @property
    def requester(self):
        """Gets the requester of this PurchaseRequest2.  # noqa: E501

        The primary identifier and full name of the requesting user. Output parameter.  # noqa: E501

        :return: The requester of this PurchaseRequest2.  # noqa: E501
        :rtype: object
        """
        return self._requester

    @requester.setter
    def requester(self, requester):
        """Sets the requester of this PurchaseRequest2.

        The primary identifier and full name of the requesting user. Output parameter.  # noqa: E501

        :param requester: The requester of this PurchaseRequest2.  # noqa: E501
        :type: object
        """

        self._requester = requester

    @property
    def created_from(self):
        """Gets the created_from of this PurchaseRequest2.  # noqa: E501

        The place in which the request was initiated. Output parameter. Possible values are listed in 'PPRSourceType' [code table](https://developers.exlibrisgroup.com/blog/Working-with-the-code-tables-API). For purchase requests created via API, this field will be populated with API.  # noqa: E501

        :return: The created_from of this PurchaseRequest2.  # noqa: E501
        :rtype: object
        """
        return self._created_from

    @created_from.setter
    def created_from(self, created_from):
        """Sets the created_from of this PurchaseRequest2.

        The place in which the request was initiated. Output parameter. Possible values are listed in 'PPRSourceType' [code table](https://developers.exlibrisgroup.com/blog/Working-with-the-code-tables-API). For purchase requests created via API, this field will be populated with API.  # noqa: E501

        :param created_from: The created_from of this PurchaseRequest2.  # noqa: E501
        :type: object
        """

        self._created_from = created_from

    @property
    def status(self):
        """Gets the status of this PurchaseRequest2.  # noqa: E501

        The status of the request. Output parameter.  # noqa: E501

        :return: The status of this PurchaseRequest2.  # noqa: E501
        :rtype: object
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PurchaseRequest2.

        The status of the request. Output parameter.  # noqa: E501

        :param status: The status of this PurchaseRequest2.  # noqa: E501
        :type: object
        """

        self._status = status

    @property
    def owning_library(self):
        """Gets the owning_library of this PurchaseRequest2.  # noqa: E501

        The library that should receive the item. See [Get libraries API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4Dp4I8TKv6CAxBlD4LyRaVE=/37088dc9-c685-4641-bc7f-60b5ca7cabed).  # noqa: E501

        :return: The owning_library of this PurchaseRequest2.  # noqa: E501
        :rtype: object
        """
        return self._owning_library

    @owning_library.setter
    def owning_library(self, owning_library):
        """Sets the owning_library of this PurchaseRequest2.

        The library that should receive the item. See [Get libraries API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4Dp4I8TKv6CAxBlD4LyRaVE=/37088dc9-c685-4641-bc7f-60b5ca7cabed).  # noqa: E501

        :param owning_library: The owning_library of this PurchaseRequest2.  # noqa: E501
        :type: object
        """

        self._owning_library = owning_library

    @property
    def estimated_cost(self):
        """Gets the estimated_cost of this PurchaseRequest2.  # noqa: E501


        :return: The estimated_cost of this PurchaseRequest2.  # noqa: E501
        :rtype: Amount2
        """
        return self._estimated_cost

    @estimated_cost.setter
    def estimated_cost(self, estimated_cost):
        """Sets the estimated_cost of this PurchaseRequest2.


        :param estimated_cost: The estimated_cost of this PurchaseRequest2.  # noqa: E501
        :type: Amount2
        """

        self._estimated_cost = estimated_cost

    @property
    def fund(self):
        """Gets the fund of this PurchaseRequest2.  # noqa: E501

        The fund code. See [Get funds API](https://developers.exlibrisgroup.com/alma/apis/acq/GET/gwPcGly021oUHLI4O/zpt8U7ewiJYRLM/d5b14609-b590-470e-baba-9944682f8c7e).  # noqa: E501

        :return: The fund of this PurchaseRequest2.  # noqa: E501
        :rtype: object
        """
        return self._fund

    @fund.setter
    def fund(self, fund):
        """Sets the fund of this PurchaseRequest2.

        The fund code. See [Get funds API](https://developers.exlibrisgroup.com/alma/apis/acq/GET/gwPcGly021oUHLI4O/zpt8U7ewiJYRLM/d5b14609-b590-470e-baba-9944682f8c7e).  # noqa: E501

        :param fund: The fund of this PurchaseRequest2.  # noqa: E501
        :type: object
        """

        self._fund = fund

    @property
    def vendor(self):
        """Gets the vendor of this PurchaseRequest2.  # noqa: E501

        The vendor code from which to purchase the item. If vendor is supplied, vendor account should be suplied as well.  # noqa: E501

        :return: The vendor of this PurchaseRequest2.  # noqa: E501
        :rtype: object
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this PurchaseRequest2.

        The vendor code from which to purchase the item. If vendor is supplied, vendor account should be suplied as well.  # noqa: E501

        :param vendor: The vendor of this PurchaseRequest2.  # noqa: E501
        :type: object
        """

        self._vendor = vendor

    @property
    def vendor_account(self):
        """Gets the vendor_account of this PurchaseRequest2.  # noqa: E501

        The vendor account code. Must be a valid account of the vendor.  # noqa: E501

        :return: The vendor_account of this PurchaseRequest2.  # noqa: E501
        :rtype: str
        """
        return self._vendor_account

    @vendor_account.setter
    def vendor_account(self, vendor_account):
        """Sets the vendor_account of this PurchaseRequest2.

        The vendor account code. Must be a valid account of the vendor.  # noqa: E501

        :param vendor_account: The vendor_account of this PurchaseRequest2.  # noqa: E501
        :type: str
        """

        self._vendor_account = vendor_account

    @property
    def approved_by(self):
        """Gets the approved_by of this PurchaseRequest2.  # noqa: E501

        The primary identifier of the operator which made the approval. Output parameter.  # noqa: E501

        :return: The approved_by of this PurchaseRequest2.  # noqa: E501
        :rtype: str
        """
        return self._approved_by

    @approved_by.setter
    def approved_by(self, approved_by):
        """Sets the approved_by of this PurchaseRequest2.

        The primary identifier of the operator which made the approval. Output parameter.  # noqa: E501

        :param approved_by: The approved_by of this PurchaseRequest2.  # noqa: E501
        :type: str
        """

        self._approved_by = approved_by

    @property
    def requester_note(self):
        """Gets the requester_note of this PurchaseRequest2.  # noqa: E501

        Any note to send to the user who will be approving or rejecting the request.  # noqa: E501

        :return: The requester_note of this PurchaseRequest2.  # noqa: E501
        :rtype: str
        """
        return self._requester_note

    @requester_note.setter
    def requester_note(self, requester_note):
        """Sets the requester_note of this PurchaseRequest2.

        Any note to send to the user who will be approving or rejecting the request.  # noqa: E501

        :param requester_note: The requester_note of this PurchaseRequest2.  # noqa: E501
        :type: str
        """

        self._requester_note = requester_note

    @property
    def reject_reason(self):
        """Gets the reject_reason of this PurchaseRequest2.  # noqa: E501

        The reason the request was rejected, if any. Output parameter.  # noqa: E501

        :return: The reject_reason of this PurchaseRequest2.  # noqa: E501
        :rtype: object
        """
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, reject_reason):
        """Sets the reject_reason of this PurchaseRequest2.

        The reason the request was rejected, if any. Output parameter.  # noqa: E501

        :param reject_reason: The reject_reason of this PurchaseRequest2.  # noqa: E501
        :type: object
        """

        self._reject_reason = reject_reason

    @property
    def resource_metadata(self):
        """Gets the resource_metadata of this PurchaseRequest2.  # noqa: E501


        :return: The resource_metadata of this PurchaseRequest2.  # noqa: E501
        :rtype: ResourceMetadata2
        """
        return self._resource_metadata

    @resource_metadata.setter
    def resource_metadata(self, resource_metadata):
        """Sets the resource_metadata of this PurchaseRequest2.


        :param resource_metadata: The resource_metadata of this PurchaseRequest2.  # noqa: E501
        :type: ResourceMetadata2
        """
        if resource_metadata is None:
            raise ValueError("Invalid value for `resource_metadata`, must not be `None`")  # noqa: E501

        self._resource_metadata = resource_metadata

    @property
    def notes(self):
        """Gets the notes of this PurchaseRequest2.  # noqa: E501


        :return: The notes of this PurchaseRequest2.  # noqa: E501
        :rtype: RestNotes
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this PurchaseRequest2.


        :param notes: The notes of this PurchaseRequest2.  # noqa: E501
        :type: RestNotes
        """

        self._notes = notes

    @property
    def location(self):
        """Gets the location of this PurchaseRequest2.  # noqa: E501


        :return: The location of this PurchaseRequest2.  # noqa: E501
        :rtype: Locations2
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this PurchaseRequest2.


        :param location: The location of this PurchaseRequest2.  # noqa: E501
        :type: Locations2
        """

        self._location = location

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
        if issubclass(PurchaseRequest2, dict):
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
        if not isinstance(other, PurchaseRequest2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
