from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging
from datetime import datetime
import os
import sys
from networksecurity.constant import training_pipeline

print(training_pipeline.ARTIFACT_DIR)


class TrainingPipelineConfig:
    def __init__(self):
        pass
class DataIngestionConfig:
    def __init__(self):
        self.feature_store_path = 
        self.train_test_split_ratio = 
        training_file_path
        testing_file_path

class DataValidationConfig:
    def __init__(self):
        pass

class DataTransformationConfig:
    def __init__(self):
        pass

class ModelTrainerConfig:
    def __init__(self):
        pass

class ModelEvaluationConfig:
    def __init__(self):
        pass

class ModelPusherConfig:
    def __init__(self):
        pass
