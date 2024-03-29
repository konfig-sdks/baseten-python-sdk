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


class RequiredAutoscalingSettingsV1(TypedDict):
    # Minimum number of replicas
    min_replica: int

    # Maximum number of replicas
    max_replica: int

    # Timeframe of traffic considered for autoscaling decisions
    autoscaling_window: int

    # Waiting period before scaling down any active replica
    scale_down_delay: int

    # Number of requests per replica before scaling up
    concurrency_target: int

class OptionalAutoscalingSettingsV1(TypedDict, total=False):
    pass

class AutoscalingSettingsV1(RequiredAutoscalingSettingsV1, OptionalAutoscalingSettingsV1):
    pass
