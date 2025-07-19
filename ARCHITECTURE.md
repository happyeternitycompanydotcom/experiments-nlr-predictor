# 🏗️ NLR-Predictor Architecture

## Overview

The system aims to predict the potential success (revenue) of IT business ideas using nonlinear modeling and large language models (LLMs).

## Components

### 1. `llm/idea_transformer.py`
- Connects to local Ollama LLM (e.g., Mistral) to generate or reformulate business ideas.

### 2. `models/nonlinear_predictor.py`
- Neural network with:
  - Nonlinear encoder (tanh)
  - LSTM time dynamics
  - Final regression decoder

### 3. `notebooks/nlr_predictor_colab.ipynb`
- Jupyter/Colab notebook pipeline:
  - Idea → Embedding → Prediction → Phase visualization

### 4. `visualization/phase_portrait.py`
- Generates 3D phase space trajectories based on model output (artistic attractors).

## Flow

```
[LLM] --> "Idea"
          |
          v
[Sentence Transformer] --> Vector
                           |
                           v
                    [Nonlinear Model]
                           |
                           v
                [Profit Metric Prediction]
                           |
                           v
                   [Phase Portrait Visual]
```

## Future Improvements

- Real-world RAG pipelines
- Multi-agent market simulation
- Dataset from historical startup failures/successes
