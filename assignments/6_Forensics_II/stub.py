#!/usr/bin/env python2

import sys
import struct


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!
i = 8
timestamp, = struct.unpack("<L", data[i:i+4])
i+=4
author, = struct.unpack("<8s", data[i:i+8]);
i+=8
section_count = struct.unpack("<L", data[i:i+4]);
i+=4

print(" TIMESTAMP: " + str(timestamp))
	print(" AUTHOR: %s" % author)
	print(" SECTION_COUNT: %d" % section_count)

	print("-------  BODY  ------- ")

	start = 24 
	end = start + 8
	extra_secionts = 2 
	for i in  range(section_count + extra_secionts):
		section_type, section_length = struct.unpack("<LL", data[start:end])
		section_number = i + 1
		
		print(" SECTION NUMBER: %d" % section_number)
		print(" SECTION_TYPE: %d" % section_type)
		print(" SECTION_LENGTH: %d" % section_length)

		start_of_section = end
		end_of_section = start_of_section + section_length
		print("New Section:)
		
		if section_type == 1:
			print(" SECTION_ASCII ")
			contents = struct.unpack(str(section_length) + "s", data[start_of_section:end_of_section])
			print(" CONTENTS: %s\n" % contents)
		elif section_type == 2:
			print(" SECTION_UTF8 ")
			contents = struct.unpack(str(section_length) + "s", data[start_of_section:end_of_section])
			print(" CONTENTS: %s\n" % contents)
		elif section_type == 3:
			print(" SECTION_WORDS ")
			contents = struct.unpack("<%dL" % (section_length/4), data[start_of_section:end_of_section])
			print(" CONTENTS: %s\n" % unicode(contents)
			
		else:
			print("")
			sys.exit()
		start = end_of_section 
		end = start + 8

if __name__ == "__main__":
	main()
