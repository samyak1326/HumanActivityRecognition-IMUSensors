# Human Activity Recognition using IMU Sensors

This project implements a machine learning model to recognize human activities using smartphone IMU sensor data. The model can classify various physical activities such as walking, running, sitting, and climbing stairs based on accelerometer data.

### Project completed as part of CS 655: Wireless and Mobile Computing (Fall 2024) at George Mason University.
 

## Overview

The project analyzes IMU sensor data collected from smartphone sensors to classify different human activities. Using features extracted from accelerometer readings, the model can distinguish between activities like:

- Walking
- Running
- Sitting
- Standing 
- Going up/down stairs
- Taking elevator
- Lifting weights
- Waving
- Body rotating
- And more

## Model Performance

The Random Forest classifier achieves 90.81% accuracy on the test set. The model performs particularly well at distinguishing between basic activities like walking, sitting and standing.

## Files

- `features.ipynb`: Jupyter notebook containing the data preprocessing, feature extraction, and model training code
- `trained_model.joblib`: Saved Random Forest model file
- Raw sensor data files (not included in repo)

## Usage

The trained model can be loaded and used for predictions:

```python
from joblib import load
model = load('trained_model.joblib')
# Make predictions on new data
predictions = model.predict(X_new)
```

### Requirements

- Python 3.x
- scikit-learn
- numpy
- pandas
- matplotlib
- seaborn

### Authors

- Karan Monga 
- Samyak Jain