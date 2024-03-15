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
from pydantic import BaseModel, Field, RootModel

from baseten_python_sdk.pydantic.update_autoscaling_settings_status_v1 import UpdateAutoscalingSettingsStatusV1

class UpdateAutoscalingSettingsResponseV1(BaseModel):
    # Status of the request to update autoscaling settings
    status: UpdateAutoscalingSettingsStatusV1 = Field(alias='status')

    # A message describing the status of the request to update autoscaling settings
    message: str = Field(alias='message')
    class Config:
        arbitrary_types_allowed = True