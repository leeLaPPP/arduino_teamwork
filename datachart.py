import pandas as pd
import matplotlib.pyplot as plt
import time as t 

csv_file = 'data.csv'

try:
    # CSV 파일 읽기 (탭 구분자 사용)
    # '시간' 컬럼을 datetime 형식으로 파싱
    df = pd.read_csv(csv_file, sep='\t', parse_dates=['시간'])

    print("데이터 로드 성공:")
    print(df.head())

    # 데이터 시각화
    plt.figure(figsize=(12, 8))

    # 온도 그래프
    plt.subplot(3, 1, 1) # 3행 1열 중 첫 번째 그래프
    plt.plot(df['시간'], df['온도'], label='온도 (°C)', color='red')
    plt.ylabel('온도 (°C)')
    plt.title('시간별 센서 데이터')
    plt.grid(True)
    plt.legend()

    # 습도 그래프
    plt.subplot(3, 1, 2) # 3행 1열 중 두 번째 그래프
    plt.plot(df['시간'], df['습도'], label='습도 (%)', color='blue')
    plt.ylabel('습도 (%)')
    plt.grid(True)
    plt.legend()

    # 공기질 그래프
    plt.subplot(3, 1, 3) # 3행 1열 중 세 번째 그래프
    plt.plot(df['시간'], df['공기질'], label='공기질 (ppm)', color='green')
    plt.ylabel('공기질 (ppm)')
    plt.xlabel('시간')
    plt.grid(True)
    plt.legend()

    # 그래프 레이아웃 조정
    plt.tight_layout()

    # 그래프 표시
    plt.show()

except FileNotFoundError:
    print(f"오류: 파일 '{csv_file}'을 찾을 수 없습니다. Aduino_CSV_Data.py를 실행하여 데이터를 먼저 생성해주세요.")
except Exception as e:
    print(f"데이터 시각화 중 오류 발생: {e}") 