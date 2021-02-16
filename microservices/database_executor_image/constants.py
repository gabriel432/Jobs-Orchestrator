class Constants:
    MODULE_PATH_FIELD_NAME = "modulePath"
    CLASS_FIELD_NAME = "class"
    NAME_FIELD_NAME = "name"
    FINISHED_FIELD_NAME = "finished"
    DESCRIPTION_FIELD_NAME = "description"
    METHOD_FIELD_NAME = "method"
    CLASS_PARAMETERS_FIELD_NAME = "classParameters"
    METHOD_PARAMETERS_FIELD_NAME = "methodParameters"
    TYPE_PARAM_NAME = "type"
    TOOL_PARAM_NAME = "tool"

    DEFAULT_MODEL_MICROSERVICE_TYPE = "defaultModel"
    EXCEPTION_FIELD_NAME = "exception"

    EXPLORE_VOLUME_PATH = "EXPLORE_VOLUME_PATH"
    TRANSFORM_VOLUME_PATH = "TRANSFORM_VOLUME_PATH"
    MODELS_VOLUME_PATH = "MODELS_VOLUME_PATH"
    BINARY_VOLUME_PATH = "BINARY_VOLUME_PATH"

    IMAGE_FORMAT = ".png"

    DELETED_MESSAGE = "deleted file"

    HTTP_STATUS_CODE_SUCCESS = 200
    HTTP_STATUS_CODE_SUCCESS_CREATED = 201
    HTTP_STATUS_CODE_CONFLICT = 409
    HTTP_STATUS_CODE_NOT_ACCEPTABLE = 406
    HTTP_STATUS_CODE_NOT_FOUND = 404
    GET_METHOD_NAME = "GET"

    DATABASE_URL = "DATABASE_URL"
    DATABASE_PORT = "DATABASE_PORT"
    DATABASE_NAME = "DATABASE_NAME"
    DATABASE_REPLICA_SET = "DATABASE_REPLICA_SET"

    ID_FIELD_NAME = "_id"
    METADATA_DOCUMENT_ID = 0

    MESSAGE_RESULT = "result"

    EXPLORE_TYPE = "explore"
    TRANSFORM_TYPE = "transform"
    DEFAULT_MODEL_TYPE = "defaultModel"
    TUNE_TYPE = "tune"
    TRAIN_TYPE = "train"
    EVALUATE_TYPE = "evaluate"
    PREDICT_TYPE = "predict"
    PYTHON_TRANSFORM_TYPE = "pythonTransform"

    MICROSERVICE_URI_SWITCHER = {
        "explore": "/api/learningOrchestra/v1/explore/",
        "transform": "/api/learningOrchestra/v1/transform/",

    }

    MICROSERVICE_URI_PATH = "/databaseExecutor"
    MICROSERVICE_URI_GET_PARAMS = "?query={}&limit=20&skip=0"

    FIRST_ARGUMENT = 0
    SECOND_ARGUMENT = 1
