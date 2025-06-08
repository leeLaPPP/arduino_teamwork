# Arduino Team Project - Sensor Data Logger

이 프로젝트는 Arduino로부터 온습도(DHT11)와 공기질(MQ135) 센서 데이터를 받아와서,
Python을 통해 CSV 파일로 저장하고, 이를 그래프로 시각화하는 환경 모니터링 시스템입니다.

---

## 📦 사용된 부품 및 센서
- DHT11 (온도 및 습도 센서)
- MQ135 (공기질 센서)
- Arduino UNO or Mega
- USB 시리얼 통신
- 라즈베리파이 (선택 사항)

---

## 🔧 아두이노 코드 주요 기능
- 온도, 습도, 공기질 센서값 주기적 측정 (2초 간격)
- 데이터 유효성 검증
- 시리얼 포트로 탭 구분 데이터 전송 (`\t`)

```cpp
Serial.print(temp);
Serial.print("\t");
Serial.print(humi);
Serial.print("\t");
Serial.println(ppm);
