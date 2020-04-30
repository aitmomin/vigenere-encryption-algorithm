# vigenere-encryption-algorithm

The implementation of the Vigenère encryption algorithm.

Encryption method Rot 13
Among the basic encryption algorithms, we can first mention the ROT13 algorithm which consists of shifting each letter of the message by thirteen notches in the alphabet:

a - n
b - o
...
y - l
z - m

Mathematically, if the letters of the alphabet are numbered from 0 to 25, the algorithm consists simply in adding 13 to their rank and considering the result modulo 26 to make sure that it remains between 0 and 25.
Vigenère encryption algorithm
Fixed shift encryption algorithms like ROT13 are relatively easy to break, indeed, for an alphabet of 26 letters, there are only 26 possible shifts (including one trivial) and it is enough to test them all to decipher the message considered. Vigenère's algorithm consists in introducing a key which makes it possible to make the offset variable according to the position of the character in the message.

The example below encrypts the clear message "bring out your dead" by Vigenère's algorithm with the key "grail":
The encrypted message "hiivr fub efuz jval" is obtained by successively using the offsets given by the key.
