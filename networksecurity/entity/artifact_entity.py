from dataclasses import dataclass
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging
import os
import sys


@dataclass
class DataIngestionArtifact:
    pass

@dataclass
class DataValidationArtifact:
    pass

@dataclass
class DataTransformationArtifact:
    pass

@dataclass
class ModelTrainerArtifact:
    pass

@dataclass
class ModeEvaluationArtifact:
    pass


@dataclass
class ModelPusherArtifact:
    pass

@dataclass
class ClassificationMetricArtifact:
    pass
