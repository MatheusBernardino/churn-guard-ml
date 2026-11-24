# ChurnGuard: Pipeline Ponta a Ponta para Predição de Evasão de Clientes

Projeto final da disciplina **Engenharia de Sistemas Inteligentes (CK0444 – UFC)** voltado para a **Predição de Churn de Clientes** utilizando a base pública *Telco Customer Churn* (IBM/Kaggle).

## Arquitetura do Projeto

O sistema é organizado em três módulos principais:

1. **Módulo de Pipeline de Dados (`src/churn_ml/data/`):** extração do dataset bruto imutável, limpeza, tratamento de inconsistências, validação de schema e exportação em `.parquet`.
2. **Módulo de Pipeline de Modelos (`src/churn_ml/model/`):** divisão estratificada, pré-processamento encapsulado (`ColumnTransformer` + `SMOTE`), benchmark com `GridSearchCV` (`LRC`, `RFC`, `GBC`, `SVC`), geração de relatórios em `reports/` e exportação do modelo campeão (`models/champion_model.pkl`).
3. **Módulo de Serviço (`src/churn_ml/service/`):** API REST em **FastAPI** com validação Pydantic para inferência em tempo real (`GET /health` e `POST /predict`).

## Estrutura de Diretórios

```text
churn-guard-ml/
├── data/
│   ├── raw/          # Dataset original imutável (rastreado via DVC)
│   ├── interim/      # Dados intermediários
│   └── processed/    # Dataset limpo em .parquet (rastreado via DVC)
├── models/           # Binário do modelo campeão (.pkl)
├── notebooks/        # EDA e notebook cliente de demonstração da API
├── reports/          # Métricas, manifesto do modelo, benchmark e gráficos
├── src/churn_ml/     # Código modular de dados, modelagem e serviço
├── tests/            # Testes automatizados (pytest)
└── pyproject.toml    # Gerenciamento de dependências (Poetry)
```

## Como Executar

### 1. Instalação das dependências
```bash
poetry install --with dev
```

### 2. Módulo 1 — Pipeline de Dados
```bash
poetry run python -m churn_ml.data.pipeline
```

### 3. Módulo 2 — Pipeline de Modelos
```bash
poetry run python -m churn_ml.model.pipeline
```

### 4. Módulo 3 — Serviço (API REST)
```bash
poetry run uvicorn churn_ml.service.api:app --reload --port 8000
```
Acesse a documentação interativa em `http://127.0.0.1:8000/docs`.

### 5. Testes Automatizados
```bash
poetry run pytest -v
```
