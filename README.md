[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/zSomi9Bq)
# W9_5

Collect red, green and blue integer values, each on range 0-255 inclusively. This range is often described as “byte” or 8-bit. These 3 bytes (R, G and B) can be used to describe one color using hex notation “#rrggbb”, where the “rr” represents the amount of color red. The hex notation is created using the byte information.

28 = 162 = 255

Above notation:

28 - 0-1 * 8 - 8-bits (base2)
162 - 0-f * 2 - Hexadecimals (base16)
255 - 0-9 0-255 - Integer representation (base10)

So for example value 127(base-10) converts to 01111111(base-2) in 8-bit format or 7F(base-16) in hexadecimal format.

While prompting values, ensure that:

* Values are numeric
* Values are actually integers
* Value is inclusively within the 0-255 range

If any of these conditions aren’t met, then print the error message "Couldn't perform the designed task due to the invalid input values.". Continue the program execution to the end normally skipping the RGB displaying part. One way to achieve this is to use “try-except” for the whole process and then any incorrect value being collected raises exception. See Python Doc: Raising Exceptions

If the RGB was ok, then show the details like in the example program run. String format specified {:02x} converts integer into 2-digit hex format. More details in the Python Documentation page Format Specification Mini-Language.

Run 1
````
Program starting.
Insert red: 255
Insert green: 255
Insert blue: 0
RGB Details:
- Red 255
- Green 255
- Blue 0
- Hex #ffff00
- R-byte(base-2): 11111111
- G-byte(base-2): 11111111
- B-byte(base-2): 00000000
Program ending.
````

Run 2
````
Program starting.
Insert red: 0
Insert green: 255
Insert blue: 0
RGB Details:
- Red 0
- Green 255
- Blue 0
- Hex #00ff00
- R-byte(base-2): 00000000
- G-byte(base-2): 11111111
- B-byte(base-2): 00000000
Program ending.
````

Run 3
````
Program starting.
Insert red: aaa
"aaa" is non-numeric value.
Couldn't perform the designed task due to the invalid input values.
Program ending.
````

Run 4
````
Program starting.
Insert red: aaaa
"aaaa" is non-numeric value.
Couldn't perform the designed task due to the invalid input values.
Program ending.
````

Run 5
````
Program starting.
Insert red: 5
Insert green: 10
Insert blue: 2.45
"2.45" is non-numeric value.
Couldn't perform the designed task due to the invalid input values.
Program ending.
````

Run 6
````
Program starting.
Insert red: 245
Insert green: 265
Value "265" is out of the range 0-255.
Couldn't perform the designed task due to the invalid input values.
Program ending.
````
