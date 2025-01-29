![...](takatoa_head-img_1920-200.jpg)

# qDaT - quantum-oriented Datetime

   qDaT defines a class for date and time information in the form: complex(qDaT-date,qDaT-time) 

### basic information

   On June 7, 1925, Werner Heisenberg went to Helgoland. There he completed the quantum-theoretical calculation of the anharmonic oscillator by determining the missing motion constant. In particular, he used a new quantum condition, which he later called the “Canonical commutation relation”. Together with Max Born and Pascual Jordan, Heisenberg proved that his new theory led to stationary states of the oscillator and thus ensured energy conservation. After returning from Helgoland on June 19, 1925, he wrote his fundamental work “On the Quantum-Theoretical Reinterpretation of Kinetic and Mechanical Relationships” in Göttingen. He completed this study on July 9 and used the philosophical principle that only observable quantities could be included in the theoretical description of atoms. 

   After Born and Jordan had formulated the content of Heisenberg's work in a consistent mathematical theory with infinite Hermitian matrices in August and September 1925, Heisenberg helped to complete and apply this new “matrix mechanics” from September onwards. __A joint paper entitled “On Quantum Mechanics II” was submitted on November 16, 1925.__

   These events mark the decisive turning point in the history of quantum mechanics.

   (Above informations are taken from: www.heisenberg-gesellschaft.de)

   qDaT shows that a new era began on November 16, 1925, by displaying the time that has passed since then. However, qDaT does not display the time that has passed in the usual form of years, months, days, hours, minutes and seconds, but in the form: complex(qDaT-date,qDaT-time).

### qDaT format

![...](qDaT_img_1920-200.jpg)
shown datetime: January 13, 2025; 15:40:13
> __complex(qDaT-date,qDaT-time) --> ([0..1[+[0..1[j)__

   | &nbsp; | value |
   | ---: | :----------- |
   | date [0 - 1[ | Days passed since the reference date / 1000000 |
   | time [0 - 1[ | (Seconds passed since midnighty / 0.864) / 100000 |
 
   Reference time: 16.11.1925 0.00 Uhr (Born, Heisenberg, Jordan: “On Quantum Mechanics II”)

### copyright notice 

   see LICENSE

### implemented by takatoa
    
   Name      : Roland Degelmann  
   Adress    : Hofmillerstraße 12, 85356 Freising   
   Mail      : rode@takatoa.net</br>
   Web       : takatoa.net
 
### created | last modified | version

   2024-12-01 | 2024-01-28 | version: 0.1.0

