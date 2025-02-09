# coding: utf-8

"""
    Resend

    Resend is the email platform for developers.  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse201(object):
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
        'id': 'str',
        'name': 'str',
        'created_at': 'datetime',
        'status': 'str',
        'records': 'list[CreateDomainResponseRecords]',
        'region': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'created_at': 'created_at',
        'status': 'status',
        'records': 'records',
        'region': 'region'
    }

    def __init__(self, id=None, name=None, created_at=None, status=None, records=None, region=None):  # noqa: E501
        """InlineResponse201 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._created_at = None
        self._status = None
        self._records = None
        self._region = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if created_at is not None:
            self.created_at = created_at
        if status is not None:
            self.status = status
        if records is not None:
            self.records = records
        if region is not None:
            self.region = region

    @property
    def id(self):
        """Gets the id of this InlineResponse201.  # noqa: E501

        The ID of the domain.  # noqa: E501

        :return: The id of this InlineResponse201.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse201.

        The ID of the domain.  # noqa: E501

        :param id: The id of this InlineResponse201.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse201.  # noqa: E501

        The name of the domain.  # noqa: E501

        :return: The name of this InlineResponse201.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse201.

        The name of the domain.  # noqa: E501

        :param name: The name of this InlineResponse201.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponse201.  # noqa: E501

        The date and time the domain was created.  # noqa: E501

        :return: The created_at of this InlineResponse201.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponse201.

        The date and time the domain was created.  # noqa: E501

        :param created_at: The created_at of this InlineResponse201.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def status(self):
        """Gets the status of this InlineResponse201.  # noqa: E501

        The status of the domain.  # noqa: E501

        :return: The status of this InlineResponse201.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse201.

        The status of the domain.  # noqa: E501

        :param status: The status of this InlineResponse201.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def records(self):
        """Gets the records of this InlineResponse201.  # noqa: E501


        :return: The records of this InlineResponse201.  # noqa: E501
        :rtype: list[CreateDomainResponseRecords]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this InlineResponse201.


        :param records: The records of this InlineResponse201.  # noqa: E501
        :type: list[CreateDomainResponseRecords]
        """

        self._records = records

    @property
    def region(self):
        """Gets the region of this InlineResponse201.  # noqa: E501

        The region where the domain is hosted.  # noqa: E501

        :return: The region of this InlineResponse201.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this InlineResponse201.

        The region where the domain is hosted.  # noqa: E501

        :param region: The region of this InlineResponse201.  # noqa: E501
        :type: str
        """

        self._region = region

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
        if issubclass(InlineResponse201, dict):
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
        if not isinstance(other, InlineResponse201):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
