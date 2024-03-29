# coding: utf-8

"""
    Baseten management API

    REST API for management of Baseten resources

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from baseten_python_sdk.paths.v1_secrets.get import GetAllSecretsRaw
from baseten_python_sdk.paths.v1_secrets.post import UpsertNewSecretRaw


class SecretApiRaw(
    GetAllSecretsRaw,
    UpsertNewSecretRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
