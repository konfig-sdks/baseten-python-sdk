# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from baseten_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_SECRETS = "/v1/secrets"
    V1_MODELS = "/v1/models"
    V1_MODELS_MODEL_ID = "/v1/models/{model_id}"
    V1_MODELS_MODEL_ID_DEPLOYMENTS = "/v1/models/{model_id}/deployments"
    V1_MODELS_MODEL_ID_DEPLOYMENTS_DEVELOPMENT = "/v1/models/{model_id}/deployments/development"
    V1_MODELS_MODEL_ID_DEPLOYMENTS_PRODUCTION = "/v1/models/{model_id}/deployments/production"
    V1_MODELS_MODEL_ID_DEPLOYMENTS_DEPLOYMENT_ID = "/v1/models/{model_id}/deployments/{deployment_id}"
    V1_MODELS_MODEL_ID_DEPLOYMENTS_DEVELOPMENT_AUTOSCALING_SETTINGS = "/v1/models/{model_id}/deployments/development/autoscaling_settings"
    V1_MODELS_MODEL_ID_DEPLOYMENTS_PRODUCTION_AUTOSCALING_SETTINGS = "/v1/models/{model_id}/deployments/production/autoscaling_settings"
    V1_MODELS_MODEL_ID_DEPLOYMENTS_DEPLOYMENT_ID_AUTOSCALING_SETTINGS = "/v1/models/{model_id}/deployments/{deployment_id}/autoscaling_settings"
    V1_MODELS_MODEL_ID_DEPLOYMENTS_DEVELOPMENT_PROMOTE = "/v1/models/{model_id}/deployments/development/promote"
    V1_MODELS_MODEL_ID_DEPLOYMENTS_DEPLOYMENT_ID_PROMOTE = "/v1/models/{model_id}/deployments/{deployment_id}/promote"
