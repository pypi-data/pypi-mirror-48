# coding: utf-8

"""
    OOXML Automation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import presalytics_ooxml_automation
from presalytics_ooxml_automation.api.color_types_api import ColorTypesApi  # noqa: E501
from presalytics_ooxml_automation.rest import ApiException


class TestColorTypesApi(unittest.TestCase):
    """ColorTypesApi unit test stubs"""

    def setUp(self):
        self.api = presalytics_ooxml_automation.api.color_types_api.ColorTypesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_color_types_get(self):
        """Test case for color_types_get

        ColorTypes: List All Possible Types  # noqa: E501
        """
        pass

    def test_color_types_get_id(self):
        """Test case for color_types_get_id

        ColorTypes: Get by Id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
