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


DeploymentStatusV1 = Literal["BUILDING", "DEPLOYING", "DEPLOY_FAILED", "LOADING_MODEL", "ACTIVE", "UNHEALTHY", "BUILD_FAILED", "BUILD_STOPPED", "DEACTIVATING", "INACTIVE", "FAILED", "UPDATING", "SCALED_TO_ZERO", "WAKING_UP"]
