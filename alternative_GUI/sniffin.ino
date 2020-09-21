#include "./esppl_functions.h"

void cb(esppl_frame_info *info) {
  Serial.print(" MAC: ");
  for (int i = 0; i < 6; i++) Serial.printf("%02x", info->sourceaddr[i]);
  Serial.print(" DEST: ");
  for (int i = 0; i < 6; i++) Serial.printf("%02x", info->receiveraddr[i]);
  Serial.print(" RSSI: ");
  Serial.print(info->rssi);
  Serial.print(" SEQ: ");
  Serial.print(info->seq_num);
  Serial.print(" CHNL: ");
  Serial.println(info->channel);
 
}

void setup() {
  delay(500);
  Serial.begin(115200);
  esppl_init(cb);
}

void loop() {
  esppl_sniffing_start();
  while (true) {
    for (int i = 1; i < 15; i++ ) {
      esppl_set_channel(i);
      while (esppl_process_frames()) {
        //
      }
    }
    delay(1000);
  }  
}