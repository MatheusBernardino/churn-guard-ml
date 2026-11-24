"""Configurações centralizadas de caminhos, colunas e hiperparâmetros do projeto."""

from pathlib import Path

# Diretórios principais
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_PATH = DATA_DIR / "raw" / "telco_churn_raw.csv"
RAW_DATA_URL = (
    "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/"
    "master/data/Telco-Customer-Churn.csv"
)
PROCESSED_DATA_PATH = DATA_DIR / "processed" / "telco_clean.parquet"

MODELS_DIR = PROJECT_ROOT / "models"
CHAMPION_MODEL_PATH = MODELS_DIR / "champion_model.pkl"

REPORTS_DIR = PROJECT_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# Esquema das colunas do Telco Customer Churn
ID_COLUMN = "customerID"
TARGET_COLUMN = "Churn"

NUMERIC_FEATURES: list[str] = [
    "SeniorCitizen",
    "tenure",
    "MonthlyCharges",
    "TotalCharges",
]

CATEGORICAL_FEATURES: list[str] = [
    "gender",
    "Partner",
    "Dependents",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod",
]

ALL_FEATURES: list[str] = NUMERIC_FEATURES + CATEGORICAL_FEATURES

# Parâmetros gerais de modelagem
RANDOM_STATE = 42
TEST_SIZE = 0.20
CV_FOLDS = 5
SCORING_METRIC = "roc_auc"

# Faixas de risco para classificação de negócio na API
LOW_RISK_THRESHOLD = 0.35
HIGH_RISK_THRESHOLD = 0.65
