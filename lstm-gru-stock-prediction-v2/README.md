# LSTM & GRU Stock Price Prediction

Projeto de previsão de preços de ações utilizando redes neurais recorrentes (LSTM e GRU) com dados do Yahoo Finance.

##  Objetivo

Comparar o desempenho de modelos LSTM e GRU na previsão de séries temporais financeiras.

##  Modelos utilizados

- LSTM
- GRU

##  Dataset

Dados históricos via Yahoo Finance (yfinance).

##  Pipeline

1. Coleta de dados
2. Normalização
3. Criação de janelas
4. Treinamento
5. Avaliação

##  Execução

```bash
pip install -r requirements.txt
python src/train.py
```
