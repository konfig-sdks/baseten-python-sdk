# coding: utf-8

"""
    Baseten management API

    REST API for management of Baseten resources

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import baseten_python_sdk
from baseten_python_sdk.paths.v1_models_model_id_deployments import get
from baseten_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1ModelsModelIdDeployments(ApiTestMixin, unittest.TestCase):
    """
    V1ModelsModelIdDeployments unit test stubs
        Gets all deployments of a model
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
