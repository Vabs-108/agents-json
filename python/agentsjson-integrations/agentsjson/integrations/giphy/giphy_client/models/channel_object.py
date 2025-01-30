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

class ChannelObject(object):
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
        'id': 'int',
        'url': 'str',
        'display_name': 'str',
        'slug': 'str',
        'type': 'str',
        'user': 'GIFObjectUser',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'display_name': 'display_name',
        'slug': 'slug',
        'type': 'type',
        'user': 'user',
        'description': 'description'
    }

    def __init__(self, id=None, url=None, display_name=None, slug=None, type=None, user=None, description=None):  # noqa: E501
        """ChannelObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._url = None
        self._display_name = None
        self._slug = None
        self._type = None
        self._user = None
        self._description = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        if display_name is not None:
            self.display_name = display_name
        if slug is not None:
            self.slug = slug
        if type is not None:
            self.type = type
        if user is not None:
            self.user = user
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this ChannelObject.  # noqa: E501

        Channel unique ID.  # noqa: E501

        :return: The id of this ChannelObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChannelObject.

        Channel unique ID.  # noqa: E501

        :param id: The id of this ChannelObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this ChannelObject.  # noqa: E501

        Channel relative URL.  # noqa: E501

        :return: The url of this ChannelObject.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ChannelObject.

        Channel relative URL.  # noqa: E501

        :param url: The url of this ChannelObject.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def display_name(self):
        """Gets the display_name of this ChannelObject.  # noqa: E501

        The display name of the channel.  # noqa: E501

        :return: The display_name of this ChannelObject.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ChannelObject.

        The display name of the channel.  # noqa: E501

        :param display_name: The display_name of this ChannelObject.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def slug(self):
        """Gets the slug of this ChannelObject.  # noqa: E501

        The unique channel slug.  # noqa: E501

        :return: The slug of this ChannelObject.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this ChannelObject.

        The unique channel slug.  # noqa: E501

        :param slug: The slug of this ChannelObject.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def type(self):
        """Gets the type of this ChannelObject.  # noqa: E501

        Possible values are `community` or `editorial`.  # noqa: E501

        :return: The type of this ChannelObject.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ChannelObject.

        Possible values are `community` or `editorial`.  # noqa: E501

        :param type: The type of this ChannelObject.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def user(self):
        """Gets the user of this ChannelObject.  # noqa: E501


        :return: The user of this ChannelObject.  # noqa: E501
        :rtype: GIFObjectUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ChannelObject.


        :param user: The user of this ChannelObject.  # noqa: E501
        :type: GIFObjectUser
        """

        self._user = user

    @property
    def description(self):
        """Gets the description of this ChannelObject.  # noqa: E501

        Channel description.  # noqa: E501

        :return: The description of this ChannelObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ChannelObject.

        Channel description.  # noqa: E501

        :param description: The description of this ChannelObject.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(ChannelObject, dict):
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
        if not isinstance(other, ChannelObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
