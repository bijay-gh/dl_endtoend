import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name = "Xray"

list_of_files = [
    ".github/workflows/ci.yaml",
    ".github/workflows/main.yaml",
    "Notebook/experiments.ipynb",
    "bentofile.yaml",
    "inti_setup.sh",
    "main.py",
    "requirements.txt",
    "setup.py",
    "requirements_dev.txt",
    "setup.cfg",
    "tox.ini",
    "test.py",
    "test/integration_test/__init__.py",
    "test/unit_test/__init__.py",
    f"{project_name}/__init__.py",
    f"{project_name}/logger.py",
    f"{project_name}/exception.py",
    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/cloud_storage/s3_operation.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/ml/__init__.py",
    f"{project_name}/ml/model/__init__.py",
    f"{project_name}/ml/model/architecture.py",
    f"{project_name}/ml/model/model_service.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
]

for file_path in list_of_files:
    filepath = Path(file_path)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating a new file: {filepath}")
    else:
        logging.info(f"{filename} already exists!")