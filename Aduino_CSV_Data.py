import serial
import csv
import time
from datetime import datetime

PORT = 'COM5' 
BAUD_RATE = 9600
INTERVAL = 1  # 1초 간격 측정 (데이터 수신 간격과는 다를 수 있음)

csv_file = 'data.csv'

# CSV 파일 초기화 및 헤더 작성 (탭 구분자로 변경)
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerow(['시간', '온도', '습도', '공기질'])

# 시리얼 포트 열기
try:
    ser = serial.Serial(PORT, BAUD_RATE)
    time.sleep(3)  # 아두이노 리셋 및 준비 대기 시간 증가
    print(f"시리얼 포트 {PORT}에 연결되었습니다.")

    # 아두이노가 PC 시간을 기다릴 수 있으므로 현재 시간을 전송
    current_pc_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ser.write((current_pc_time + '\n').encode())
    print(f"아두이노에 현재 시간 전송: {current_pc_time}")
    time.sleep(1) # 시간 전송 후 아두이노 처리 대기

    # 아두이노의 초기 메시지(헤더 등)를 읽어서 버림
    while ser.in_waiting:
         line = ser.readline().decode('utf-8').strip()
         print(f"초기 메시지 건너뛰기: {line}")


except serial.SerialException as e:
    print(f"시리얼 포트 연결 실패: {e}")
    exit(1)

print("데이터 수신 및 저장을 시작합니다. Ctrl + c를 누르면 멈춥니다.\n")

try:
    # last_logged_time 변수는 더 이상 사용하지 않습니다.

    while True:
        try:
            # 데이터 라인이 수신될 때까지 대기
            if ser.in_waiting:
                line = ser.readline().decode('utf-8').strip()
                # print(f"수신된 라인: {line}")  # 디버깅용 출력 주석 처리

                # 탭으로 구분된 데이터인지 확인
                if '\t' in line:
                    data = line.split('\t')

                    # 데이터가 3개(온도, 습도, 공기질)이고 숫자로 변환 가능한지 확인
                    if len(data) == 3:
                        try:
                            temp = float(data[0])
                            hum = float(data[1])
                            ppm = float(data[2])

                            # 데이터가 유효한 범위인지 간단히 확인 (필요시 수정)
                            # if -50 <= temp <= 100 and 0 <= hum <= 100 and ppm >= 0:

                            timestamp = datetime.now().strftime('%H:%M:%S') # 시간 형식은 이미 수정하셨네요.
                            with open(csv_file, 'a', newline='') as file:
                                writer = csv.writer(file, delimiter='\t') # 여기를 수정하여 탭 구분자로 설정
                                writer.writerow([timestamp, temp, hum, ppm])
                            print(f"[{timestamp}] 저장됨: 온도={temp}°C, 습도={hum}%, 공기질={ppm}ppm")

                            # else:
                            #     print(f"유효하지 않은 데이터 범위: {line}")

                        except ValueError:
                            # 숫자로 변환할 수 없는 경우 (예: 오류 메시지 라인 등)
                            # print(f"데이터 변환 오류, 라인 무시: {line}") # 디버깅 출력 주석 처리
                            pass # 변환 오류 발생 시 라인 무시

                    else:
                        # 탭은 있지만 데이터 개수가 3개가 아닌 경우
                        # print(f"데이터 개수 오류, 라인 무시: {line}") # 디버깅 출력 주석 처리
                        pass # 데이터 개수 오류 시 라인 무시

                # 탭이 없는 라인은 무시 (아두이노의 다른 메시지일 가능성)
                # else:
                #      print(f"탭 없음, 라인 무시: {line}") # 필요시 이 주석을 해제하여 확인

        except serial.SerialException as e:
            print(f"시리얼 통신 오류: {e}")
            break # 시리얼 오류 발생 시 루프 종료

        # 데이터가 없을 때는 잠시 대기하여 CPU 점유율을 낮춤
        time.sleep(0.01)

except KeyboardInterrupt:
    print("\n측정을 중지하고 저장했습니다.")
finally:
    if 'ser' in locals() and ser.isOpen():
        ser.close()
        print("시리얼 포트가 닫혔습니다.")
