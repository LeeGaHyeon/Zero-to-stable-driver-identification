# import pandas as pd
#
# # 데이터 파일 불러오기
# location_df = pd.read_csv('C:/Users/user/PycharmProjects/paper-implementation-2/data/leegahyeon/C/4/Location.csv')
# totalacc_df = pd.read_csv('C:/Users/user/PycharmProjects/paper-implementation-2/data/leegahyeon/C/4/TotalAcceleration.csv')
# data_df = pd.read_csv('C:/Users/user/PycharmProjects/paper-implementation-2/data/leegahyeon/C/4/Orientation.csv')
#
# # location_df의 time에서 소수점 아래를 버리고 정수로 변환
# location_df['int_time'] = location_df['seconds_elapsed'].astype(int)
# # location_df의 time에서 소수점 아래를 버리고 정수로 변환
# totalacc_df['int_time'] = location_df['seconds_elapsed'].astype(int)
# # data_df의 time에서 소수점 아래를 버리고 정수로 변환
# data_df['int_time'] = data_df['seconds_elapsed'].astype(int)
#
# # data_df의 int_time 값에 따라 location_df에서 speed 값을 찾아서 새로운 speed 열을 data_df에 추가
# data_df['speed'] = data_df['int_time'].map(location_df['speed'])
# # data_df의 int_time 값에 따라 location_df에서 totalacc 값을 찾아서 새로운 speed 열을 data_df에 추가
# data_df['totalacc'] = data_df['int_time'].map(totalacc_df['x'])
#
# # int_time 열은 더 이상 필요하지 않으므로 삭제
# data_df.drop('int_time', axis=1, inplace=True)
# print(data_df)
#
# data_df.to_csv('C:/Users/user/PycharmProjects/paper-implementation-2/data/leegahyeon/C/4/zts_input.csv')
import os
import pandas as pd

name_list = ['leeseunglee']
# name_list = ['choimingi']
# name_list = ['huhongjune', 'jeongyubin', 'jojeongdeok', 'leegahyeon', 'leegihun', 'leejaeho', 'leekanghyuk', 'leeyunguel', 'simboseok']
course_list = ['A', 'B', 'C']
num_files = 4

for name in name_list:
    for course in course_list:
        for i in range(1, num_files + 1):
            # Generate file paths
            location_file_path = f'C:/Users/user/PycharmProjects/paper-implementation-2/data/{name}/{course}/{i}/Location.csv'
            totalacc_file_path = f'C:/Users/user/PycharmProjects/paper-implementation-2/data/{name}/{course}/{i}/TotalAcceleration.csv'
            data_file_path = f'C:/Users/user/PycharmProjects/paper-implementation-2/data/{name}/{course}/{i}/Orientation.csv'
            output_file_path = f'C:/Users/user/PycharmProjects/paper-implementation-2/data/{name}/{course}/{i}/zts_input.csv'
            # C:\Users\user\PycharmProjects\paper-implementation-2\data\leeseunglee\Ａ\1

            # Load data frames
            location_df = pd.read_csv(location_file_path)
            totalacc_df = pd.read_csv(totalacc_file_path)
            data_df = pd.read_csv(data_file_path)

            location_df['int_time'] = location_df['seconds_elapsed'].astype(int)
            totalacc_df['int_time'] = location_df['seconds_elapsed'].astype(int)
            data_df['int_time'] = data_df['seconds_elapsed'].astype(int)
            data_df['speed'] = data_df['int_time'].map(location_df['speed'])
            data_df['totalacc'] = data_df['int_time'].map(totalacc_df['x'])
            data_df.drop('int_time', axis=1, inplace=True)


            # # Round time values in data_df to integers
            # data_df['int_time'] = data_df['seconds_elapsed'].astype(int)
            #
            # # Map 'speed' and 'totalacc' values from other data frames
            # data_df['speed'] = data_df['int_time'].map(location_df.set_index('int_time')['speed'])
            # data_df['totalacc'] = data_df['int_time'].map(totalacc_df.set_index('int_time')['x'])
            #
            # # Drop 'int_time' column
            # data_df.drop('int_time', axis=1, inplace=True)

            # Save the updated data frame to the output file
            data_df.to_csv(output_file_path)
            print(f'Saved: {output_file_path}')

