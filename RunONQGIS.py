from qgis.core import QgsProject, QgsVectorLayer

# QGIS 프로젝트 로드
project = QgsProject.instance()
project.read('/path/to/project.qgz')

# 예측 결과를 기반으로 레이어 추가 및 애니메이션 설정
for region, results in regression_results.items():
    for area, coeffs in results.items():
        # 이 부분에서 각 지역별로 시간에 따른 변화를 레이어로 추가하고 애니메이션화 할 수 있습니다.
        print(f"{area} 지역의 예측 회귀선: {coeffs['intercept']} + {coeffs['slope']}*년도")
