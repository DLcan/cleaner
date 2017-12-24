
#include <AccelStepper.h>
#include <EEPROM.h>

#define FULLSTEP 4
#define HALFSTEP 8

// motor pins
#define motorPin1  2     
#define motorPin2  3     
#define motorPin3  4     
#define motorPin4  5     
                     
                        
#define motorPin5  10     
#define motorPin6  11   
#define motorPin7  12    
#define motorPin8  13    

const int button1Pin = 8;  
                     

// NOTE: The sequence 1-3-2-4 is required for proper sequencing of 28BYJ48
AccelStepper stepper1(HALFSTEP, motorPin1, motorPin3, motorPin2, motorPin4);
AccelStepper stepper2(HALFSTEP, motorPin5, motorPin7, motorPin6, motorPin8);

int V2number;

void setup()   
{
  //stepper1.setMaxSpeed(1000.0);
  //stepper1.setAcceleration(400.0);
  stepper1.setSpeed(6);
  stepper1.moveTo(1024);  // 1 revolution 
  
    //sağ motor
  //stepper2.setMaxSpeed(1000.0);
  //stepper2.setAcceleration(400.0);
  stepper2.setSpeed(6);
  stepper2.moveTo(1024);  // 1 revolution 



Serial.begin(9600);
}


void loop()  
{

  delay(1000); 
  V2number = 0;
  
  if (Serial.available() > 0) 
  {
    V2number = Serial.read();
    Serial.print(V2number);
  }  
  if(V2number == 1)
    //düz gidiyor
  {

  stepper1.moveTo(1500);
  stepper2.moveTo(1500);
  }
  
  if(V2number == 2)
    //sola dönüyor
  {

  stepper1.moveTo(-500);
  stepper2.moveTo(500);
  }
  
  if(V2number == 3)
    //sağa dönüyor
  {

  stepper1.moveTo(500);
  stepper2.moveTo(-500);
  }  
    
  
  if(V2number == 4)
    //geri dönüyor (sağdan)
  {

  stepper1.moveTo(1000);
  stepper2.moveTo(-1000);
  }     
   stepper1.run();
   stepper2.run();
}
