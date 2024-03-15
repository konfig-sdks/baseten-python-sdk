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


class UpdateAutoscalingSettingsV1(BaseModel):
    # Minimum number of replicas
    min_replica: typing.Optional[int] = Field(None, alias='min_replica')

    # Maximum number of replicas
    max_replica: typing.Optional[int] = Field(None, alias='max_replica')

    # Timeframe of traffic considered for autoscaling decisions
    autoscaling_window: typing.Optional[int] = Field(None, alias='autoscaling_window')

    # Waiting period before scaling down any active replica
    scale_down_delay: typing.Optional[int] = Field(None, alias='scale_down_delay')

    # Number of requests per replica before scaling up
    concurrency_target: typing.Optional[int] = Field(None, alias='concurrency_target')
    class Config:
        arbitrary_types_allowed = True