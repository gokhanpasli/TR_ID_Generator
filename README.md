# TR_ID_Generator
This algorithm generates Turkish identity numbers based on the rules of the Directorate General of Civil Registration and Citizenship Affairs.

It asks the user for how many Turkish ID numbers they want to produce.

The T.C. Kimlik No is an eleven-digit number assigned by the General Directorate of Population and Citizenship Affairs to Turkish citizens. The last digit of the number is always an even number.

It has a simple error-checking feature based on parity. The units digit of the sum of the first ten digits determines the eleventh digit. Using this algorithm, it is possible to generate approximately 900 million valid T.C. identification numbers.

Additionally, the units digit of the sum of the digits 1, 3, 5, 7, and 9 multiplied by 7, plus the units digit of the sum of the digits 2, 4, 6, and 8 multiplied by 9, equals the tenth digit. The units digit of the sum of the digits 1, 3, 5, 7, and 9 multiplied by 8 determines the eleventh digit.
