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


class ResourceMetadata(object):
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
        'mms_id': 'object',
        'citation_type': 'object',
        'title': 'str',
        'author': 'str',
        'edition': 'str',
        'isbn': 'str',
        'issn': 'str',
        'lcc_number': 'str',
        'other_system_number': 'str',
        'publisher': 'str',
        'publication_place': 'str',
        'publication_year': 'str',
        'bib_note': 'str',
        'volume': 'str'
    }

    attribute_map = {
        'mms_id': 'mms_id',
        'citation_type': 'citation_type',
        'title': 'title',
        'author': 'author',
        'edition': 'edition',
        'isbn': 'isbn',
        'issn': 'issn',
        'lcc_number': 'lcc_number',
        'other_system_number': 'other_system_number',
        'publisher': 'publisher',
        'publication_place': 'publication_place',
        'publication_year': 'publication_year',
        'bib_note': 'bib_note',
        'volume': 'volume'
    }

    def __init__(self, mms_id=None, citation_type=None, title=None, author=None, edition=None, isbn=None, issn=None, lcc_number=None, other_system_number=None, publisher=None, publication_place=None, publication_year=None, bib_note=None, volume=None):  # noqa: E501
        """ResourceMetadata - a model defined in Swagger"""  # noqa: E501
        self._mms_id = None
        self._citation_type = None
        self._title = None
        self._author = None
        self._edition = None
        self._isbn = None
        self._issn = None
        self._lcc_number = None
        self._other_system_number = None
        self._publisher = None
        self._publication_place = None
        self._publication_year = None
        self._bib_note = None
        self._volume = None
        self.discriminator = None
        if mms_id is not None:
            self.mms_id = mms_id
        if citation_type is not None:
            self.citation_type = citation_type
        if title is not None:
            self.title = title
        if author is not None:
            self.author = author
        if edition is not None:
            self.edition = edition
        if isbn is not None:
            self.isbn = isbn
        if issn is not None:
            self.issn = issn
        if lcc_number is not None:
            self.lcc_number = lcc_number
        if other_system_number is not None:
            self.other_system_number = other_system_number
        if publisher is not None:
            self.publisher = publisher
        if publication_place is not None:
            self.publication_place = publication_place
        if publication_year is not None:
            self.publication_year = publication_year
        if bib_note is not None:
            self.bib_note = bib_note
        if volume is not None:
            self.volume = volume

    @property
    def mms_id(self):
        """Gets the mms_id of this ResourceMetadata.  # noqa: E501

        mms_id. If supplied in the POST action, The purchase order will be created for this bibliographic record.  # noqa: E501

        :return: The mms_id of this ResourceMetadata.  # noqa: E501
        :rtype: object
        """
        return self._mms_id

    @mms_id.setter
    def mms_id(self, mms_id):
        """Sets the mms_id of this ResourceMetadata.

        mms_id. If supplied in the POST action, The purchase order will be created for this bibliographic record.  # noqa: E501

        :param mms_id: The mms_id of this ResourceMetadata.  # noqa: E501
        :type: object
        """

        self._mms_id = mms_id

    @property
    def citation_type(self):
        """Gets the citation_type of this ResourceMetadata.  # noqa: E501

        Type of the requested resource. For example, book or article. Mandatory when creating a request unless mms_id is supplied. Possible codes are listed in PR_CitationType [code table](https://developers.exlibrisgroup.com/blog/Working-with-the-code-tables-API): BOOK / JOURNAL.  # noqa: E501

        :return: The citation_type of this ResourceMetadata.  # noqa: E501
        :rtype: object
        """
        return self._citation_type

    @citation_type.setter
    def citation_type(self, citation_type):
        """Sets the citation_type of this ResourceMetadata.

        Type of the requested resource. For example, book or article. Mandatory when creating a request unless mms_id is supplied. Possible codes are listed in PR_CitationType [code table](https://developers.exlibrisgroup.com/blog/Working-with-the-code-tables-API): BOOK / JOURNAL.  # noqa: E501

        :param citation_type: The citation_type of this ResourceMetadata.  # noqa: E501
        :type: object
        """

        self._citation_type = citation_type

    @property
    def title(self):
        """Gets the title of this ResourceMetadata.  # noqa: E501

        The title. Mandatory in the POST action if mms_id was not supplied.  # noqa: E501

        :return: The title of this ResourceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ResourceMetadata.

        The title. Mandatory in the POST action if mms_id was not supplied.  # noqa: E501

        :param title: The title of this ResourceMetadata.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def author(self):
        """Gets the author of this ResourceMetadata.  # noqa: E501

        Author of the requested resource.  # noqa: E501

        :return: The author of this ResourceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this ResourceMetadata.

        Author of the requested resource.  # noqa: E501

        :param author: The author of this ResourceMetadata.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def edition(self):
        """Gets the edition of this ResourceMetadata.  # noqa: E501

        The edition of the requested resource.  # noqa: E501

        :return: The edition of this ResourceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._edition

    @edition.setter
    def edition(self, edition):
        """Sets the edition of this ResourceMetadata.

        The edition of the requested resource.  # noqa: E501

        :param edition: The edition of this ResourceMetadata.  # noqa: E501
        :type: str
        """

        self._edition = edition

    @property
    def isbn(self):
        """Gets the isbn of this ResourceMetadata.  # noqa: E501

        isbn  # noqa: E501

        :return: The isbn of this ResourceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._isbn

    @isbn.setter
    def isbn(self, isbn):
        """Sets the isbn of this ResourceMetadata.

        isbn  # noqa: E501

        :param isbn: The isbn of this ResourceMetadata.  # noqa: E501
        :type: str
        """

        self._isbn = isbn

    @property
    def issn(self):
        """Gets the issn of this ResourceMetadata.  # noqa: E501

        issn  # noqa: E501

        :return: The issn of this ResourceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._issn

    @issn.setter
    def issn(self, issn):
        """Sets the issn of this ResourceMetadata.

        issn  # noqa: E501

        :param issn: The issn of this ResourceMetadata.  # noqa: E501
        :type: str
        """

        self._issn = issn

    @property
    def lcc_number(self):
        """Gets the lcc_number of this ResourceMetadata.  # noqa: E501

        The library of congress number of the book.  # noqa: E501

        :return: The lcc_number of this ResourceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._lcc_number

    @lcc_number.setter
    def lcc_number(self, lcc_number):
        """Sets the lcc_number of this ResourceMetadata.

        The library of congress number of the book.  # noqa: E501

        :param lcc_number: The lcc_number of this ResourceMetadata.  # noqa: E501
        :type: str
        """

        self._lcc_number = lcc_number

    @property
    def other_system_number(self):
        """Gets the other_system_number of this ResourceMetadata.  # noqa: E501

        A central identifier number, such as Online Computer Library Center (OCLC) number  # noqa: E501

        :return: The other_system_number of this ResourceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._other_system_number

    @other_system_number.setter
    def other_system_number(self, other_system_number):
        """Sets the other_system_number of this ResourceMetadata.

        A central identifier number, such as Online Computer Library Center (OCLC) number  # noqa: E501

        :param other_system_number: The other_system_number of this ResourceMetadata.  # noqa: E501
        :type: str
        """

        self._other_system_number = other_system_number

    @property
    def publisher(self):
        """Gets the publisher of this ResourceMetadata.  # noqa: E501

        The Publisher of the item.  # noqa: E501

        :return: The publisher of this ResourceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this ResourceMetadata.

        The Publisher of the item.  # noqa: E501

        :param publisher: The publisher of this ResourceMetadata.  # noqa: E501
        :type: str
        """

        self._publisher = publisher

    @property
    def publication_place(self):
        """Gets the publication_place of this ResourceMetadata.  # noqa: E501

        The publication place of the item.  # noqa: E501

        :return: The publication_place of this ResourceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._publication_place

    @publication_place.setter
    def publication_place(self, publication_place):
        """Sets the publication_place of this ResourceMetadata.

        The publication place of the item.  # noqa: E501

        :param publication_place: The publication_place of this ResourceMetadata.  # noqa: E501
        :type: str
        """

        self._publication_place = publication_place

    @property
    def publication_year(self):
        """Gets the publication_year of this ResourceMetadata.  # noqa: E501

        The publication year of the item.  # noqa: E501

        :return: The publication_year of this ResourceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._publication_year

    @publication_year.setter
    def publication_year(self, publication_year):
        """Sets the publication_year of this ResourceMetadata.

        The publication year of the item.  # noqa: E501

        :param publication_year: The publication_year of this ResourceMetadata.  # noqa: E501
        :type: str
        """

        self._publication_year = publication_year

    @property
    def bib_note(self):
        """Gets the bib_note of this ResourceMetadata.  # noqa: E501

        The note of the bibliographic record.  # noqa: E501

        :return: The bib_note of this ResourceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._bib_note

    @bib_note.setter
    def bib_note(self, bib_note):
        """Sets the bib_note of this ResourceMetadata.

        The note of the bibliographic record.  # noqa: E501

        :param bib_note: The bib_note of this ResourceMetadata.  # noqa: E501
        :type: str
        """

        self._bib_note = bib_note

    @property
    def volume(self):
        """Gets the volume of this ResourceMetadata.  # noqa: E501

        The volume number.  # noqa: E501

        :return: The volume of this ResourceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this ResourceMetadata.

        The volume number.  # noqa: E501

        :param volume: The volume of this ResourceMetadata.  # noqa: E501
        :type: str
        """

        self._volume = volume

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
        if issubclass(ResourceMetadata, dict):
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
        if not isinstance(other, ResourceMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
