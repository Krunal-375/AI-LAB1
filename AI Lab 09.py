import numpy as np
from sklearn.linear_model import Perceptron, LogisticRegression

# Sample dataset
X = np.array([
    [0, 0, 1, 0],  # free down
    [1, 0, 1, 0],  # free down
    [0, 1, 1, 0],  # free up
    [1, 1, 1, 1],  # blocked all side
    [0, 0, 0, 1],  # free up and down
    [0, 1, 0, 0],  # free up, right
])
y_binary = np.array([1, 1, 1, 0, 1, 1])  # Move or not
y_multi = np.array([1, 1, 0, -1, 0, 3])  # Direction: Up = 0, Down = 1, Left = 2, Right = 3

# Train models
perceptron = Perceptron()
perceptron.fit(X, y_binary)

X_multi = X[y_multi != -1]
y_multi_filtered = y_multi[y_multi != -1]
multi_model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
multi_model.fit(X_multi, y_multi_filtered)

# --- Take input from user ---
print("Enter sensor readings (0 = free, 1 = obstacle):")
left = int(input("Left: "))
right = int(input("Right: "))
up = int(input("Up: "))
down = int(input("Down: "))

user_input = np.array([[left, right, up, down]])

# --- Prediction ---
move_decision = perceptron.predict(user_input)[0]

if move_decision == 1:
    direction = multi_model.predict(user_input)[0]
    direction_map = {0: "Up", 1: "Down", 2: "Left", 3: "Right"}
    print("Decision: MOVE")
    print("Direction:", direction_map[direction])
else:
    print("Decision: STOP")
