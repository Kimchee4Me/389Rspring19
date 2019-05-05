# Crypto II Writeup

Name: Esther Malone
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Esther Malone

## Assignment Writeup

### Part 1 (70 Pts)
Flag: CMSC389R-{m3ss@g3_!n_A_b0ttl3}
### Part 2 (30 Pts)

In both images the original image is being altered/hidden. I would say the ECB cipher mode is less secure as it does not completley cover the image as CBC does.It leaks information about the original image. In ECB each block is concatenated to the next block, in contrast in CBC every block is XOR'ed with the exncrypted previous block, which means every block depends on the output of the previous block. This makes it more secure. 
