from pathlib import Path
import requests
from churn_ml.config import RAW_DATA_PATH, RAW_DATA_URL

def extract_raw_data(output_path: Path = RAW_DATA_PATH, url: str = RAW_DATA_URL) -> Path:
    """
    Extrai o dataset do repositorio da IBM no GitHub ,em formato csv e salva na pasta designada.

    """
    if output_path.exists():
        return output_path
    else:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        output_path.write_bytes(response.content)
        return output_path
if __name__ == "__main__":
    path = extract_raw_data()
    print(f"Dataset bruto disponível em: {path}")