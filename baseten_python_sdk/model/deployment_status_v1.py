# coding: utf-8

"""
    Baseten management API

    REST API for management of Baseten resources

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from baseten_python_sdk import schemas  # noqa: F401


class DeploymentStatusV1(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The status of a deployment.
    """


    class MetaOapg:
        enum_value_to_name = {
            "BUILDING": "BUILDING",
            "DEPLOYING": "DEPLOYING",
            "DEPLOY_FAILED": "DEPLOY_FAILED",
            "LOADING_MODEL": "LOADING_MODEL",
            "ACTIVE": "ACTIVE",
            "UNHEALTHY": "UNHEALTHY",
            "BUILD_FAILED": "BUILD_FAILED",
            "BUILD_STOPPED": "BUILD_STOPPED",
            "DEACTIVATING": "DEACTIVATING",
            "INACTIVE": "INACTIVE",
            "FAILED": "FAILED",
            "UPDATING": "UPDATING",
            "SCALED_TO_ZERO": "SCALED_TO_ZERO",
            "WAKING_UP": "WAKING_UP",
        }
    
    @schemas.classproperty
    def BUILDING(cls):
        return cls("BUILDING")
    
    @schemas.classproperty
    def DEPLOYING(cls):
        return cls("DEPLOYING")
    
    @schemas.classproperty
    def DEPLOY_FAILED(cls):
        return cls("DEPLOY_FAILED")
    
    @schemas.classproperty
    def LOADING_MODEL(cls):
        return cls("LOADING_MODEL")
    
    @schemas.classproperty
    def ACTIVE(cls):
        return cls("ACTIVE")
    
    @schemas.classproperty
    def UNHEALTHY(cls):
        return cls("UNHEALTHY")
    
    @schemas.classproperty
    def BUILD_FAILED(cls):
        return cls("BUILD_FAILED")
    
    @schemas.classproperty
    def BUILD_STOPPED(cls):
        return cls("BUILD_STOPPED")
    
    @schemas.classproperty
    def DEACTIVATING(cls):
        return cls("DEACTIVATING")
    
    @schemas.classproperty
    def INACTIVE(cls):
        return cls("INACTIVE")
    
    @schemas.classproperty
    def FAILED(cls):
        return cls("FAILED")
    
    @schemas.classproperty
    def UPDATING(cls):
        return cls("UPDATING")
    
    @schemas.classproperty
    def SCALED_TO_ZERO(cls):
        return cls("SCALED_TO_ZERO")
    
    @schemas.classproperty
    def WAKING_UP(cls):
        return cls("WAKING_UP")
