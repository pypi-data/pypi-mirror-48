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


class ChartCharts(object):
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
        'parent_graphic_id': 'int',
        'svg_blob_url': 'str',
        'title_text_container_id': 'int',
        'chart_data_id': 'int',
        'axes': 'str',
        'oo_xml_blob_url': 'str',
        'id': 'int',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'parent_graphic_id': 'ParentGraphicId',
        'svg_blob_url': 'SvgBlobUrl',
        'title_text_container_id': 'TitleTextContainerId',
        'chart_data_id': 'ChartDataId',
        'axes': 'Axes',
        'oo_xml_blob_url': 'OoXmlBlobUrl',
        'id': 'Id',
        'date_created': 'DateCreated',
        'user_created': 'UserCreated',
        'date_modified': 'DateModified',
        'user_modified': 'UserModified'
    }

    def __init__(self, parent_graphic_id=None, svg_blob_url=None, title_text_container_id=None, chart_data_id=None, axes=None, oo_xml_blob_url=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None):  # noqa: E501
        """ChartCharts - a model defined in OpenAPI"""  # noqa: E501

        self._parent_graphic_id = None
        self._svg_blob_url = None
        self._title_text_container_id = None
        self._chart_data_id = None
        self._axes = None
        self._oo_xml_blob_url = None
        self._id = None
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        if parent_graphic_id is not None:
            self.parent_graphic_id = parent_graphic_id
        if svg_blob_url is not None:
            self.svg_blob_url = svg_blob_url
        self.title_text_container_id = title_text_container_id
        if chart_data_id is not None:
            self.chart_data_id = chart_data_id
        if axes is not None:
            self.axes = axes
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
    def parent_graphic_id(self):
        """Gets the parent_graphic_id of this ChartCharts.  # noqa: E501


        :return: The parent_graphic_id of this ChartCharts.  # noqa: E501
        :rtype: int
        """
        return self._parent_graphic_id

    @parent_graphic_id.setter
    def parent_graphic_id(self, parent_graphic_id):
        """Sets the parent_graphic_id of this ChartCharts.


        :param parent_graphic_id: The parent_graphic_id of this ChartCharts.  # noqa: E501
        :type: int
        """

        self._parent_graphic_id = parent_graphic_id

    @property
    def svg_blob_url(self):
        """Gets the svg_blob_url of this ChartCharts.  # noqa: E501


        :return: The svg_blob_url of this ChartCharts.  # noqa: E501
        :rtype: str
        """
        return self._svg_blob_url

    @svg_blob_url.setter
    def svg_blob_url(self, svg_blob_url):
        """Sets the svg_blob_url of this ChartCharts.


        :param svg_blob_url: The svg_blob_url of this ChartCharts.  # noqa: E501
        :type: str
        """

        self._svg_blob_url = svg_blob_url

    @property
    def title_text_container_id(self):
        """Gets the title_text_container_id of this ChartCharts.  # noqa: E501


        :return: The title_text_container_id of this ChartCharts.  # noqa: E501
        :rtype: int
        """
        return self._title_text_container_id

    @title_text_container_id.setter
    def title_text_container_id(self, title_text_container_id):
        """Sets the title_text_container_id of this ChartCharts.


        :param title_text_container_id: The title_text_container_id of this ChartCharts.  # noqa: E501
        :type: int
        """

        self._title_text_container_id = title_text_container_id

    @property
    def chart_data_id(self):
        """Gets the chart_data_id of this ChartCharts.  # noqa: E501


        :return: The chart_data_id of this ChartCharts.  # noqa: E501
        :rtype: int
        """
        return self._chart_data_id

    @chart_data_id.setter
    def chart_data_id(self, chart_data_id):
        """Sets the chart_data_id of this ChartCharts.


        :param chart_data_id: The chart_data_id of this ChartCharts.  # noqa: E501
        :type: int
        """

        self._chart_data_id = chart_data_id

    @property
    def axes(self):
        """Gets the axes of this ChartCharts.  # noqa: E501


        :return: The axes of this ChartCharts.  # noqa: E501
        :rtype: str
        """
        return self._axes

    @axes.setter
    def axes(self, axes):
        """Sets the axes of this ChartCharts.


        :param axes: The axes of this ChartCharts.  # noqa: E501
        :type: str
        """

        self._axes = axes

    @property
    def oo_xml_blob_url(self):
        """Gets the oo_xml_blob_url of this ChartCharts.  # noqa: E501


        :return: The oo_xml_blob_url of this ChartCharts.  # noqa: E501
        :rtype: str
        """
        return self._oo_xml_blob_url

    @oo_xml_blob_url.setter
    def oo_xml_blob_url(self, oo_xml_blob_url):
        """Sets the oo_xml_blob_url of this ChartCharts.


        :param oo_xml_blob_url: The oo_xml_blob_url of this ChartCharts.  # noqa: E501
        :type: str
        """

        self._oo_xml_blob_url = oo_xml_blob_url

    @property
    def id(self):
        """Gets the id of this ChartCharts.  # noqa: E501


        :return: The id of this ChartCharts.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChartCharts.


        :param id: The id of this ChartCharts.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this ChartCharts.  # noqa: E501


        :return: The date_created of this ChartCharts.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this ChartCharts.


        :param date_created: The date_created of this ChartCharts.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this ChartCharts.  # noqa: E501


        :return: The user_created of this ChartCharts.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this ChartCharts.


        :param user_created: The user_created of this ChartCharts.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this ChartCharts.  # noqa: E501


        :return: The date_modified of this ChartCharts.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this ChartCharts.


        :param date_modified: The date_modified of this ChartCharts.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this ChartCharts.  # noqa: E501


        :return: The user_modified of this ChartCharts.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this ChartCharts.


        :param user_modified: The user_modified of this ChartCharts.  # noqa: E501
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
        if not isinstance(other, ChartCharts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
