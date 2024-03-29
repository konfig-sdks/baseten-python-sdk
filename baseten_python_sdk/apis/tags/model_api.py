# coding: utf-8

"""
    Baseten management API

    REST API for management of Baseten resources

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from baseten_python_sdk.paths.v1_models_model_id_deployments_development_promote.post import DeployPromote
from baseten_python_sdk.paths.v1_models_model_id_deployments_deployment_id_promote.post import DeploymentPromote
from baseten_python_sdk.paths.v1_models_model_id_deployments.get import GetAllDeployments
from baseten_python_sdk.paths.v1_models.get import GetAllModels
from baseten_python_sdk.paths.v1_models_model_id.get import GetModelById
from baseten_python_sdk.apis.tags.model_api_raw import ModelApiRaw


class ModelApi(
    DeployPromote,
    DeploymentPromote,
    GetAllDeployments,
    GetAllModels,
    GetModelById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ModelApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ModelApiRaw(api_client)
