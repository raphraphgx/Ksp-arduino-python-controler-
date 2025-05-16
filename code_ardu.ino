void setup() {
  Serial.begin(9600); // Démarrer la communication avec l'ordinateur
}

void loop() {
  int potValue = analogRead(A0); // Lire la position du potentiomètre
  float normalizedValue = potValue / 1023.0; // Transformer la valeur pour qu'elle soit entre 0 et 1
  Serial.println(normalizedValue); // Envoyer la valeur à l'ordinateur
  delay(100); // Répéter toutes les 100 ms
}
