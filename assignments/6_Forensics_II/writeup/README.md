# Writeup 6 - Forensics

Name: Esther Malone
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Esther Malone 

## Assignment Writeup

### Part 1 (45 Pts)

1) 159.203.113.181
2) nmap
3) 142.93.136.81
4) 21
5) findme.jpeg
  a) This is a .jpeg file
  b) Rambla General Jose Artigas, 20100 Punta del Este, Departamento de Maldonado, Uruguay
  c) 2018:12:23 17:16:24
  d) 4.5 m 
6) greetz.fpff
7) 

### Part 2 (55 Pts)
The author of greetz.fpff is fl1nch
The section count was 5. 

Section 1: 
Type: 1, SECTION ASCII
Contents: Hey you, keep looking :)

Section 2: 
Type: 6, SECTION_COORD
Contents: 52.336035, 4.880673

Section 3:
Type: 8, SECTION PNG
Created PNG image of testudo

Section 4: 
Type 1: SECTION_ASCII
Contents: }R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC

Section 5:
Type: 1
Contents: Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30=


Flags
First one was in the fourth section
}R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC

Next was in the image from the png section
CMSC389R-{w3lc0me_b@ck_fr0m_spr1ng_br3ak}

This one was in section 5 its contents: Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30=
converts base64 to 
CMSC389R-{hey_h3y_y0U_you_I_dont_nt_like_your_base64_encoding}
