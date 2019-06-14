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


class UserRequest(object):
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
        'request_type': 'str',
        'description': 'str',
        'pickup_location_type': 'str',
        'pickup_location_library': 'str',
        'pickup_location_circulation_desk': 'str',
        'target_destination': 'object',
        'material_type': 'object',
        'last_interest_date': 'date',
        'partial_digitization': 'bool',
        'chapter_or_article_title': 'str',
        'chapter_or_article_author': 'str',
        'required_pages_range': 'list[object]',
        'full_chapter': 'str',
        'comment': 'str',
        'booking_start_date': 'date',
        'booking_end_date': 'date',
        'destination_location': 'object',
        'call_number_type': 'object',
        'call_number': 'str',
        'item_policy': 'object',
        'due_back_date': 'date',
        'copyrights_declaration_signed_by_patron': 'bool'
    }

    attribute_map = {
        'request_type': 'request_type',
        'description': 'description',
        'pickup_location_type': 'pickup_location_type',
        'pickup_location_library': 'pickup_location_library',
        'pickup_location_circulation_desk': 'pickup_location_circulation_desk',
        'target_destination': 'target_destination',
        'material_type': 'material_type',
        'last_interest_date': 'last_interest_date',
        'partial_digitization': 'partial_digitization',
        'chapter_or_article_title': 'chapter_or_article_title',
        'chapter_or_article_author': 'chapter_or_article_author',
        'required_pages_range': 'required_pages_range',
        'full_chapter': 'full_chapter',
        'comment': 'comment',
        'booking_start_date': 'booking_start_date',
        'booking_end_date': 'booking_end_date',
        'destination_location': 'destination_location',
        'call_number_type': 'call_number_type',
        'call_number': 'call_number',
        'item_policy': 'item_policy',
        'due_back_date': 'due_back_date',
        'copyrights_declaration_signed_by_patron': 'copyrights_declaration_signed_by_patron'
    }

    def __init__(self, request_type=None, description=None, pickup_location_type=None, pickup_location_library=None, pickup_location_circulation_desk=None, target_destination=None, material_type=None, last_interest_date=None, partial_digitization=None, chapter_or_article_title=None, chapter_or_article_author=None, required_pages_range=None, full_chapter=None, comment=None, booking_start_date=None, booking_end_date=None, destination_location=None, call_number_type=None, call_number=None, item_policy=None, due_back_date=None, copyrights_declaration_signed_by_patron=None):  # noqa: E501
        """UserRequest - a model defined in Swagger"""  # noqa: E501
        self._request_type = None
        self._description = None
        self._pickup_location_type = None
        self._pickup_location_library = None
        self._pickup_location_circulation_desk = None
        self._target_destination = None
        self._material_type = None
        self._last_interest_date = None
        self._partial_digitization = None
        self._chapter_or_article_title = None
        self._chapter_or_article_author = None
        self._required_pages_range = None
        self._full_chapter = None
        self._comment = None
        self._booking_start_date = None
        self._booking_end_date = None
        self._destination_location = None
        self._call_number_type = None
        self._call_number = None
        self._item_policy = None
        self._due_back_date = None
        self._copyrights_declaration_signed_by_patron = None
        self.discriminator = None
        self.request_type = request_type
        if description is not None:
            self.description = description
        if pickup_location_type is not None:
            self.pickup_location_type = pickup_location_type
        if pickup_location_library is not None:
            self.pickup_location_library = pickup_location_library
        if pickup_location_circulation_desk is not None:
            self.pickup_location_circulation_desk = pickup_location_circulation_desk
        if target_destination is not None:
            self.target_destination = target_destination
        if material_type is not None:
            self.material_type = material_type
        if last_interest_date is not None:
            self.last_interest_date = last_interest_date
        if partial_digitization is not None:
            self.partial_digitization = partial_digitization
        if chapter_or_article_title is not None:
            self.chapter_or_article_title = chapter_or_article_title
        if chapter_or_article_author is not None:
            self.chapter_or_article_author = chapter_or_article_author
        if required_pages_range is not None:
            self.required_pages_range = required_pages_range
        if full_chapter is not None:
            self.full_chapter = full_chapter
        if comment is not None:
            self.comment = comment
        if booking_start_date is not None:
            self.booking_start_date = booking_start_date
        if booking_end_date is not None:
            self.booking_end_date = booking_end_date
        if destination_location is not None:
            self.destination_location = destination_location
        if call_number_type is not None:
            self.call_number_type = call_number_type
        if call_number is not None:
            self.call_number = call_number
        if item_policy is not None:
            self.item_policy = item_policy
        if due_back_date is not None:
            self.due_back_date = due_back_date
        if copyrights_declaration_signed_by_patron is not None:
            self.copyrights_declaration_signed_by_patron = copyrights_declaration_signed_by_patron

    @property
    def request_type(self):
        """Gets the request_type of this UserRequest.  # noqa: E501


        :return: The request_type of this UserRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        """Sets the request_type of this UserRequest.


        :param request_type: The request_type of this UserRequest.  # noqa: E501
        :type: str
        """
        if request_type is None:
            raise ValueError("Invalid value for `request_type`, must not be `None`")  # noqa: E501
        allowed_values = ["BOOKING", "DIGITIZATION", "HOLD", "MOVE", "WORK_ORDER"]  # noqa: E501
        if request_type not in allowed_values:
            raise ValueError(
                "Invalid value for `request_type` ({0}), must be one of {1}"  # noqa: E501
                .format(request_type, allowed_values)
            )

        self._request_type = request_type

    @property
    def description(self):
        """Gets the description of this UserRequest.  # noqa: E501

        The description of the requested resource when dealing with multi volume/issue resource. For item level requests this is an output parameter. When creating or updating a request for a specific periodical resource, the request is title level, but the specific volume/issue requested is input using this description field (e.g. v.30, #4 Dec, 1966). Please note that this field is sensitive to case and white spaces.  # noqa: E501

        :return: The description of this UserRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserRequest.

        The description of the requested resource when dealing with multi volume/issue resource. For item level requests this is an output parameter. When creating or updating a request for a specific periodical resource, the request is title level, but the specific volume/issue requested is input using this description field (e.g. v.30, #4 Dec, 1966). Please note that this field is sensitive to case and white spaces.  # noqa: E501

        :param description: The description of this UserRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def pickup_location_type(self):
        """Gets the pickup_location_type of this UserRequest.  # noqa: E501


        :return: The pickup_location_type of this UserRequest.  # noqa: E501
        :rtype: str
        """
        return self._pickup_location_type

    @pickup_location_type.setter
    def pickup_location_type(self, pickup_location_type):
        """Sets the pickup_location_type of this UserRequest.


        :param pickup_location_type: The pickup_location_type of this UserRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["LIBRARY", "CIRCULATION_DESK", "USER_WORK_ADDRESS", "USER_HOME_ADDRESS"]  # noqa: E501
        if pickup_location_type not in allowed_values:
            raise ValueError(
                "Invalid value for `pickup_location_type` ({0}), must be one of {1}"  # noqa: E501
                .format(pickup_location_type, allowed_values)
            )

        self._pickup_location_type = pickup_location_type

    @property
    def pickup_location_library(self):
        """Gets the pickup_location_library of this UserRequest.  # noqa: E501

        The pickup location library code. Relevant and mandatory when request_type = HOLD or BOOKING. see [Get libraries API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4Dp4I8TKv6CAxBlD4LyRaVE=/37088dc9-c685-4641-bc7f-60b5ca7cabed).  # noqa: E501

        :return: The pickup_location_library of this UserRequest.  # noqa: E501
        :rtype: str
        """
        return self._pickup_location_library

    @pickup_location_library.setter
    def pickup_location_library(self, pickup_location_library):
        """Sets the pickup_location_library of this UserRequest.

        The pickup location library code. Relevant and mandatory when request_type = HOLD or BOOKING. see [Get libraries API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4Dp4I8TKv6CAxBlD4LyRaVE=/37088dc9-c685-4641-bc7f-60b5ca7cabed).  # noqa: E501

        :param pickup_location_library: The pickup_location_library of this UserRequest.  # noqa: E501
        :type: str
        """

        self._pickup_location_library = pickup_location_library

    @property
    def pickup_location_circulation_desk(self):
        """Gets the pickup_location_circulation_desk of this UserRequest.  # noqa: E501

        The pickup location circulation desk code. Relevant when request_type = HOLD or BOOKING, if pickup_location_type = CIRCULATION_DESK.  # noqa: E501

        :return: The pickup_location_circulation_desk of this UserRequest.  # noqa: E501
        :rtype: str
        """
        return self._pickup_location_circulation_desk

    @pickup_location_circulation_desk.setter
    def pickup_location_circulation_desk(self, pickup_location_circulation_desk):
        """Sets the pickup_location_circulation_desk of this UserRequest.

        The pickup location circulation desk code. Relevant when request_type = HOLD or BOOKING, if pickup_location_type = CIRCULATION_DESK.  # noqa: E501

        :param pickup_location_circulation_desk: The pickup_location_circulation_desk of this UserRequest.  # noqa: E501
        :type: str
        """

        self._pickup_location_circulation_desk = pickup_location_circulation_desk

    @property
    def target_destination(self):
        """Gets the target_destination of this UserRequest.  # noqa: E501

        The code of the department chosen to fulfill the digitization or work order request. A list of relevant departments can be retrieved using GET /almaws/v1/conf/departments?Type=DIGI  # noqa: E501

        :return: The target_destination of this UserRequest.  # noqa: E501
        :rtype: object
        """
        return self._target_destination

    @target_destination.setter
    def target_destination(self, target_destination):
        """Sets the target_destination of this UserRequest.

        The code of the department chosen to fulfill the digitization or work order request. A list of relevant departments can be retrieved using GET /almaws/v1/conf/departments?Type=DIGI  # noqa: E501

        :param target_destination: The target_destination of this UserRequest.  # noqa: E501
        :type: object
        """

        self._target_destination = target_destination

    @property
    def material_type(self):
        """Gets the material_type of this UserRequest.  # noqa: E501

        The requested material type code. Optional. Possible codes are listed in 'Physical Material Type' [code table](https://developers.exlibrisgroup.com/blog/Working-with-the-code-tables-API). This field is output parameter when the request is in item level, and input parameter when the request is in title level.  # noqa: E501

        :return: The material_type of this UserRequest.  # noqa: E501
        :rtype: object
        """
        return self._material_type

    @material_type.setter
    def material_type(self, material_type):
        """Sets the material_type of this UserRequest.

        The requested material type code. Optional. Possible codes are listed in 'Physical Material Type' [code table](https://developers.exlibrisgroup.com/blog/Working-with-the-code-tables-API). This field is output parameter when the request is in item level, and input parameter when the request is in title level.  # noqa: E501

        :param material_type: The material_type of this UserRequest.  # noqa: E501
        :type: object
        """

        self._material_type = material_type

    @property
    def last_interest_date(self):
        """Gets the last_interest_date of this UserRequest.  # noqa: E501

        The last date for which the request is needed. Optional.  # noqa: E501

        :return: The last_interest_date of this UserRequest.  # noqa: E501
        :rtype: date
        """
        return self._last_interest_date

    @last_interest_date.setter
    def last_interest_date(self, last_interest_date):
        """Sets the last_interest_date of this UserRequest.

        The last date for which the request is needed. Optional.  # noqa: E501

        :param last_interest_date: The last_interest_date of this UserRequest.  # noqa: E501
        :type: date
        """

        self._last_interest_date = last_interest_date

    @property
    def partial_digitization(self):
        """Gets the partial_digitization of this UserRequest.  # noqa: E501

        Indication whether the digitization is partial or full. Relevant and mandatory when request_type = DIGITIZATION.  # noqa: E501

        :return: The partial_digitization of this UserRequest.  # noqa: E501
        :rtype: bool
        """
        return self._partial_digitization

    @partial_digitization.setter
    def partial_digitization(self, partial_digitization):
        """Sets the partial_digitization of this UserRequest.

        Indication whether the digitization is partial or full. Relevant and mandatory when request_type = DIGITIZATION.  # noqa: E501

        :param partial_digitization: The partial_digitization of this UserRequest.  # noqa: E501
        :type: bool
        """

        self._partial_digitization = partial_digitization

    @property
    def chapter_or_article_title(self):
        """Gets the chapter_or_article_title of this UserRequest.  # noqa: E501

        The title of the chapter or article.  # noqa: E501

        :return: The chapter_or_article_title of this UserRequest.  # noqa: E501
        :rtype: str
        """
        return self._chapter_or_article_title

    @chapter_or_article_title.setter
    def chapter_or_article_title(self, chapter_or_article_title):
        """Sets the chapter_or_article_title of this UserRequest.

        The title of the chapter or article.  # noqa: E501

        :param chapter_or_article_title: The chapter_or_article_title of this UserRequest.  # noqa: E501
        :type: str
        """

        self._chapter_or_article_title = chapter_or_article_title

    @property
    def chapter_or_article_author(self):
        """Gets the chapter_or_article_author of this UserRequest.  # noqa: E501

        The author of the chapter or article.  # noqa: E501

        :return: The chapter_or_article_author of this UserRequest.  # noqa: E501
        :rtype: str
        """
        return self._chapter_or_article_author

    @chapter_or_article_author.setter
    def chapter_or_article_author(self, chapter_or_article_author):
        """Sets the chapter_or_article_author of this UserRequest.

        The author of the chapter or article.  # noqa: E501

        :param chapter_or_article_author: The chapter_or_article_author of this UserRequest.  # noqa: E501
        :type: str
        """

        self._chapter_or_article_author = chapter_or_article_author

    @property
    def required_pages_range(self):
        """Gets the required_pages_range of this UserRequest.  # noqa: E501

        The pages required for the digitization.  # noqa: E501

        :return: The required_pages_range of this UserRequest.  # noqa: E501
        :rtype: list[object]
        """
        return self._required_pages_range

    @required_pages_range.setter
    def required_pages_range(self, required_pages_range):
        """Sets the required_pages_range of this UserRequest.

        The pages required for the digitization.  # noqa: E501

        :param required_pages_range: The required_pages_range of this UserRequest.  # noqa: E501
        :type: list[object]
        """

        self._required_pages_range = required_pages_range

    @property
    def full_chapter(self):
        """Gets the full_chapter of this UserRequest.  # noqa: E501

        An indication whether the full chapter is requested for digitization. Valid options are: true of false (lower case).  # noqa: E501

        :return: The full_chapter of this UserRequest.  # noqa: E501
        :rtype: str
        """
        return self._full_chapter

    @full_chapter.setter
    def full_chapter(self, full_chapter):
        """Sets the full_chapter of this UserRequest.

        An indication whether the full chapter is requested for digitization. Valid options are: true of false (lower case).  # noqa: E501

        :param full_chapter: The full_chapter of this UserRequest.  # noqa: E501
        :type: str
        """

        self._full_chapter = full_chapter

    @property
    def comment(self):
        """Gets the comment of this UserRequest.  # noqa: E501

        The related comment of the request. Mandatory when request_type = DIGITIZATION and partial_digitization is true.  # noqa: E501

        :return: The comment of this UserRequest.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this UserRequest.

        The related comment of the request. Mandatory when request_type = DIGITIZATION and partial_digitization is true.  # noqa: E501

        :param comment: The comment of this UserRequest.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def booking_start_date(self):
        """Gets the booking_start_date of this UserRequest.  # noqa: E501

        The start date in which the request is needed. Relevant and mandatory when request_type = BOOKING.  # noqa: E501

        :return: The booking_start_date of this UserRequest.  # noqa: E501
        :rtype: date
        """
        return self._booking_start_date

    @booking_start_date.setter
    def booking_start_date(self, booking_start_date):
        """Sets the booking_start_date of this UserRequest.

        The start date in which the request is needed. Relevant and mandatory when request_type = BOOKING.  # noqa: E501

        :param booking_start_date: The booking_start_date of this UserRequest.  # noqa: E501
        :type: date
        """

        self._booking_start_date = booking_start_date

    @property
    def booking_end_date(self):
        """Gets the booking_end_date of this UserRequest.  # noqa: E501

        The end date in which the request is needed. Relevant and mandatory when request_type = BOOKING.  # noqa: E501

        :return: The booking_end_date of this UserRequest.  # noqa: E501
        :rtype: date
        """
        return self._booking_end_date

    @booking_end_date.setter
    def booking_end_date(self, booking_end_date):
        """Sets the booking_end_date of this UserRequest.

        The end date in which the request is needed. Relevant and mandatory when request_type = BOOKING.  # noqa: E501

        :param booking_end_date: The booking_end_date of this UserRequest.  # noqa: E501
        :type: date
        """

        self._booking_end_date = booking_end_date

    @property
    def destination_location(self):
        """Gets the destination_location of this UserRequest.  # noqa: E501

        The location in the library to which the item is to be moved. Relevant when request_type = MOVE.  # noqa: E501

        :return: The destination_location of this UserRequest.  # noqa: E501
        :rtype: object
        """
        return self._destination_location

    @destination_location.setter
    def destination_location(self, destination_location):
        """Sets the destination_location of this UserRequest.

        The location in the library to which the item is to be moved. Relevant when request_type = MOVE.  # noqa: E501

        :param destination_location: The destination_location of this UserRequest.  # noqa: E501
        :type: object
        """

        self._destination_location = destination_location

    @property
    def call_number_type(self):
        """Gets the call_number_type of this UserRequest.  # noqa: E501

        The call number type of the holding to which the item is to be moved. Relevant when request_type = MOVE.  # noqa: E501

        :return: The call_number_type of this UserRequest.  # noqa: E501
        :rtype: object
        """
        return self._call_number_type

    @call_number_type.setter
    def call_number_type(self, call_number_type):
        """Sets the call_number_type of this UserRequest.

        The call number type of the holding to which the item is to be moved. Relevant when request_type = MOVE.  # noqa: E501

        :param call_number_type: The call_number_type of this UserRequest.  # noqa: E501
        :type: object
        """

        self._call_number_type = call_number_type

    @property
    def call_number(self):
        """Gets the call_number of this UserRequest.  # noqa: E501

        The call number of the holding to which the item is to be moved. Relevant when request_type = MOVE.  # noqa: E501

        :return: The call_number of this UserRequest.  # noqa: E501
        :rtype: str
        """
        return self._call_number

    @call_number.setter
    def call_number(self, call_number):
        """Sets the call_number of this UserRequest.

        The call number of the holding to which the item is to be moved. Relevant when request_type = MOVE.  # noqa: E501

        :param call_number: The call_number of this UserRequest.  # noqa: E501
        :type: str
        """

        self._call_number = call_number

    @property
    def item_policy(self):
        """Gets the item_policy of this UserRequest.  # noqa: E501

        The item policy to be applied in the new location. Relevant when request_type = MOVE.  # noqa: E501

        :return: The item_policy of this UserRequest.  # noqa: E501
        :rtype: object
        """
        return self._item_policy

    @item_policy.setter
    def item_policy(self, item_policy):
        """Sets the item_policy of this UserRequest.

        The item policy to be applied in the new location. Relevant when request_type = MOVE.  # noqa: E501

        :param item_policy: The item_policy of this UserRequest.  # noqa: E501
        :type: object
        """

        self._item_policy = item_policy

    @property
    def due_back_date(self):
        """Gets the due_back_date of this UserRequest.  # noqa: E501

        The date the item is due back. Relevant when request_type = MOVE and request_sub_type = MOVE_TO_TEMPORARY.  # noqa: E501

        :return: The due_back_date of this UserRequest.  # noqa: E501
        :rtype: date
        """
        return self._due_back_date

    @due_back_date.setter
    def due_back_date(self, due_back_date):
        """Sets the due_back_date of this UserRequest.

        The date the item is due back. Relevant when request_type = MOVE and request_sub_type = MOVE_TO_TEMPORARY.  # noqa: E501

        :param due_back_date: The due_back_date of this UserRequest.  # noqa: E501
        :type: date
        """

        self._due_back_date = due_back_date

    @property
    def copyrights_declaration_signed_by_patron(self):
        """Gets the copyrights_declaration_signed_by_patron of this UserRequest.  # noqa: E501

        An indication whether copyrights declaration was signed by patron. Relevant for patron digitization requests only.  # noqa: E501

        :return: The copyrights_declaration_signed_by_patron of this UserRequest.  # noqa: E501
        :rtype: bool
        """
        return self._copyrights_declaration_signed_by_patron

    @copyrights_declaration_signed_by_patron.setter
    def copyrights_declaration_signed_by_patron(self, copyrights_declaration_signed_by_patron):
        """Sets the copyrights_declaration_signed_by_patron of this UserRequest.

        An indication whether copyrights declaration was signed by patron. Relevant for patron digitization requests only.  # noqa: E501

        :param copyrights_declaration_signed_by_patron: The copyrights_declaration_signed_by_patron of this UserRequest.  # noqa: E501
        :type: bool
        """

        self._copyrights_declaration_signed_by_patron = copyrights_declaration_signed_by_patron

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
        if issubclass(UserRequest, dict):
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
        if not isinstance(other, UserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
