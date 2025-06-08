import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib         # 멧플롯립에 한글 사용가능

csv_file = 'data.csv'

try:
    df = pd.read_csv(csv_file, sep='\t', parse_dates=['시간'], encoding='cp949')

    print("데이터 로드 성공:")
    print(df.head())

    plt.figure(figsize=(12, 8))
    plt.suptitle('시간별 센서 데이터', fontsize=16)
    # 온도 그래프
    plt.subplot(3, 1, 1)
    plt.plot(df['시간'], df['온도'], label='온도 (°C)', color='red')
    plt.title('온도 (°C)')
    plt.grid(True)
    plt.legend()

    # 습도 그래프
    plt.subplot(3, 1, 2)
    plt.plot(df['시간'], df['습도'], label='습도 (%)', color='blue')
    plt.title('습도 (%)')
    plt.grid(True)
    plt.legend()

    # 공기질 그래프
    plt.subplot(3, 1, 3)
    plt.plot(df['시간'], df['공기질'], label='공기질 (ppm)', color='green')
    plt.title('공기질 (ppm)')
    plt.xlabel('시간')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()

    # 그래프 표시
    plt.show()

except FileNotFoundError:
    print(f"오류: 파일 '{csv_file}'을 찾을 수 없습니다. Aduino_CSV_Data.py를 실행하여 데이터를 먼저 생성해주세요.")
except Exception as e:
    print(f"데이터 시각화 중 오류 발생: {e}") 