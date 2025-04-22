void setup() {
  Serial.begin(115200); // Initialise la communication série
}

void loop() {
  int sensorValue = analogRead(A0); // Lit la valeur analogique sur la broche A0
  Serial.println(sensorValue);      // Envoie la valeur via le port série
  delay(100);                       // Attente de 100 ms
}
