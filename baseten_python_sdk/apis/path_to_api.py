import typing_extensions

from baseten_python_sdk.paths import PathValues
from baseten_python_sdk.apis.paths.v1_secrets import V1Secrets
from baseten_python_sdk.apis.paths.v1_models import V1Models
from baseten_python_sdk.apis.paths.v1_models_model_id import V1ModelsModelId
from baseten_python_sdk.apis.paths.v1_models_model_id_deployments import V1ModelsModelIdDeployments
from baseten_python_sdk.apis.paths.v1_models_model_id_deployments_development import V1ModelsModelIdDeploymentsDevelopment
from baseten_python_sdk.apis.paths.v1_models_model_id_deployments_production import V1ModelsModelIdDeploymentsProduction
from baseten_python_sdk.apis.paths.v1_models_model_id_deployments_deployment_id import V1ModelsModelIdDeploymentsDeploymentId
from baseten_python_sdk.apis.paths.v1_models_model_id_deployments_development_autoscaling_settings import V1ModelsModelIdDeploymentsDevelopmentAutoscalingSettings
from baseten_python_sdk.apis.paths.v1_models_model_id_deployments_production_autoscaling_settings import V1ModelsModelIdDeploymentsProductionAutoscalingSettings
from baseten_python_sdk.apis.paths.v1_models_model_id_deployments_deployment_id_autoscaling_settings import V1ModelsModelIdDeploymentsDeploymentIdAutoscalingSettings
from baseten_python_sdk.apis.paths.v1_models_model_id_deployments_development_promote import V1ModelsModelIdDeploymentsDevelopmentPromote
from baseten_python_sdk.apis.paths.v1_models_model_id_deployments_deployment_id_promote import V1ModelsModelIdDeploymentsDeploymentIdPromote

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_SECRETS: V1Secrets,
        PathValues.V1_MODELS: V1Models,
        PathValues.V1_MODELS_MODEL_ID: V1ModelsModelId,
        PathValues.V1_MODELS_MODEL_ID_DEPLOYMENTS: V1ModelsModelIdDeployments,
        PathValues.V1_MODELS_MODEL_ID_DEPLOYMENTS_DEVELOPMENT: V1ModelsModelIdDeploymentsDevelopment,
        PathValues.V1_MODELS_MODEL_ID_DEPLOYMENTS_PRODUCTION: V1ModelsModelIdDeploymentsProduction,
        PathValues.V1_MODELS_MODEL_ID_DEPLOYMENTS_DEPLOYMENT_ID: V1ModelsModelIdDeploymentsDeploymentId,
        PathValues.V1_MODELS_MODEL_ID_DEPLOYMENTS_DEVELOPMENT_AUTOSCALING_SETTINGS: V1ModelsModelIdDeploymentsDevelopmentAutoscalingSettings,
        PathValues.V1_MODELS_MODEL_ID_DEPLOYMENTS_PRODUCTION_AUTOSCALING_SETTINGS: V1ModelsModelIdDeploymentsProductionAutoscalingSettings,
        PathValues.V1_MODELS_MODEL_ID_DEPLOYMENTS_DEPLOYMENT_ID_AUTOSCALING_SETTINGS: V1ModelsModelIdDeploymentsDeploymentIdAutoscalingSettings,
        PathValues.V1_MODELS_MODEL_ID_DEPLOYMENTS_DEVELOPMENT_PROMOTE: V1ModelsModelIdDeploymentsDevelopmentPromote,
        PathValues.V1_MODELS_MODEL_ID_DEPLOYMENTS_DEPLOYMENT_ID_PROMOTE: V1ModelsModelIdDeploymentsDeploymentIdPromote,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_SECRETS: V1Secrets,
        PathValues.V1_MODELS: V1Models,
        PathValues.V1_MODELS_MODEL_ID: V1ModelsModelId,
        PathValues.V1_MODELS_MODEL_ID_DEPLOYMENTS: V1ModelsModelIdDeployments,
        PathValues.V1_MODELS_MODEL_ID_DEPLOYMENTS_DEVELOPMENT: V1ModelsModelIdDeploymentsDevelopment,
        PathValues.V1_MODELS_MODEL_ID_DEPLOYMENTS_PRODUCTION: V1ModelsModelIdDeploymentsProduction,
        PathValues.V1_MODELS_MODEL_ID_DEPLOYMENTS_DEPLOYMENT_ID: V1ModelsModelIdDeploymentsDeploymentId,
        PathValues.V1_MODELS_MODEL_ID_DEPLOYMENTS_DEVELOPMENT_AUTOSCALING_SETTINGS: V1ModelsModelIdDeploymentsDevelopmentAutoscalingSettings,
        PathValues.V1_MODELS_MODEL_ID_DEPLOYMENTS_PRODUCTION_AUTOSCALING_SETTINGS: V1ModelsModelIdDeploymentsProductionAutoscalingSettings,
        PathValues.V1_MODELS_MODEL_ID_DEPLOYMENTS_DEPLOYMENT_ID_AUTOSCALING_SETTINGS: V1ModelsModelIdDeploymentsDeploymentIdAutoscalingSettings,
        PathValues.V1_MODELS_MODEL_ID_DEPLOYMENTS_DEVELOPMENT_PROMOTE: V1ModelsModelIdDeploymentsDevelopmentPromote,
        PathValues.V1_MODELS_MODEL_ID_DEPLOYMENTS_DEPLOYMENT_ID_PROMOTE: V1ModelsModelIdDeploymentsDeploymentIdPromote,
    }
)
