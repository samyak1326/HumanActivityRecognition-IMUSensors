import matplotlib.pyplot as plt
import pandas as pd
import os

# Define the directory containing the CSV files
folder_path = '/Users/samyak/SynologyDrive/George Mason University/Fall_2024/CS655/Final Project/human-activity-recognition/stream-files/Files/walking/stream-walking-10-2024-10-14_23-44-22'

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)

        # Load the data from each CSV file
        data = pd.read_csv(file_path)

        # Check if required columns are present
        if {'seconds_elapsed', 'x', 'y', 'z'}.issubset(data.columns):
            # Plot the accelerometer data
            plt.figure(figsize=(10, 6))

            # Plot x, y, z coordinates against seconds_elapsed
            plt.plot(data['seconds_elapsed'], data['x'], label='X', alpha=0.7)
            plt.plot(data['seconds_elapsed'], data['y'], label='Y', alpha=0.7)
            plt.plot(data['seconds_elapsed'], data['z'], label='Z', alpha=0.7)

            # Adding labels and title
            plt.xlabel('Seconds Elapsed')
            plt.ylabel('Readings')
            plt.title(f'Time-Series Graph of Walking Data - {filename}')
            plt.legend()

            # Grid and show plot
            plt.grid(True)
            plt.show()
        else:
            print(f"Skipping file {filename}: Required columns not found.")
