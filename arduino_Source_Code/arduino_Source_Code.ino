#include <DHT.h>
#include <MQ135.h>

#define DHT11_PIN 7
#define DHT11_TYPE DHT11
#define MQ135_PIN A0

DHT dht(DHT11_PIN, DHT11_TYPE);
MQ135 mq135(MQ135_PIN);

unsigned long nowSec = 0;
unsigned long prevSec = 0;
unsigned int interval_sec = 2;  // 측정 간격 (초)

String Now;  // PC 시간 저장할 전역변수

void timeUpdate() {
  if (Serial.available()) {
    Now = Serial.readStringUntil('\n');  // PC에서 시간 받아서 변수에 저장
  }
}

void setup() {
  Serial.begin(9600);
  dht.begin();
  prevSec = millis() / 1000;
  Serial.println("시간 데이터 기다리는중 . . . ");
  while (!Serial.available());
  timeUpdate();
  Serial.println("");
  // header
  Serial.print("현재 시간 : ");
  Serial.println(Now);
  Serial.println("온도\t습도\t공기질");
}


void loop() {
  timeUpdate();
  nowSec = millis() / 1000;

  if (nowSec - prevSec >= interval_sec) {
    float temp = dht.readTemperature();
    float humi = dht.readHumidity();
    int ppm = mq135.getPPM();


    // 오류 감지
    if (isnan(temp) || isnan(humi))
   {
      Serial.println("dht11센서 인식 불가");
    }
    // 현재 mq135센서 망가져서 인식 불가.
    /*else if(ppm < 10 || ppm > 10000) 
    {
  Serial.println("mq135센서 인식 불가");
    }*/ 
  else
    {
      Serial.print(temp, 1);   // 소수점 1자리
      Serial.print("\t");
      Serial.print(humi, 1);
      Serial.print("\t");
      Serial.println(ppm);
    }

    prevSec = nowSec;
  }
}