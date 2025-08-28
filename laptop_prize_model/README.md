# Laptop Price Prediction Model (Pickle File) 💻
This repository has a trained machine learning model (`model.pkl`).Developers can create themselves web app, desktop app or script using this model

---

## 🔧 Requirements
- Python 3.10+
- Required library:

  ```bash
  pip install -r requirements.txt
  ```
  If you are already installed then you will run even if not installed
  ---

  # How to Open/Load Pickle File 

```python
import pickle

# Load Pickle file
with open("model.pkl", "rb") as file:
    model = pickle.load(file)
    
# Example Data (Number of Features will be according to your trained model)
features = [[8, 512, 2.4]]   # such as [RAM(GB), Storage(GB), Processor Speed(GHz)]

# Take Prediction
prediction = model.predict(features)
print("Predicted Laptop Price:", prediction[0])