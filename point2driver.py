# import pandas as pd
# # 허홍준 1
# # 정유빈 2
# # 이가현 3
# # 이기훈 4
# # 이재호 5
# # 이강혁 6
# # 조정덕 7
# # 이윤걸 8
# # 심보석 9
# # CSV 파일 경로 설정
# # csv_file_path = "C:/Users/user/PycharmProjects/paper-implementation-2/driver2.csv"  # 파일 경로를 실제 파일 경로로 바꿔주세요.
# csv_file_path = "C:/Users/user/PycharmProjects/paper-implementation-2/data/simboseok/A/1/zts_output.csv"
#
# # CSV 파일을 읽어옵니다.
# data = pd.read_csv(csv_file_path)
#
# # 'label' 열의 모든 값을 1로 설정합니다.
# data['label'] = 9
#
# # 변경된 데이터프레임을 CSV 파일로 저장할 수도 있습니다.
# data.to_csv("C:/Users/user/PycharmProjects/paper-implementation-2/zts/driver9_A_1.csv", index=False)  # index=False는 인덱스를 저장하지 않도록 하는 옵션
#
# # 'label' 열이 모두 1로 업데이트된 데이터프레임을 출력합니다.
# print(data)

import os
import pandas as pd

name_map = {
    'leeseunglee': 0,
    'huhongjune': 1,
    'jeongyubin': 2,
    'jojeongdeok': 3,
    'leegahyeon': 4,
    'leegihun': 5,
    'leejaeho': 6,
    'leekanghyuk': 7,
    'leeyunguel': 8,
    'simboseok': 9,
    'choimingi': 10
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

base_data_path = "C:/Users/user/PycharmProjects/paper-implementation-2/data"

for name, label in name_map.items():
    for course, course_label in course_map.items():
        for round, round_label in round_map.items():
            csv_file_path = f"{base_data_path}/{name}/{course}/{round}/zts_point.csv"

            if os.path.exists(csv_file_path):
                # CSV 파일을 읽어옵니다.
                data = pd.read_csv(csv_file_path)

                # 'label', 'course', and 'round' 열을 추가하고 값을 설정합니다.
                data['label'] = label
                data['course'] = course_label
                data['round'] = round_label

                # 변경된 데이터프레임을 CSV 파일로 저장할 수도 있습니다.
                output_file_path = f"C:/Users/user/PycharmProjects/paper-implementation-2/11_point/driver{label}_{course_label}_{round_label}.csv"
                data.to_csv(output_file_path, index=False)  # index=False는 인덱스를 저장하지 않도록 하는 옵션

                print(f'Saved: {output_file_path}')

