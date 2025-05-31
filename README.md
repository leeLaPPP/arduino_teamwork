# Arduino Sensor Data Logger & Visualizer

이 프로젝트는 **아두이노를 활용해 온도, 습도, 공기질 데이터를 측정**하고,  
**Python으로 데이터를 CSV 파일로 로깅 및 시각화**하는 시스템입니다.

---

## 📝 프로젝트 개요

✅ 아두이노 센서:  
- DHT11 (온습도 센서)  
- MQ135 (공기질 센서)  

✅ 데이터 흐름:  
1️⃣ 아두이노에서 센서 데이터를 시리얼로 전송  
2️⃣ Python이 데이터를 받아서 CSV로 저장  
3️⃣ matplotlib로 데이터 시각화  

---

## 📁 폴더 구조
arduino_teamwork/
├── .vscode/ # VSCode 설정 폴더

├── arduino_Source_Code/ # 아두이노 스케치 코드

├── Aduiono_CSV_Data.py # 시리얼 데이터 수집 및 CSV 저장 파이썬 코드

├── data.csv # 센서 데이터 저장 CSV

└── datachart.py # 시각화 파이썬 코드


---

## ⚙️ 주요 기능

✅ 아두이노가 측정한 데이터를 시리얼로 전송  
✅ Python이 데이터를 수신해서 **시간, 온도, 습도, 공기질**로 구분 저장  
✅ CSV 파일은 탭(\t)으로 구분  
✅ **불필요한 초기 메시지를 건너뛰고** 필요한 데이터만 CSV에 저장  
✅ matplotlib를 이용한 시각화 지원

---

## 🚀 실행 방법

1️⃣ **아두이노 코드 업로드**  
- `arduino_Source_Code` 폴더의 코드를 아두이노 IDE로 업로드

2️⃣ **Python 데이터 로거 실행**  
```bash
python Aduiono_CSV_Data.py
