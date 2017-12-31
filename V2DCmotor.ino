#include <AFMotor.h>  // Kütüphane dosyamızı yükledik
AF_DCMotor motorcan(1);
AF_DCMotor motoryon(2); // M2 çıkış pinini kullandık ve ismini motoryon koyduk.Parantez içerisindeki 2 M2 yi temsil etmektedir.
int x[] = {1,1,1,1,1,2,1,2,1,1,1,1,1,3,1,3,1,1,1,1,1,2,1,2,1,1,1,1,1};
// taş zeminde 200 süratle her 1de 20 cm gidiyor  
int a=0;
void setup() {
motorcan.setSpeed(200);
motoryon.setSpeed(200); // Motorumuzun hızını ayarladık

motorcan.run(RELEASE);
motoryon.run(RELEASE);
}

void loop() {
a=a+1;
if (a>=sizeof( x[0] ))
{
  motorcan.run(RELEASE);
  motoryon.run(RELEASE);
}

if (x[a]==1)
{
  motorcan.run(FORWARD);
  motoryon.run(FORWARD);
  delay(1000);
}

if (x[a]==2) // sağa dön
{
  motorcan.run(FORWARD);
  motoryon.run(BACKWARD);  
  delay(650); // 90 derecelik dönüş
}

if (x[a]==3) //sola dön
{
  motorcan.run(BACKWARD);
  motoryon.run(FORWARD); 
  delay(700); //90 derecelik dönüş 
}
}
