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


class UpdateAutoscalingSettingsResponseV1(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The response to a request to update autoscaling settings.
    """


    class MetaOapg:
        required = {
            "message",
            "status",
        }
        
        class properties:
        
            @staticmethod
            def status() -> typing.Type['UpdateAutoscalingSettingsStatusV1']:
                return UpdateAutoscalingSettingsStatusV1
            message = schemas.StrSchema
            __annotations__ = {
                "status": status,
                "message": message,
            }
    
    message: MetaOapg.properties.message
    status: 'UpdateAutoscalingSettingsStatusV1'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'UpdateAutoscalingSettingsStatusV1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "message", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'UpdateAutoscalingSettingsStatusV1': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "message", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        message: typing.Union[MetaOapg.properties.message, str, ],
        status: 'UpdateAutoscalingSettingsStatusV1',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateAutoscalingSettingsResponseV1':
        return super().__new__(
            cls,
            *args,
            message=message,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from baseten_python_sdk.model.update_autoscaling_settings_status_v1 import UpdateAutoscalingSettingsStatusV1
