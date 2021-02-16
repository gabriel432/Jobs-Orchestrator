class Constants:
    MODULE_PATH_FIELD_NAME = "modulePath"
    CLASS_FIELD_NAME = "class"
    PARENT_NAME_FIELD_NAME = "parentName"
    NAME_FIELD_NAME = "name"
    FINISHED_FIELD_NAME = "finished"
    DESCRIPTION_FIELD_NAME = "description"
    METHOD_FIELD_NAME = "method"
    METHOD_PARAMETERS_FIELD_NAME = "methodParameters"
    TYPE_FIELD_NAME = "type"
    EXCEPTION_FIELD_NAME = "exception"

    MODELS_VOLUME_PATH = "MODELS_VOLUME_PATH"
    BINARY_VOLUME_PATH = "BINARY_VOLUME_PATH"
    TRANSFORM_VOLUME_PATH = "TRANSFORM_VOLUME_PATH"

    DELETED_MESSAGE = "deleted file"

    HTTP_STATUS_CODE_SUCCESS = 200
    HTTP_STATUS_CODE_SUCCESS_CREATED = 201
    HTTP_STATUS_CODE_CONFLICT = 409
    HTTP_STATUS_CODE_NOT_ACCEPTABLE = 406
    GET_METHOD_NAME = "GET"

    DATABASE_URL = "DATABASE_URL"
    DATABASE_PORT = "DATABASE_PORT"
    DATABASE_NAME = "DATABASE_NAME"
    DATABASE_REPLICA_SET = "DATABASE_REPLICA_SET"

    ID_FIELD_NAME = "_id"
    METADATA_DOCUMENT_ID = 0

    MESSAGE_RESULT = "result"

    MICROSERVICE_URI_SWITCHER = {
        "tune": "/api/learningOrchestra/v1/tune",
        "train": "/api/learningOrchestra/v1/train",
        "evaluate": "/api/learningOrchestra/v1/evaluate",
        "predict": "/api/learningOrchestra/v1/predict"
    }

    DEFAULT_MODEL_TYPE = "defaultModel"
    TUNE_TYPE = "tune"
    TRAIN_TYPE = "train"
    EVALUATE_TYPE = "evaluate"
    PREDICT_TYPE = "predict"
    TRANSFORM_TYPE = "transform"
    PYTHON_TRANSFORM_TYPE = "pythonTransform"

    MICROSERVICE_URI_PATH = "/binaryExecutor"
    MICROSERVICE_URI_GET_PARAMS = "?query={}&limit=20&skip=0"

    FIRST_ARGUMENT = 0
    SECOND_ARGUMENT = 1
