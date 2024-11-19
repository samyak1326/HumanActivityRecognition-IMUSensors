import matplotlib.pyplot as plt
import pandas as pd
import os

# Define the directory containing the CSV files
folder_path = '/Users/samyak/SynologyDrive/George Mason University/Fall_2024/CS655/Final Project/human-activity-recognition/stream-files/Files/stairs-down/stream-stairs-down-3-2024-10-16_14-58-20'

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)

        # Load the data from each CSV file
        data = pd.read_csv(file_path)

        # Check if required columns are present for barometer readings
        if {'seconds_elapsed', 'relativeAltitude'}.issubset(data.columns):
            # Plot the barometer data
            plt.figure(figsize=(10, 6))

            # Plot relative altitude against seconds_elapsed
            plt.plot(data['seconds_elapsed'], data['relativeAltitude'], label='Relative Altitude', alpha=0.7, color='blue')

            # Adding labels and title
            plt.xlabel('Seconds Elapsed', fontsize=12)
            plt.ylabel('Relative Altitude (meters)', fontsize=12)
            plt.title(f'Time-Series Graph of Barometer Data - {filename}', fontsize=14)
            plt.legend()

            # Adding grid lines for clarity
            plt.grid(True, linestyle='--', alpha=0.5)

            # Show the plot
            plt.show()

            # Optional: Save the plot as an image file (uncomment to enable)
            # plt.savefig(f"barometer_plot_{filename}.png")
        else:
            print(f"Skipping file {filename}: Required columns not found.")
