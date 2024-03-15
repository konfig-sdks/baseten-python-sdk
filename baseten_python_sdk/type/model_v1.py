# coding: utf-8

"""
    Baseten management API

    REST API for management of Baseten resources

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredModelV1(TypedDict):
    # Unique identifier of the model
    id: str

    # Time the model was created in ISO 8601 format
    created_at: datetime

    # Name of the model
    name: str

    # Number of deployments of the model
    deployments_count: int

    # Unique identifier of the production deployment of the model
    production_deployment_id: str

    # Unique identifier of the development deployment of the model
    development_deployment_id: str

    # Name of the instance type the model is deployed on
    instance_type_name: str

class OptionalModelV1(TypedDict, total=False):
    pass

class ModelV1(RequiredModelV1, OptionalModelV1):
    pass