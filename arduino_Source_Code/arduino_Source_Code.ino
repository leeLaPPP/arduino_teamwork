#include <DHT.h>
#include <MQ135.h>

#define DHT11_PIN 7
#define DHT11_TYPE DHT11
#define MQ135_PIN A0

// 각 센서 최소 최댓값 지정 
const float TEMP_MIN = -50.0;
const float TEMP_MAX = 100.0;
const float HUM_MIN = 0.0;
const float HUM_MAX = 100.0;
const int PPM_MIN = 10;
const int PPM_MAX = 10000;

DHT dht(DHT11_PIN, DHT11_TYPE);
MQ135 mq135(MQ135_PIN);

unsigned long nowSec = 0;
unsigned long prevSec = 0;
unsigned int interval_sec = 2;  // 측정 간격 (초)





void setup() {
  Serial.begin(9600);
  dht.begin();
  prevSec = millis() / 1000;

  Serial.println("");

  // header
  Serial.println("시간\t온도\t습도\t공기질");
}

void loop() {
  nowSec = millis() / 1000;

  if (nowSec - prevSec >= interval_sec) {
    // 각 센서 데이터
    float temp = dht.readTemperature();
    float humi = dht.readHumidity();
    int ppm = mq135.getPPM();

    // 데이터 유효성 검사
    if (isnan(temp) || isnan(humi)) {
      Serial.println("ERROR_DHT11");
    }
    else if (temp < TEMP_MIN || temp > TEMP_MAX || 
             humi < HUM_MIN || humi > HUM_MAX) {
      Serial.println("ERROR_RANGE_DHT11");
    }
    else if (ppm < PPM_MIN || ppm > PPM_MAX) {
      Serial.println("ERROR_MQ135");
    }
    else {
      // 시간 온도 습도 공기질 순으로 데이터 추출 
      Serial.print(temp, 1);
      Serial.print("\t");
      Serial.print(humi, 1);
      Serial.print("\t");
      Serial.println(ppm);
    }

    prevSec = nowSec;
  }
}