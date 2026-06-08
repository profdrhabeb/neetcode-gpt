class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        current_obj_val = init * init
        current_derivative = 2 * init
        current_x = init
        for _ in range(iterations):
            current_x = current_x - learning_rate * current_derivative
            current_obj_val = current_x * current_x
            current_derivative = 2 * current_x

        return round(current_x, 5)
