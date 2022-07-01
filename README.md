# kNN-example
k 최근접이웃(kNN : k Nearest Neighbor) 알고리즘 구현 예시

### 알고리즘 구현 내용
1. 거리계산 : 기준데이터와 적용데이터 간의 유클리드 거리계산식
2. k 최근접 이웃 선정 : 최근접이웃 1, 3, 5개 선정
3. 최근접이웃 선정 결과 출력

#### 출력내용 예시
```
k1 -> [0.18133] -> 최근접이웃 1개 거리(distance)
real data : [0.91311, 0.12316] -> 적용데이터 중에서 선정된 데이터
k3 -> [0.18133, 0.18540, 0.24802] ] -> 최근접이웃 3개 거리(distance)
real data : [0.91311, 0.12316] [0.75420, 0.45281] [0.62317, 0.18049]
k5 -> [0.18133, 0.18540, 0.24802, 0.45897, 0.59520] -> 최근접이웃 5개 거리(distance)
real data : [0.91311, 0.12316] [0.75420, 0.45281] [0.62317, 0.18049] [0.8892, 0.7480] [0.24990, 0.28701]
```
