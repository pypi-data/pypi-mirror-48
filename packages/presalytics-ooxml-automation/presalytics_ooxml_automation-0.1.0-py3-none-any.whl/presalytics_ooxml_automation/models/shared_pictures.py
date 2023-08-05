# coding: utf-8

"""
    OOXML Automation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SharedPictures(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'graphics_id': 'int',
        'image_file_blob_url': 'str',
        'file_extension': 'str',
        'oo_xml_blob_url': 'str',
        'id': 'int',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'graphics_id': 'GraphicsId',
        'image_file_blob_url': 'ImageFileBlobUrl',
        'file_extension': 'FileExtension',
        'oo_xml_blob_url': 'OoXmlBlobUrl',
        'id': 'Id',
        'date_created': 'DateCreated',
        'user_created': 'UserCreated',
        'date_modified': 'DateModified',
        'user_modified': 'UserModified'
    }

    def __init__(self, graphics_id=None, image_file_blob_url=None, file_extension=None, oo_xml_blob_url=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None):  # noqa: E501
        """SharedPictures - a model defined in OpenAPI"""  # noqa: E501

        self._graphics_id = None
        self._image_file_blob_url = None
        self._file_extension = None
        self._oo_xml_blob_url = None
        self._id = None
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        if graphics_id is not None:
            self.graphics_id = graphics_id
        if image_file_blob_url is not None:
            self.image_file_blob_url = image_file_blob_url
        if file_extension is not None:
            self.file_extension = file_extension
        if oo_xml_blob_url is not None:
            self.oo_xml_blob_url = oo_xml_blob_url
        if id is not None:
            self.id = id
        if date_created is not None:
            self.date_created = date_created
        if user_created is not None:
            self.user_created = user_created
        if date_modified is not None:
            self.date_modified = date_modified
        if user_modified is not None:
            self.user_modified = user_modified

    @property
    def graphics_id(self):
        """Gets the graphics_id of this SharedPictures.  # noqa: E501


        :return: The graphics_id of this SharedPictures.  # noqa: E501
        :rtype: int
        """
        return self._graphics_id

    @graphics_id.setter
    def graphics_id(self, graphics_id):
        """Sets the graphics_id of this SharedPictures.


        :param graphics_id: The graphics_id of this SharedPictures.  # noqa: E501
        :type: int
        """

        self._graphics_id = graphics_id

    @property
    def image_file_blob_url(self):
        """Gets the image_file_blob_url of this SharedPictures.  # noqa: E501


        :return: The image_file_blob_url of this SharedPictures.  # noqa: E501
        :rtype: str
        """
        return self._image_file_blob_url

    @image_file_blob_url.setter
    def image_file_blob_url(self, image_file_blob_url):
        """Sets the image_file_blob_url of this SharedPictures.


        :param image_file_blob_url: The image_file_blob_url of this SharedPictures.  # noqa: E501
        :type: str
        """

        self._image_file_blob_url = image_file_blob_url

    @property
    def file_extension(self):
        """Gets the file_extension of this SharedPictures.  # noqa: E501


        :return: The file_extension of this SharedPictures.  # noqa: E501
        :rtype: str
        """
        return self._file_extension

    @file_extension.setter
    def file_extension(self, file_extension):
        """Sets the file_extension of this SharedPictures.


        :param file_extension: The file_extension of this SharedPictures.  # noqa: E501
        :type: str
        """

        self._file_extension = file_extension

    @property
    def oo_xml_blob_url(self):
        """Gets the oo_xml_blob_url of this SharedPictures.  # noqa: E501


        :return: The oo_xml_blob_url of this SharedPictures.  # noqa: E501
        :rtype: str
        """
        return self._oo_xml_blob_url

    @oo_xml_blob_url.setter
    def oo_xml_blob_url(self, oo_xml_blob_url):
        """Sets the oo_xml_blob_url of this SharedPictures.


        :param oo_xml_blob_url: The oo_xml_blob_url of this SharedPictures.  # noqa: E501
        :type: str
        """

        self._oo_xml_blob_url = oo_xml_blob_url

    @property
    def id(self):
        """Gets the id of this SharedPictures.  # noqa: E501


        :return: The id of this SharedPictures.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedPictures.


        :param id: The id of this SharedPictures.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this SharedPictures.  # noqa: E501


        :return: The date_created of this SharedPictures.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SharedPictures.


        :param date_created: The date_created of this SharedPictures.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this SharedPictures.  # noqa: E501


        :return: The user_created of this SharedPictures.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this SharedPictures.


        :param user_created: The user_created of this SharedPictures.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this SharedPictures.  # noqa: E501


        :return: The date_modified of this SharedPictures.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SharedPictures.


        :param date_modified: The date_modified of this SharedPictures.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this SharedPictures.  # noqa: E501


        :return: The user_modified of this SharedPictures.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this SharedPictures.


        :param user_modified: The user_modified of this SharedPictures.  # noqa: E501
        :type: str
        """

        self._user_modified = user_modified

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SharedPictures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
