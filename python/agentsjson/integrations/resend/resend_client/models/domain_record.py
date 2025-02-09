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

class DomainRecord(object):
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
        'record': 'str',
        'name': 'str',
        'type': 'str',
        'ttl': 'str',
        'status': 'str',
        'value': 'str',
        'priority': 'int'
    }

    attribute_map = {
        'record': 'record',
        'name': 'name',
        'type': 'type',
        'ttl': 'ttl',
        'status': 'status',
        'value': 'value',
        'priority': 'priority'
    }

    def __init__(self, record=None, name=None, type=None, ttl=None, status=None, value=None, priority=None):  # noqa: E501
        """DomainRecord - a model defined in Swagger"""  # noqa: E501
        self._record = None
        self._name = None
        self._type = None
        self._ttl = None
        self._status = None
        self._value = None
        self._priority = None
        self.discriminator = None
        if record is not None:
            self.record = record
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if ttl is not None:
            self.ttl = ttl
        if status is not None:
            self.status = status
        if value is not None:
            self.value = value
        if priority is not None:
            self.priority = priority

    @property
    def record(self):
        """Gets the record of this DomainRecord.  # noqa: E501

        The type of record.  # noqa: E501

        :return: The record of this DomainRecord.  # noqa: E501
        :rtype: str
        """
        return self._record

    @record.setter
    def record(self, record):
        """Sets the record of this DomainRecord.

        The type of record.  # noqa: E501

        :param record: The record of this DomainRecord.  # noqa: E501
        :type: str
        """

        self._record = record

    @property
    def name(self):
        """Gets the name of this DomainRecord.  # noqa: E501

        The name of the record.  # noqa: E501

        :return: The name of this DomainRecord.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DomainRecord.

        The name of the record.  # noqa: E501

        :param name: The name of this DomainRecord.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this DomainRecord.  # noqa: E501

        The type of record.  # noqa: E501

        :return: The type of this DomainRecord.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DomainRecord.

        The type of record.  # noqa: E501

        :param type: The type of this DomainRecord.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def ttl(self):
        """Gets the ttl of this DomainRecord.  # noqa: E501

        The time to live for the record.  # noqa: E501

        :return: The ttl of this DomainRecord.  # noqa: E501
        :rtype: str
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this DomainRecord.

        The time to live for the record.  # noqa: E501

        :param ttl: The ttl of this DomainRecord.  # noqa: E501
        :type: str
        """

        self._ttl = ttl

    @property
    def status(self):
        """Gets the status of this DomainRecord.  # noqa: E501

        The status of the record.  # noqa: E501

        :return: The status of this DomainRecord.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DomainRecord.

        The status of the record.  # noqa: E501

        :param status: The status of this DomainRecord.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def value(self):
        """Gets the value of this DomainRecord.  # noqa: E501

        The value of the record.  # noqa: E501

        :return: The value of this DomainRecord.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DomainRecord.

        The value of the record.  # noqa: E501

        :param value: The value of this DomainRecord.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def priority(self):
        """Gets the priority of this DomainRecord.  # noqa: E501

        The priority of the record.  # noqa: E501

        :return: The priority of this DomainRecord.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this DomainRecord.

        The priority of the record.  # noqa: E501

        :param priority: The priority of this DomainRecord.  # noqa: E501
        :type: int
        """

        self._priority = priority

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
        if issubclass(DomainRecord, dict):
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
        if not isinstance(other, DomainRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
