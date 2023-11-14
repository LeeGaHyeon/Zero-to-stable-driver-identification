# Zero-to-stable-driver-identification
## Smartphone sensor data 기반 비교실험 구현 
## Rahim, Mussadiq Abdul, et al. "Zero-to-stable driver identification: A non-intrusive and scalable driver identification scheme." IEEE transactions on vehicular technology 69.1 (2019): 163-171.
[2020 TVT] Zero-to-Stable Driver Identification_ A Non-Intrusive and Scalable Driver Identification Scheme
** GPS 데이터에서 피쳐로써, timestamp, origentation, speed, acceleration 4개 피쳐를 사용
* zts 피쳐를 추출 (속도0에서 정속주행(가속도가 0)일때까지의 데이터만을 추출함. 자세한 부분은 해당 논문을 통해 확인)
* zts 피쳐를 machine learning 알고리즘에 적용하여 운전자 식별 수행 (Random forest, knn, svm)
### 실험결과: https://docs.google.com/spreadsheets/d/1wCc0gsfeFkKPOzhDx_54-1VQd9EBFUNFCVxIKFvzKmo/edit?usp=sharing
