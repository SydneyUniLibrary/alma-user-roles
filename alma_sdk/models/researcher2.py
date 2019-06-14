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
from alma_sdk.models.researcher_alternate_emails2 import ResearcherAlternateEmails2  # noqa: F401,E501
from alma_sdk.models.researcher_associations2 import ResearcherAssociations2  # noqa: F401,E501
from alma_sdk.models.researcher_descriptions2 import ResearcherDescriptions2  # noqa: F401,E501
from alma_sdk.models.researcher_educations2 import ResearcherEducations2  # noqa: F401,E501
from alma_sdk.models.researcher_external_organization_affiliations2 import ResearcherExternalOrganizationAffiliations2  # noqa: F401,E501
from alma_sdk.models.researcher_honors2 import ResearcherHonors2  # noqa: F401,E501
from alma_sdk.models.researcher_keywords2 import ResearcherKeywords2  # noqa: F401,E501
from alma_sdk.models.researcher_languages2 import ResearcherLanguages2  # noqa: F401,E501
from alma_sdk.models.researcher_name_variants2 import ResearcherNameVariants2  # noqa: F401,E501
from alma_sdk.models.researcher_organization_affiliations2 import ResearcherOrganizationAffiliations2  # noqa: F401,E501
from alma_sdk.models.researcher_previous_external_organization_affiliations2 import ResearcherPreviousExternalOrganizationAffiliations2  # noqa: F401,E501
from alma_sdk.models.researcher_previous_organization_affiliations2 import ResearcherPreviousOrganizationAffiliations2  # noqa: F401,E501
from alma_sdk.models.researcher_research_topics2 import ResearcherResearchTopics2  # noqa: F401,E501
from alma_sdk.models.researcher_webpages2 import ResearcherWebpages2  # noqa: F401,E501


class Researcher2(object):
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
        'position': 'str',
        'default_publication_language': 'str',
        'researcher_alternate_email': 'ResearcherAlternateEmails2',
        'researcher_organization_affiliation': 'ResearcherOrganizationAffiliations2',
        'researcher_previous_organization_affiliation': 'ResearcherPreviousOrganizationAffiliations2',
        'researcher_external_organization_affiliation': 'ResearcherExternalOrganizationAffiliations2',
        'researcher_previous_external_organization_affiliation': 'ResearcherPreviousExternalOrganizationAffiliations2',
        'researcher_name_variant': 'ResearcherNameVariants2',
        'researcher_research_topic': 'ResearcherResearchTopics2',
        'researcher_keyword': 'ResearcherKeywords2',
        'researcher_association': 'ResearcherAssociations2',
        'researcher_language': 'ResearcherLanguages2',
        'researcher_honor': 'ResearcherHonors2',
        'researcher_education': 'ResearcherEducations2',
        'researcher_description': 'ResearcherDescriptions2',
        'researcher_webpage': 'ResearcherWebpages2'
    }

    attribute_map = {
        'position': 'position',
        'default_publication_language': 'default_publication_language',
        'researcher_alternate_email': 'researcher_alternate_email',
        'researcher_organization_affiliation': 'researcher_organization_affiliation',
        'researcher_previous_organization_affiliation': 'researcher_previous_organization_affiliation',
        'researcher_external_organization_affiliation': 'researcher_external_organization_affiliation',
        'researcher_previous_external_organization_affiliation': 'researcher_previous_external_organization_affiliation',
        'researcher_name_variant': 'researcher_name_variant',
        'researcher_research_topic': 'researcher_research_topic',
        'researcher_keyword': 'researcher_keyword',
        'researcher_association': 'researcher_association',
        'researcher_language': 'researcher_language',
        'researcher_honor': 'researcher_honor',
        'researcher_education': 'researcher_education',
        'researcher_description': 'researcher_description',
        'researcher_webpage': 'researcher_webpage'
    }

    def __init__(self, position=None, default_publication_language=None, researcher_alternate_email=None, researcher_organization_affiliation=None, researcher_previous_organization_affiliation=None, researcher_external_organization_affiliation=None, researcher_previous_external_organization_affiliation=None, researcher_name_variant=None, researcher_research_topic=None, researcher_keyword=None, researcher_association=None, researcher_language=None, researcher_honor=None, researcher_education=None, researcher_description=None, researcher_webpage=None):  # noqa: E501
        """Researcher2 - a model defined in Swagger"""  # noqa: E501
        self._position = None
        self._default_publication_language = None
        self._researcher_alternate_email = None
        self._researcher_organization_affiliation = None
        self._researcher_previous_organization_affiliation = None
        self._researcher_external_organization_affiliation = None
        self._researcher_previous_external_organization_affiliation = None
        self._researcher_name_variant = None
        self._researcher_research_topic = None
        self._researcher_keyword = None
        self._researcher_association = None
        self._researcher_language = None
        self._researcher_honor = None
        self._researcher_education = None
        self._researcher_description = None
        self._researcher_webpage = None
        self.discriminator = None
        if position is not None:
            self.position = position
        if default_publication_language is not None:
            self.default_publication_language = default_publication_language
        if researcher_alternate_email is not None:
            self.researcher_alternate_email = researcher_alternate_email
        if researcher_organization_affiliation is not None:
            self.researcher_organization_affiliation = researcher_organization_affiliation
        if researcher_previous_organization_affiliation is not None:
            self.researcher_previous_organization_affiliation = researcher_previous_organization_affiliation
        if researcher_external_organization_affiliation is not None:
            self.researcher_external_organization_affiliation = researcher_external_organization_affiliation
        if researcher_previous_external_organization_affiliation is not None:
            self.researcher_previous_external_organization_affiliation = researcher_previous_external_organization_affiliation
        if researcher_name_variant is not None:
            self.researcher_name_variant = researcher_name_variant
        if researcher_research_topic is not None:
            self.researcher_research_topic = researcher_research_topic
        if researcher_keyword is not None:
            self.researcher_keyword = researcher_keyword
        if researcher_association is not None:
            self.researcher_association = researcher_association
        if researcher_language is not None:
            self.researcher_language = researcher_language
        if researcher_honor is not None:
            self.researcher_honor = researcher_honor
        if researcher_education is not None:
            self.researcher_education = researcher_education
        if researcher_description is not None:
            self.researcher_description = researcher_description
        if researcher_webpage is not None:
            self.researcher_webpage = researcher_webpage

    @property
    def position(self):
        """Gets the position of this Researcher2.  # noqa: E501

        The researcher's position.  # noqa: E501

        :return: The position of this Researcher2.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Researcher2.

        The researcher's position.  # noqa: E501

        :param position: The position of this Researcher2.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def default_publication_language(self):
        """Gets the default_publication_language of this Researcher2.  # noqa: E501

        The researcher's default publication language. Possible codes are listed in 'User Preferred Language' [code table](https://developers.exlibrisgroup.com/blog/Working-with-the-code-tables-API). Default: en. On SIS synch this field will not be replaced if it was updated manually.  # noqa: E501

        :return: The default_publication_language of this Researcher2.  # noqa: E501
        :rtype: str
        """
        return self._default_publication_language

    @default_publication_language.setter
    def default_publication_language(self, default_publication_language):
        """Sets the default_publication_language of this Researcher2.

        The researcher's default publication language. Possible codes are listed in 'User Preferred Language' [code table](https://developers.exlibrisgroup.com/blog/Working-with-the-code-tables-API). Default: en. On SIS synch this field will not be replaced if it was updated manually.  # noqa: E501

        :param default_publication_language: The default_publication_language of this Researcher2.  # noqa: E501
        :type: str
        """

        self._default_publication_language = default_publication_language

    @property
    def researcher_alternate_email(self):
        """Gets the researcher_alternate_email of this Researcher2.  # noqa: E501


        :return: The researcher_alternate_email of this Researcher2.  # noqa: E501
        :rtype: ResearcherAlternateEmails2
        """
        return self._researcher_alternate_email

    @researcher_alternate_email.setter
    def researcher_alternate_email(self, researcher_alternate_email):
        """Sets the researcher_alternate_email of this Researcher2.


        :param researcher_alternate_email: The researcher_alternate_email of this Researcher2.  # noqa: E501
        :type: ResearcherAlternateEmails2
        """

        self._researcher_alternate_email = researcher_alternate_email

    @property
    def researcher_organization_affiliation(self):
        """Gets the researcher_organization_affiliation of this Researcher2.  # noqa: E501


        :return: The researcher_organization_affiliation of this Researcher2.  # noqa: E501
        :rtype: ResearcherOrganizationAffiliations2
        """
        return self._researcher_organization_affiliation

    @researcher_organization_affiliation.setter
    def researcher_organization_affiliation(self, researcher_organization_affiliation):
        """Sets the researcher_organization_affiliation of this Researcher2.


        :param researcher_organization_affiliation: The researcher_organization_affiliation of this Researcher2.  # noqa: E501
        :type: ResearcherOrganizationAffiliations2
        """

        self._researcher_organization_affiliation = researcher_organization_affiliation

    @property
    def researcher_previous_organization_affiliation(self):
        """Gets the researcher_previous_organization_affiliation of this Researcher2.  # noqa: E501


        :return: The researcher_previous_organization_affiliation of this Researcher2.  # noqa: E501
        :rtype: ResearcherPreviousOrganizationAffiliations2
        """
        return self._researcher_previous_organization_affiliation

    @researcher_previous_organization_affiliation.setter
    def researcher_previous_organization_affiliation(self, researcher_previous_organization_affiliation):
        """Sets the researcher_previous_organization_affiliation of this Researcher2.


        :param researcher_previous_organization_affiliation: The researcher_previous_organization_affiliation of this Researcher2.  # noqa: E501
        :type: ResearcherPreviousOrganizationAffiliations2
        """

        self._researcher_previous_organization_affiliation = researcher_previous_organization_affiliation

    @property
    def researcher_external_organization_affiliation(self):
        """Gets the researcher_external_organization_affiliation of this Researcher2.  # noqa: E501


        :return: The researcher_external_organization_affiliation of this Researcher2.  # noqa: E501
        :rtype: ResearcherExternalOrganizationAffiliations2
        """
        return self._researcher_external_organization_affiliation

    @researcher_external_organization_affiliation.setter
    def researcher_external_organization_affiliation(self, researcher_external_organization_affiliation):
        """Sets the researcher_external_organization_affiliation of this Researcher2.


        :param researcher_external_organization_affiliation: The researcher_external_organization_affiliation of this Researcher2.  # noqa: E501
        :type: ResearcherExternalOrganizationAffiliations2
        """

        self._researcher_external_organization_affiliation = researcher_external_organization_affiliation

    @property
    def researcher_previous_external_organization_affiliation(self):
        """Gets the researcher_previous_external_organization_affiliation of this Researcher2.  # noqa: E501


        :return: The researcher_previous_external_organization_affiliation of this Researcher2.  # noqa: E501
        :rtype: ResearcherPreviousExternalOrganizationAffiliations2
        """
        return self._researcher_previous_external_organization_affiliation

    @researcher_previous_external_organization_affiliation.setter
    def researcher_previous_external_organization_affiliation(self, researcher_previous_external_organization_affiliation):
        """Sets the researcher_previous_external_organization_affiliation of this Researcher2.


        :param researcher_previous_external_organization_affiliation: The researcher_previous_external_organization_affiliation of this Researcher2.  # noqa: E501
        :type: ResearcherPreviousExternalOrganizationAffiliations2
        """

        self._researcher_previous_external_organization_affiliation = researcher_previous_external_organization_affiliation

    @property
    def researcher_name_variant(self):
        """Gets the researcher_name_variant of this Researcher2.  # noqa: E501


        :return: The researcher_name_variant of this Researcher2.  # noqa: E501
        :rtype: ResearcherNameVariants2
        """
        return self._researcher_name_variant

    @researcher_name_variant.setter
    def researcher_name_variant(self, researcher_name_variant):
        """Sets the researcher_name_variant of this Researcher2.


        :param researcher_name_variant: The researcher_name_variant of this Researcher2.  # noqa: E501
        :type: ResearcherNameVariants2
        """

        self._researcher_name_variant = researcher_name_variant

    @property
    def researcher_research_topic(self):
        """Gets the researcher_research_topic of this Researcher2.  # noqa: E501


        :return: The researcher_research_topic of this Researcher2.  # noqa: E501
        :rtype: ResearcherResearchTopics2
        """
        return self._researcher_research_topic

    @researcher_research_topic.setter
    def researcher_research_topic(self, researcher_research_topic):
        """Sets the researcher_research_topic of this Researcher2.


        :param researcher_research_topic: The researcher_research_topic of this Researcher2.  # noqa: E501
        :type: ResearcherResearchTopics2
        """

        self._researcher_research_topic = researcher_research_topic

    @property
    def researcher_keyword(self):
        """Gets the researcher_keyword of this Researcher2.  # noqa: E501


        :return: The researcher_keyword of this Researcher2.  # noqa: E501
        :rtype: ResearcherKeywords2
        """
        return self._researcher_keyword

    @researcher_keyword.setter
    def researcher_keyword(self, researcher_keyword):
        """Sets the researcher_keyword of this Researcher2.


        :param researcher_keyword: The researcher_keyword of this Researcher2.  # noqa: E501
        :type: ResearcherKeywords2
        """

        self._researcher_keyword = researcher_keyword

    @property
    def researcher_association(self):
        """Gets the researcher_association of this Researcher2.  # noqa: E501


        :return: The researcher_association of this Researcher2.  # noqa: E501
        :rtype: ResearcherAssociations2
        """
        return self._researcher_association

    @researcher_association.setter
    def researcher_association(self, researcher_association):
        """Sets the researcher_association of this Researcher2.


        :param researcher_association: The researcher_association of this Researcher2.  # noqa: E501
        :type: ResearcherAssociations2
        """

        self._researcher_association = researcher_association

    @property
    def researcher_language(self):
        """Gets the researcher_language of this Researcher2.  # noqa: E501


        :return: The researcher_language of this Researcher2.  # noqa: E501
        :rtype: ResearcherLanguages2
        """
        return self._researcher_language

    @researcher_language.setter
    def researcher_language(self, researcher_language):
        """Sets the researcher_language of this Researcher2.


        :param researcher_language: The researcher_language of this Researcher2.  # noqa: E501
        :type: ResearcherLanguages2
        """

        self._researcher_language = researcher_language

    @property
    def researcher_honor(self):
        """Gets the researcher_honor of this Researcher2.  # noqa: E501


        :return: The researcher_honor of this Researcher2.  # noqa: E501
        :rtype: ResearcherHonors2
        """
        return self._researcher_honor

    @researcher_honor.setter
    def researcher_honor(self, researcher_honor):
        """Sets the researcher_honor of this Researcher2.


        :param researcher_honor: The researcher_honor of this Researcher2.  # noqa: E501
        :type: ResearcherHonors2
        """

        self._researcher_honor = researcher_honor

    @property
    def researcher_education(self):
        """Gets the researcher_education of this Researcher2.  # noqa: E501


        :return: The researcher_education of this Researcher2.  # noqa: E501
        :rtype: ResearcherEducations2
        """
        return self._researcher_education

    @researcher_education.setter
    def researcher_education(self, researcher_education):
        """Sets the researcher_education of this Researcher2.


        :param researcher_education: The researcher_education of this Researcher2.  # noqa: E501
        :type: ResearcherEducations2
        """

        self._researcher_education = researcher_education

    @property
    def researcher_description(self):
        """Gets the researcher_description of this Researcher2.  # noqa: E501


        :return: The researcher_description of this Researcher2.  # noqa: E501
        :rtype: ResearcherDescriptions2
        """
        return self._researcher_description

    @researcher_description.setter
    def researcher_description(self, researcher_description):
        """Sets the researcher_description of this Researcher2.


        :param researcher_description: The researcher_description of this Researcher2.  # noqa: E501
        :type: ResearcherDescriptions2
        """

        self._researcher_description = researcher_description

    @property
    def researcher_webpage(self):
        """Gets the researcher_webpage of this Researcher2.  # noqa: E501


        :return: The researcher_webpage of this Researcher2.  # noqa: E501
        :rtype: ResearcherWebpages2
        """
        return self._researcher_webpage

    @researcher_webpage.setter
    def researcher_webpage(self, researcher_webpage):
        """Sets the researcher_webpage of this Researcher2.


        :param researcher_webpage: The researcher_webpage of this Researcher2.  # noqa: E501
        :type: ResearcherWebpages2
        """

        self._researcher_webpage = researcher_webpage

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
        if issubclass(Researcher2, dict):
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
        if not isinstance(other, Researcher2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other