# tests/test_model.py

import torch
from models.nonlinear_predictor import NonlinearRevenuePredictor

def test_model_output_shape():
    model = NonlinearRevenuePredictor()
    input_tensor = torch.randn(1, 1, 768)
    output = model(input_tensor)
    assert output.shape == (1, 1)
