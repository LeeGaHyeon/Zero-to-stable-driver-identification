import os
import pandas as pd

name_map = {
    'leeseunglee':0,
    'huhongjune': 1,
    'jeongyubin': 2,
    'jojeongdeok': 3,
    'leegahyeon': 4,
    'leegihun': 5,
    'leejaeho': 6,
    'leekanghyuk': 7,
    'leeyunguel': 8,
    'simboseok': 9,
    'choimingi':10
}

course_map = {
    'A': 1,
    'B': 2,
    'C': 3
}

round_map = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4
}

base_output_path = "C:/Users/user/PycharmProjects/paper-implementation-2/11_point"

# Create an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

for name, label in name_map.items():
    for course, course_label in course_map.items():
        for round, round_label in round_map.items():
            csv_file_path = f"{base_output_path}/driver{label}_{course_label}_{round_label}.csv"

            if os.path.exists(csv_file_path):
                # Read each CSV file
                data = pd.read_csv(csv_file_path)

                # Concatenate the data to the combined_data DataFrame
                combined_data = pd.concat([combined_data, data], ignore_index=True)

# Save the combined data to 'data.csv'
combined_data.to_csv(f"{base_output_path}/data.csv", index=False)

print("Combined data saved as 'data.csv'")
