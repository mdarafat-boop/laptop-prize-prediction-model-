import pickle
with open("model.pkl", "rb") as file:
    model = pickle.load(file)
# Demo input
features = [[8, 512, 2.4]]
prediction = model.predict(features)

print("Predicted Laptop Price:", prediction[0])