# coding: utf-8

"""
    Giphy API

    The Giphy API allows you to search, upload, and manage GIFs and stickers. It provides endpoints to access trending content, search for specific GIFs, translate phrases into GIFs, and more.   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UserObject(object):
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
        'avatar_url': 'str',
        'banner_url': 'str',
        'profile_url': 'str',
        'username': 'str',
        'display_name': 'str'
    }

    attribute_map = {
        'avatar_url': 'avatar_url',
        'banner_url': 'banner_url',
        'profile_url': 'profile_url',
        'username': 'username',
        'display_name': 'display_name'
    }

    def __init__(self, avatar_url=None, banner_url=None, profile_url=None, username=None, display_name=None):  # noqa: E501
        """UserObject - a model defined in Swagger"""  # noqa: E501
        self._avatar_url = None
        self._banner_url = None
        self._profile_url = None
        self._username = None
        self._display_name = None
        self.discriminator = None
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if banner_url is not None:
            self.banner_url = banner_url
        if profile_url is not None:
            self.profile_url = profile_url
        if username is not None:
            self.username = username
        if display_name is not None:
            self.display_name = display_name

    @property
    def avatar_url(self):
        """Gets the avatar_url of this UserObject.  # noqa: E501

        The URL for this user's avatar image.  # noqa: E501

        :return: The avatar_url of this UserObject.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this UserObject.

        The URL for this user's avatar image.  # noqa: E501

        :param avatar_url: The avatar_url of this UserObject.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def banner_url(self):
        """Gets the banner_url of this UserObject.  # noqa: E501

        The URL for the banner image that appears atop this user's profile page.  # noqa: E501

        :return: The banner_url of this UserObject.  # noqa: E501
        :rtype: str
        """
        return self._banner_url

    @banner_url.setter
    def banner_url(self, banner_url):
        """Sets the banner_url of this UserObject.

        The URL for the banner image that appears atop this user's profile page.  # noqa: E501

        :param banner_url: The banner_url of this UserObject.  # noqa: E501
        :type: str
        """

        self._banner_url = banner_url

    @property
    def profile_url(self):
        """Gets the profile_url of this UserObject.  # noqa: E501

        The URL for this user's GIPHY profile.  # noqa: E501

        :return: The profile_url of this UserObject.  # noqa: E501
        :rtype: str
        """
        return self._profile_url

    @profile_url.setter
    def profile_url(self, profile_url):
        """Sets the profile_url of this UserObject.

        The URL for this user's GIPHY profile.  # noqa: E501

        :param profile_url: The profile_url of this UserObject.  # noqa: E501
        :type: str
        """

        self._profile_url = profile_url

    @property
    def username(self):
        """Gets the username of this UserObject.  # noqa: E501

        The username associated with this user.  # noqa: E501

        :return: The username of this UserObject.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserObject.

        The username associated with this user.  # noqa: E501

        :param username: The username of this UserObject.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def display_name(self):
        """Gets the display_name of this UserObject.  # noqa: E501

        The display name associated with this user.  # noqa: E501

        :return: The display_name of this UserObject.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UserObject.

        The display name associated with this user.  # noqa: E501

        :param display_name: The display_name of this UserObject.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

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
        if issubclass(UserObject, dict):
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
        if not isinstance(other, UserObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
