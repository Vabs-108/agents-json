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

class ApikeysBody(object):
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
        'name': 'str',
        'permission': 'str',
        'domain_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'permission': 'permission',
        'domain_id': 'domain_id'
    }

    def __init__(self, name=None, permission=None, domain_id=None):  # noqa: E501
        """ApikeysBody - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._permission = None
        self._domain_id = None
        self.discriminator = None
        self.name = name
        if permission is not None:
            self.permission = permission
        if domain_id is not None:
            self.domain_id = domain_id

    @property
    def name(self):
        """Gets the name of this ApikeysBody.  # noqa: E501

        The API key name.  # noqa: E501

        :return: The name of this ApikeysBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApikeysBody.

        The API key name.  # noqa: E501

        :param name: The name of this ApikeysBody.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def permission(self):
        """Gets the permission of this ApikeysBody.  # noqa: E501

        The API key can have full access to Resend’s API or be only restricted to send emails. * full_access - Can create, delete, get, and update any resource. * sending_access - Can only send emails.  # noqa: E501

        :return: The permission of this ApikeysBody.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this ApikeysBody.

        The API key can have full access to Resend’s API or be only restricted to send emails. * full_access - Can create, delete, get, and update any resource. * sending_access - Can only send emails.  # noqa: E501

        :param permission: The permission of this ApikeysBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["full_access", "sending_access"]  # noqa: E501
        if permission not in allowed_values:
            raise ValueError(
                "Invalid value for `permission` ({0}), must be one of {1}"  # noqa: E501
                .format(permission, allowed_values)
            )

        self._permission = permission

    @property
    def domain_id(self):
        """Gets the domain_id of this ApikeysBody.  # noqa: E501

        Restrict an API key to send emails only from a specific domain. Only used when the permission is sending_acces.  # noqa: E501

        :return: The domain_id of this ApikeysBody.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ApikeysBody.

        Restrict an API key to send emails only from a specific domain. Only used when the permission is sending_acces.  # noqa: E501

        :param domain_id: The domain_id of this ApikeysBody.  # noqa: E501
        :type: str
        """

        self._domain_id = domain_id

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
        if issubclass(ApikeysBody, dict):
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
        if not isinstance(other, ApikeysBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
