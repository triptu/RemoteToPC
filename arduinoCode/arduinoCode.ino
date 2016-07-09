/* Lets get started:
 
 The IR sensor's pins are attached to Arduino as so:
 Pin 1 to Vout (pin 11 on Arduino)
 Pin 2 to GND
 Pin 3 to Vcc (+5v from Arduino)

*/

/*******************CODE BEGINS HERE********************/

#include <IRremote.h>

int IRpin = 11;
IRrecv irrecv(IRpin);
decode_results results;

int value, lastValue;
long lastDebounceTime=0;
long debounceDelay = 300;

void setup()
{
  Serial.begin(9600);
  irrecv.enableIRIn(); // Start the receiver
}

void loop() 
{
  if (irrecv.decode(&results)) // Sending the address of result as argument
    {
      value=results.value;
      if ((millis()-lastDebounceTime)>debounceDelay) {
        Serial.println(results.value, DEC); // Print the Serial 'results.value'
      }
      if(value!=lastValue){
        lastDebounceTime=millis();
      }
      lastValue=value;
      irrecv.resume();   // Receive the next value
    }
}
