import pandas as pd
import numpy as np
import statsmodels.api as sm

# 파일 경로
files = {
    'g_goesan_2008': '/path/to/괴산데이터 2008.csv',
    'g_goesan_2016': '/path/to/괴산데이터 2016.csv',
    'g_hamyang_2008': '/path/to/함양데이터 2008.csv',
    'g_hamyang_2016': '/path/to/함양데이터 2016.csv'
}

# 데이터 로드
data_frames = {name: pd.read_csv(path) for name, path in files.items()}

# 데이터 정리 및 통합
data_frames_clean = {
    'goesan': pd.concat([
        data_frames['g_goesan_2008'].assign(년도=2008),
        data_frames['g_goesan_2016'].assign(년도=2016)
    ]),
    'hamyang': pd.concat([
        data_frames['g_hamyang_2008'].assign(년도=2008),
        data_frames['g_hamyang_2016'].assign(년도=2016)
    ])
}

# 열 이름 정리 및 데이터 형식 조정
for key in data_frames_clean:
    data_frames_clean[key] = data_frames_clean[key][['지역', '위도', '경도', '지수', '년도']]
    data_frames_clean[key]['지수'] = pd.to_numeric(data_frames_clean[key]['지수'], errors='coerce')




# 선형 회귀 결과 저장
regression_results = {}
for region in data_frames_clean:
    regression_results[region] = {}
    for area in data_frames_clean[region]['지역'].unique():
        area_data = data_frames_clean[region][data_frames_clean[region]['지역'] == area]
        X = sm.add_constant(area_data['년도'])  # 상수항 추가
        y = area_data['지수']
        model = sm.OLS(y, X).fit()
        regression_results[region][area] = {
            'intercept': model.params['const'],
            'slope': model.params['년도'],
            'r_squared': model.rsquared
        }

