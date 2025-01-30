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

class InlineResponse2004(object):
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
        'data': 'list[CategoriesResponseData]',
        'pagination': 'EmojiResponsePagination',
        'meta': 'RandomIDResponseMeta'
    }

    attribute_map = {
        'data': 'data',
        'pagination': 'pagination',
        'meta': 'meta'
    }

    def __init__(self, data=None, pagination=None, meta=None):  # noqa: E501
        """InlineResponse2004 - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._pagination = None
        self._meta = None
        self.discriminator = None
        if data is not None:
            self.data = data
        if pagination is not None:
            self.pagination = pagination
        if meta is not None:
            self.meta = meta

    @property
    def data(self):
        """Gets the data of this InlineResponse2004.  # noqa: E501


        :return: The data of this InlineResponse2004.  # noqa: E501
        :rtype: list[CategoriesResponseData]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineResponse2004.


        :param data: The data of this InlineResponse2004.  # noqa: E501
        :type: list[CategoriesResponseData]
        """

        self._data = data

    @property
    def pagination(self):
        """Gets the pagination of this InlineResponse2004.  # noqa: E501


        :return: The pagination of this InlineResponse2004.  # noqa: E501
        :rtype: EmojiResponsePagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this InlineResponse2004.


        :param pagination: The pagination of this InlineResponse2004.  # noqa: E501
        :type: EmojiResponsePagination
        """

        self._pagination = pagination

    @property
    def meta(self):
        """Gets the meta of this InlineResponse2004.  # noqa: E501


        :return: The meta of this InlineResponse2004.  # noqa: E501
        :rtype: RandomIDResponseMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this InlineResponse2004.


        :param meta: The meta of this InlineResponse2004.  # noqa: E501
        :type: RandomIDResponseMeta
        """

        self._meta = meta

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
        if issubclass(InlineResponse2004, dict):
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
        if not isinstance(other, InlineResponse2004):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
