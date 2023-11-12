import pandas as pd
import os

def point(df):
    # point 컬럼을 초기화
    df['point'] = 0

    # 경과시간을 첫 번째 행의 시간으로 초기화
    prev_time = df.at[0, 't']

    # point 컬럼을 계산
    for index, row in df.iterrows():
        current_time = row['t']

        # 첫 번째 행인 경우 이전 행을 참조하지 않도록 처리
        if index == 0:
            df.at[index, 'point'] = 0
        else:
            # 현재 행과 이전 행의 시간 차이 계산 (단위: 초)
            time_diff = current_time - prev_time

            # 시간 차이가 2초 이상이면 point 값을 갱신 (2초로 수정)
            if time_diff >= 2:
                df.at[index, 'point'] = df.at[index - 1, 'point'] + 1
                prev_time = current_time
            else:
                df.at[index, 'point'] = df.at[index - 1, 'point']

    return df

name_lt = ['leeseunglee','choimingi']
course  = ['A','B','C']
for name in name_lt:
    for c in course:
        for i in range(1, 5):
            path = f'./data/{name}/{c}/{i}/'  # Adjust as per your directory structure

            # Location.csv path
            location_file_path = os.path.join(path, 'zts_output.csv')
            print(location_file_path)

            if os.path.exists(location_file_path):
                data_df = pd.read_csv(location_file_path)

                # 데이터 프레임이 비어 있지 않은 경우에만 point 함수 호출
                if not data_df.empty:
                    transformed_df = point(data_df)
                    transformed_df.to_csv(os.path.join(path, 'zts_point.csv'), index=False)  # Saving transformed data
                    print(transformed_df)
                else:
                    print("Data frame is empty.")
