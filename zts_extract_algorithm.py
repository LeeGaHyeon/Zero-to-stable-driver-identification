import os
import pandas as pd
import numpy as np

name_lt = ['leeseunglee', 'choimingi']

# name_lt = ['huhongjune', 'jeongyubin', 'jojeongdeok', 'leegahyeon', 'leegihun', 'leejaeho', 'leekanghyuk', 'leeyunguel', 'simboseok']
course  = ['A', 'B', 'C']

def zts_transform(data_df):
    start = 0
    end = 0
    μ = 10
    result = []

    for i in range(1, len(data_df)):
        T = data_df.iloc[i]['seconds_elapsed']
        O = data_df.iloc[i]['yaw']
        S = data_df.iloc[i]['speed']
        A = data_df.iloc[i]['totalacc']

        if S == 0:
            start = i
            end = i
        if S > 0 and abs(S - data_df.iloc[i-1]['speed']) == 0 and A == 0:
        # if S > 0:
            end = i
            if T - data_df.iloc[start]['seconds_elapsed'] > μ and start < end:
                t = data_df.iloc[end]['seconds_elapsed'] - data_df.iloc[start]['seconds_elapsed']
                o = np.var(data_df.iloc[start:end+1]['yaw'])
                s = data_df.iloc[end]['speed']
                α = np.sum(data_df.iloc[start:end+1]['totalacc'])
                result.append((t, o, s, α))
    return pd.DataFrame(result, columns=['t', 'o', 's', 'α'])

for name in name_lt:
    for c in course:
        for i in range(1, 5):
            path = f'./data/{name}/{c}/{i}/'  # Adjust as per your directory structure

            # Location.csv path
            location_file_path = os.path.join(path, 'zts_input.csv')
            print(location_file_path)

            if os.path.exists(location_file_path):
                data_df = pd.read_csv(location_file_path)
                transformed_df = zts_transform(data_df)
                transformed_df.to_csv(os.path.join(path, 'zts_output.csv'), index=False)  # Saving transformed data
                print(transformed_df)
