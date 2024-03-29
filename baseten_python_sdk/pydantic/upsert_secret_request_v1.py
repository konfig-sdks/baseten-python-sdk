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


class UpsertSecretRequestV1(BaseModel):
    # Name of the new or existing secret
    name: str = Field(alias='name')

    # Value of the secret
    value: str = Field(alias='value')
    class Config:
        arbitrary_types_allowed = True
