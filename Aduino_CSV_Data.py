import serial
import csv
import time
from datetime import datetime

PORT = 'COM3'       # 장치관리자에서 자신의 시리얼포트번호 확인
BAUD_RATE = 9600
INTERVAL =  1 

csv_file = 'data.csv'

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerow(['시간', '온도', '습도', '공기질'])


try:
    ser = serial.Serial(PORT, BAUD_RATE)
    time.sleep(3) 
    print(f"시리얼 포트 {PORT}에 연결되었습니다.")

    while ser.in_waiting:
         line = ser.readline().decode('utf-8').strip()
         print(f"초기 메시지 건너뛰기: {line}")

except serial.SerialException as e:
    print(f"시리얼 포트 연결 실패: {e}")
    exit(1)


print("데이터 수신 및 저장을 시작합니다. Ctrl + c를 누르면 멈춥니다.\n")

try:
    while True:
        try:
            # 데이터 라인이 수신될 때까지 대기
            if ser.in_waiting:
                line = ser.readline().decode('utf-8').strip()
                if '\t' in line:
                    data = line.split('\t')
                    if len(data) == 3:
                        try:
                            temp = float(data[0])   # 온도
                            hum = float(data[1])    # 습도 
                            ppm = int(data[2])    # 공기질 

                            # 시, 분, 초로 타임 스탬프 측정
                            timestamp = datetime.now().strftime('%H:%M:%S')
                            
                            #csv파일에 데이터 저장 ansi타입으로 저장되어 차트에서 인코딩할때 cp949
                            with open(csv_file, 'a', newline='') as file:   
                                writer = csv.writer(file, delimiter='\t') 
                                writer.writerow([timestamp, temp, hum, ppm])
                            #console에 출력되는 데이터( csv에 저장되는 실제 데이터 )
                            print(f"[{timestamp}] 저장됨: 온도={temp}°C, 습도={hum}%, 공기질={ppm}ppm") 

                        except ValueError:
                            pass 

                    else:
                        pass 
        except serial.SerialException as e:
            print(f"시리얼 통신 오류: {e}")
            break
        time.sleep(0.01)

except KeyboardInterrupt:
    print("\n측정을 중지하고 저장했습니다.")
finally:
    if 'ser' in locals() and ser.isOpen():
        ser.close()
        print("시리얼 포트가 닫혔습니다.")
