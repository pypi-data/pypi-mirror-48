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


class SlideSlides(object):
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
        'document_id': 'int',
        'slide_master_id': 'int',
        'number': 'int',
        'ooxml_id': 'int',
        'svg_blob_url': 'str',
        'slide_document_url': 'str',
        'theme_id': 'int',
        'shape_trees_id': 'int',
        'oo_xml_blob_url': 'str',
        'id': 'int',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'document_id': 'DocumentId',
        'slide_master_id': 'SlideMasterId',
        'number': 'Number',
        'ooxml_id': 'OoxmlId',
        'svg_blob_url': 'SvgBlobUrl',
        'slide_document_url': 'SlideDocumentUrl',
        'theme_id': 'ThemeId',
        'shape_trees_id': 'ShapeTreesId',
        'oo_xml_blob_url': 'OoXmlBlobUrl',
        'id': 'Id',
        'date_created': 'DateCreated',
        'user_created': 'UserCreated',
        'date_modified': 'DateModified',
        'user_modified': 'UserModified'
    }

    def __init__(self, document_id=None, slide_master_id=None, number=None, ooxml_id=None, svg_blob_url=None, slide_document_url=None, theme_id=None, shape_trees_id=None, oo_xml_blob_url=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None):  # noqa: E501
        """SlideSlides - a model defined in OpenAPI"""  # noqa: E501

        self._document_id = None
        self._slide_master_id = None
        self._number = None
        self._ooxml_id = None
        self._svg_blob_url = None
        self._slide_document_url = None
        self._theme_id = None
        self._shape_trees_id = None
        self._oo_xml_blob_url = None
        self._id = None
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        if document_id is not None:
            self.document_id = document_id
        if slide_master_id is not None:
            self.slide_master_id = slide_master_id
        if number is not None:
            self.number = number
        if ooxml_id is not None:
            self.ooxml_id = ooxml_id
        if svg_blob_url is not None:
            self.svg_blob_url = svg_blob_url
        if slide_document_url is not None:
            self.slide_document_url = slide_document_url
        if theme_id is not None:
            self.theme_id = theme_id
        if shape_trees_id is not None:
            self.shape_trees_id = shape_trees_id
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
    def document_id(self):
        """Gets the document_id of this SlideSlides.  # noqa: E501


        :return: The document_id of this SlideSlides.  # noqa: E501
        :rtype: int
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this SlideSlides.


        :param document_id: The document_id of this SlideSlides.  # noqa: E501
        :type: int
        """

        self._document_id = document_id

    @property
    def slide_master_id(self):
        """Gets the slide_master_id of this SlideSlides.  # noqa: E501


        :return: The slide_master_id of this SlideSlides.  # noqa: E501
        :rtype: int
        """
        return self._slide_master_id

    @slide_master_id.setter
    def slide_master_id(self, slide_master_id):
        """Sets the slide_master_id of this SlideSlides.


        :param slide_master_id: The slide_master_id of this SlideSlides.  # noqa: E501
        :type: int
        """

        self._slide_master_id = slide_master_id

    @property
    def number(self):
        """Gets the number of this SlideSlides.  # noqa: E501


        :return: The number of this SlideSlides.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this SlideSlides.


        :param number: The number of this SlideSlides.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def ooxml_id(self):
        """Gets the ooxml_id of this SlideSlides.  # noqa: E501


        :return: The ooxml_id of this SlideSlides.  # noqa: E501
        :rtype: int
        """
        return self._ooxml_id

    @ooxml_id.setter
    def ooxml_id(self, ooxml_id):
        """Sets the ooxml_id of this SlideSlides.


        :param ooxml_id: The ooxml_id of this SlideSlides.  # noqa: E501
        :type: int
        """

        self._ooxml_id = ooxml_id

    @property
    def svg_blob_url(self):
        """Gets the svg_blob_url of this SlideSlides.  # noqa: E501


        :return: The svg_blob_url of this SlideSlides.  # noqa: E501
        :rtype: str
        """
        return self._svg_blob_url

    @svg_blob_url.setter
    def svg_blob_url(self, svg_blob_url):
        """Sets the svg_blob_url of this SlideSlides.


        :param svg_blob_url: The svg_blob_url of this SlideSlides.  # noqa: E501
        :type: str
        """

        self._svg_blob_url = svg_blob_url

    @property
    def slide_document_url(self):
        """Gets the slide_document_url of this SlideSlides.  # noqa: E501


        :return: The slide_document_url of this SlideSlides.  # noqa: E501
        :rtype: str
        """
        return self._slide_document_url

    @slide_document_url.setter
    def slide_document_url(self, slide_document_url):
        """Sets the slide_document_url of this SlideSlides.


        :param slide_document_url: The slide_document_url of this SlideSlides.  # noqa: E501
        :type: str
        """

        self._slide_document_url = slide_document_url

    @property
    def theme_id(self):
        """Gets the theme_id of this SlideSlides.  # noqa: E501


        :return: The theme_id of this SlideSlides.  # noqa: E501
        :rtype: int
        """
        return self._theme_id

    @theme_id.setter
    def theme_id(self, theme_id):
        """Sets the theme_id of this SlideSlides.


        :param theme_id: The theme_id of this SlideSlides.  # noqa: E501
        :type: int
        """

        self._theme_id = theme_id

    @property
    def shape_trees_id(self):
        """Gets the shape_trees_id of this SlideSlides.  # noqa: E501


        :return: The shape_trees_id of this SlideSlides.  # noqa: E501
        :rtype: int
        """
        return self._shape_trees_id

    @shape_trees_id.setter
    def shape_trees_id(self, shape_trees_id):
        """Sets the shape_trees_id of this SlideSlides.


        :param shape_trees_id: The shape_trees_id of this SlideSlides.  # noqa: E501
        :type: int
        """

        self._shape_trees_id = shape_trees_id

    @property
    def oo_xml_blob_url(self):
        """Gets the oo_xml_blob_url of this SlideSlides.  # noqa: E501


        :return: The oo_xml_blob_url of this SlideSlides.  # noqa: E501
        :rtype: str
        """
        return self._oo_xml_blob_url

    @oo_xml_blob_url.setter
    def oo_xml_blob_url(self, oo_xml_blob_url):
        """Sets the oo_xml_blob_url of this SlideSlides.


        :param oo_xml_blob_url: The oo_xml_blob_url of this SlideSlides.  # noqa: E501
        :type: str
        """

        self._oo_xml_blob_url = oo_xml_blob_url

    @property
    def id(self):
        """Gets the id of this SlideSlides.  # noqa: E501


        :return: The id of this SlideSlides.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SlideSlides.


        :param id: The id of this SlideSlides.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this SlideSlides.  # noqa: E501


        :return: The date_created of this SlideSlides.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SlideSlides.


        :param date_created: The date_created of this SlideSlides.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this SlideSlides.  # noqa: E501


        :return: The user_created of this SlideSlides.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this SlideSlides.


        :param user_created: The user_created of this SlideSlides.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this SlideSlides.  # noqa: E501


        :return: The date_modified of this SlideSlides.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SlideSlides.


        :param date_modified: The date_modified of this SlideSlides.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this SlideSlides.  # noqa: E501


        :return: The user_modified of this SlideSlides.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this SlideSlides.


        :param user_modified: The user_modified of this SlideSlides.  # noqa: E501
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
        if not isinstance(other, SlideSlides):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
