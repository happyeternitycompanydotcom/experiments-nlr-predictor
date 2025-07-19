import torch
import torch.nn as nn

class NonlinearRevenuePredictor(nn.Module):
    def __init__(self, input_size=768, hidden_size=128):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.Tanh(),
        )
        self.rnn = nn.LSTM(hidden_size, hidden_size, batch_first=True)
        self.decoder = nn.Sequential(
            nn.Linear(hidden_size, 1)
        )

    def forward(self, x_seq):
        x_encoded = self.encoder(x_seq)
        rnn_out, _ = self.rnn(x_encoded)
        return self.decoder(rnn_out[:, -1, :])
