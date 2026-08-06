# 🚀 Projeto Completo de Data Science & MLOps

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions)

Projeto end-to-end (ponta a ponta) desenvolvido em **Python**, demonstrando competências aplicadas em Engenharia de Dados, Ciência de Dados, Machine Learning e Engenharia de Software (MLOps).

---

## 🎯 Competências Demonstradas

- **Engenharia de Dados:** Pipelines de dados, limpeza, tratamento e preparação.
- **Ciência de Dados & Machine Learning:** Análise exploratória, treinamento de modelos e avaliação de métricas.
- **Desenvolvimento Backend:** Criação de API REST com FastAPI para servir predições.
- **Visualização de Dados:** Dashboard interativo em Streamlit para consumo de insights e predições em tempo real.
- **MLOps & CI/CD:** Automação de testes unitários e pipelines de integração contínua via GitHub Actions.

---

## 📁 Estrutura do Repositório

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml             # Pipeline de CI/CD (GitHub Actions)
├── api/
│   └── main.py                # API REST criada em FastAPI
├── data/
│   ├── raw/                   # Dados brutos
│   └── processed/             # Dados limpos e preparados
├── dashboard/
│   └── app.py                 # Interface interativa em Streamlit
├── docs/                      # Documentação técnica adicional
├── models/
│   └── model.pkl              # Modelo serializado (.pkl)
├── notebooks/                 # Notebooks de análise exploratória (EDA)
├── reports/                   # Gráficos e relatórios gerados
├── src/
│   ├── process_data.py        # Pipeline de processamento de dados
│   └── train.py               # Treinamento e avaliação do modelo
├── tests/
│   └── test_api.py            # Testes unitários para API
├── .gitignore                 # Arquivos ignorados pelo Git
├── README.md                  # Documentação principal
└── requirements.txt           # Dependências do projeto


## 🚀 Como Executar o Projeto

Você pode executar o projeto de duas formas: **localmente (via Python)** ou **containerizado (via Docker)**.

---
### Opção 1: Execução Local (Python)

#### 1. Pré-requisitos
Certifique-se de ter o **Python 3.10+** e o **Git** instalados na sua máquina.

#### 2. Clonar o Repositório e Configurar o Ambiente
```bash
# 1. Clone o repositório
git clone [https://github.com/GBRITO-Tec/FRAUD-DETECTION-BANK-AI.git](https://github.com/GBRITO-Tec/FRAUD-DETECTION-BANK-AI.git)
cd FRAUD-DETECTION-BANK-AI.git


### Opção 2: Execução Simplificada via Docker 🐳

Esta opção permite rodar toda a aplicação (API + Dashboard) em containers isolados sem a necessidade de instalar o Python ou dependências na sua máquina local.

---

#### 1. Arquivos de Configuração do Docker

Certifique-se de que os seguintes arquivos estão na raiz do seu repositório:

##### `Dockerfile` (para a API)
```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Copia e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia a estrutura do projeto
COPY api/ ./api/
COPY models/ ./models/
COPY data/ ./data/

# Expõe a porta da API
EXPOSE 8000

# Comando para rodar a API
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
# 2. Crie o ambiente virtual
python -m venv venv

# 3. Ative o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate

# 4. Instale as dependências
pip install -r requirements.txt

# Processar os dados brutos (Engenharia de Dados)
python src/process_data.py

# Treinar e salvar o modelo de Machine Learning
python src/train.py

# 5. Inciar o Dashborad(Streamlit)
uvicorn api.main:app --reload
