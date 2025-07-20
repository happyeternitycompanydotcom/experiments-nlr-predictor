# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

NLR-Predictor is an experimental nonlinear forecasting framework that predicts business idea profitability using LLMs and dynamical systems. It combines sentence transformers, LSTM neural networks, and phase space visualization.

## Architecture

The system follows this data flow:
1. **LLM Integration** (`llm/idea_transformer.py`) - Local Ollama (Mistral) for idea generation
2. **Text Embedding** - SentenceTransformer ('all-MiniLM-L6-v2') for vectorization
3. **Nonlinear Model** (`models/nonlinear_predictor.py`) - AutoEncoder + LSTM → profit prediction
4. **Visualization** (`visualization/phase_portrait.py`) - 3D phase space attractors

## Key Files

- `models/nonlinear_predictor.py:4-19` - Neural network with encoder (tanh), LSTM, decoder
- `llm/idea_transformer.py:5-21` - Local LLM integration via subprocess + Ollama
- `visualization/phase_portrait.py:6-16` - 3D phase portrait generation
- `notebooks/nlr_predictor_colab.ipynb` - Complete demo pipeline

## Commands

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/test_model.py

# Launch notebook
jupyter notebook notebooks/nlr_predictor_colab.ipynb

# Run specific test
python -m pytest tests/test_model.py::test_model_output_shape -v
```

### Dependencies
- torch
- sentence-transformers
- matplotlib
- pytest (for testing)

## Usage Patterns

1. **Model Input**: 768-dim sentence embeddings from SentenceTransformer
2. **Model Output**: Single scalar profit prediction
3. **Visualization**: 3D attractor based on predicted profit value
4. **LLM**: Requires local Ollama installation with Mistral model

## Testing

Basic test coverage in `tests/test_model.py` with shape validation for model outputs.