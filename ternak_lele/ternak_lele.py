# Program untuk peternak lele Indonesia #
# ------------------------------------- #
# File : ternak_lele.py 				#
# Author : Ahmad Rifa'i 				#
# Email : arifai209@gmail.com 			#
# ------------------------------------- #

# Inputan
nama = raw_input("Siapa nama mu? ")
jumlah_lele = int(input("Hai " + nama + " Berapa jumlah ikan lele yang kamu punya di kolam? "))
print "Ikan lele mu di kolam :", jumlah_lele, "ekor"
kasih_makan = int(input("Berapa kali Anda memberi pakan setiap harinya? "))

# Kondisi
if kasih_makan == 2:
	print "Jadwal pakan Anda :", kasih_makan, "kali perhari."
	print "Anda mengatur jadwal pakan yang tepat."
elif kasih_makan < 2:
	print "Jadwal pakan Anda :", kasih_makan, "kali perhari."
	print "Anda mengatur jadwal pakan yang kurang tepat."
elif kasih_makan > 2:
	print "Jadwal pakan Anda :", kasih_makan, "kali perhari."
	print "Anda memberikan pakan terlalu berlebihan."
elif kasih_makan == 0:
	print "Jadwal pakan Anda :", kasih_makan, "kali perhari."
	print "Maaf ikan lele Anda mati."
