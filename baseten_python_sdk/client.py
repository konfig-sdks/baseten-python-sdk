# coding: utf-8
"""
    Baseten management API

    REST API for management of Baseten resources

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from baseten_python_sdk.client_custom import ClientCustom
from baseten_python_sdk.configuration import Configuration
from baseten_python_sdk.api_client import ApiClient
from baseten_python_sdk.type_util import copy_signature
from baseten_python_sdk.apis.tags.autoscaling_setting_api import AutoscalingSettingApi
from baseten_python_sdk.apis.tags.deployment_api import DeploymentApi
from baseten_python_sdk.apis.tags.model_api import ModelApi
from baseten_python_sdk.apis.tags.secret_api import SecretApi



class Baseten(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.autoscaling_setting: AutoscalingSettingApi = AutoscalingSettingApi(api_client)
        self.deployment: DeploymentApi = DeploymentApi(api_client)
        self.model: ModelApi = ModelApi(api_client)
        self.secret: SecretApi = SecretApi(api_client)
