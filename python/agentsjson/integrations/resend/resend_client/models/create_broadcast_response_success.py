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

class CreateBroadcastResponseSuccess(object):
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
        'object': 'str'
    }

    attribute_map = {
        'id': 'id',
        'object': 'object'
    }

    def __init__(self, id=None, object=None):  # noqa: E501
        """CreateBroadcastResponseSuccess - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._object = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if object is not None:
            self.object = object

    @property
    def id(self):
        """Gets the id of this CreateBroadcastResponseSuccess.  # noqa: E501

        The ID of the broadcast.  # noqa: E501

        :return: The id of this CreateBroadcastResponseSuccess.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateBroadcastResponseSuccess.

        The ID of the broadcast.  # noqa: E501

        :param id: The id of this CreateBroadcastResponseSuccess.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def object(self):
        """Gets the object of this CreateBroadcastResponseSuccess.  # noqa: E501

        The object type of the response.  # noqa: E501

        :return: The object of this CreateBroadcastResponseSuccess.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this CreateBroadcastResponseSuccess.

        The object type of the response.  # noqa: E501

        :param object: The object of this CreateBroadcastResponseSuccess.  # noqa: E501
        :type: str
        """

        self._object = object

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
        if issubclass(CreateBroadcastResponseSuccess, dict):
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
        if not isinstance(other, CreateBroadcastResponseSuccess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
