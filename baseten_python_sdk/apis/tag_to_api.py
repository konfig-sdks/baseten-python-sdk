import typing_extensions

from baseten_python_sdk.apis.tags import TagValues
from baseten_python_sdk.apis.tags.model_api import ModelApi
from baseten_python_sdk.apis.tags.deployment_api import DeploymentApi
from baseten_python_sdk.apis.tags.autoscaling_setting_api import AutoscalingSettingApi
from baseten_python_sdk.apis.tags.secret_api import SecretApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.MODEL: ModelApi,
        TagValues.DEPLOYMENT: DeploymentApi,
        TagValues.AUTOSCALING_SETTING: AutoscalingSettingApi,
        TagValues.SECRET: SecretApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.MODEL: ModelApi,
        TagValues.DEPLOYMENT: DeploymentApi,
        TagValues.AUTOSCALING_SETTING: AutoscalingSettingApi,
        TagValues.SECRET: SecretApi,
    }
)
