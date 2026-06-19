import numpy as np
from numpy.typing import NDArray
from typing import List


class Solution:
    def forward(self, x: NDArray[np.float64], weights: List[NDArray[np.float64]], biases: List[NDArray[np.float64]]) -> NDArray[np.float64]:
        # x: 1D input array
        # weights: list of 2D weight matrices
        # biases: list of 1D bias vectors
        # Apply ReLU after each hidden layer, no activation on output layer
        # return np.round(your_answer, 5)
        for i in range(len(weights)):
            weights_temp = weights[i]
            biases_temp = biases[i]
            if i == 0:
                zi_temp = np.dot(x, weights_temp) + biases_temp
            else:
                zi_temp = np.dot(a1_temp, weights_temp) + biases_temp
            if i != len(weights):
                a1_temp = np.maximum(0.0, zi_temp)
            else:
                a1_temp = zi_temp
        return np.round(a1_temp, 5)
            
             
