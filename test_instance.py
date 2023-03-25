import align_sequence as al
import time

fichier_instances=["Inst_0000010_44.adn","Inst_0000010_8.adn","Inst_0000010_7.adn","Inst_0000012_13.adn",\
						"Inst_0000012_32.adn","Inst_0000012_56.adn","Inst_0000014_83.adn","Inst_0000013_45.adn",\
						"Inst_0000013_56.adn","Inst_0000013_89.adn","Inst_0000014_7.adn","Inst_0000015_4.adn",\
						"Inst_0000015_2.adn","Inst_0000015_76.adn","Inst_0000020_32.adn","Inst_0000020_17.adn",\
						"Inst_0000020_8.adn","Inst_0000050_3.adn","Inst_0000050_9.adn","Inst_0000050_77.adn",\
						"Inst_0000100_3.adn","Inst_0000100_7.adn","Inst_0000100_44.adn","Inst_0000500_3.adn",\
						"Inst_0000500_8.adn","Inst_0000500_88.adn","Inst_0001000_7.adn","Inst_0001000_23.adn",\
						"Inst_0001000_2.adn","Inst_0002000_8.adn","Inst_0002000_3.adn","Inst_0002000_44.adn",\
						"Inst_0003000_25.adn","Inst_0003000_45.adn","Inst_0003000_10.adn","Inst_0003000_1.adn",\
						"Inst_0005000_4.adn","Inst_0005000_33.adn","Inst_0005000_32.adn","Inst_0008000_98.adn",\
						"Inst_0008000_54.adn","Inst_0010000_8.adn","Inst_0010000_50.adn","Inst_0010000_7.adn",\
						"Inst_0015000_20.adn","Inst_0015000_30.adn","Inst_0015000_3.adn","Inst_0020000_77.adn",\
						"Inst_0020000_5.adn","Inst_0020000_64.adn","Inst_0050000_6.adn","Inst_0050000_63.adn",\
						"Inst_0050000_88.adn","Inst_0100000_3.adn","Inst_0100000_11.adn","Inst_0100000_76.adn",]

#*********************************** TACHE A ******************************************#
print("Instance : <Inst_0000010_44.adn>")
inst_44 = al.lire_instance("Inst_0000010_44.adn")
x , y ,taille_x, taille_y = inst_44
print("x = {}\ny = {}".format(x,y))
start_time = time.time()
print("Distance d'edition :",al.DIST_NAIF(x,y))
print("Temps d execution : %.6s secondes\n" % (time.time() - start_time))

print("Instance : <Inst_0000010_7.adn>")
inst_7 = al.lire_instance("Inst_0000010_7.adn")
x , y, taille_x, taille_y = inst_7
print("x = {}\ny = {}".format(x,y))
start_time = time.time()
print("Distance d'edition :",al.DIST_NAIF(x,y))
print("Temps d execution : %.6s secondes\n" % (time.time() - start_time))

print("Instance : <Inst_0000010_8.adn>")
inst_8 = al.lire_instance("Inst_0000010_8.adn")
x , y, taille_x, taille_y = inst_8
print("x = {}\ny = {}".format(x,y))
start_time = time.time()
print("Distance d'edition :",al.DIST_NAIF(x,y))
print("Temps d execution : %.6s secondes\n" % (time.time() - start_time))
""" decommenter pour tester 
for i in fichier_instances:
	instance = al.lire_instance(i)
	x, y, taille_x, taille_y = instance

	print("{}".format(i))
	print("x = {} taille = {}".format(x, taille_x))
	print("y = {} taille = {}".format(y, taille_y))
	start_time = time.time()
	print("Distance d'edition :",al.DIST_NAIF(x,y))
	print("Temps d execution : %.6s secondes\n" % (time.time() - start_time))
"""
#*********************************** TACHE B ******************************************#

for i in fichier_instances:
	instance = al.lire_instance(i)
	x, y, taille_x, taille_y = instance
	print("Instance : <{}> ".format(i))
	print("x = {} ; taille = {} \ny = {} ; taille = {}".format(x, taille_x, y, taille_y))
	start_time = time.time()
	d, (ch1, ch2) = al.PROG_DYN(x,y)
	print("Temps d execution : %.6s secondes" % (time.time() - start_time))
	print("Alignement minimale :\nmot1 : {}\nmot2 : {}\n".format(ch1,ch2))


#*********************************** TACHE C ******************************************#

for i in fichier_instances:
	instance = al.lire_instance(i)
	x, y, taille_x, taille_y = instance
	print("Instance : <{}>".format(i))
	start_time = time.time()
	print("Distance d'edition :",al.DIST_2(x,y))
	print("Temps d execution : %.6s secondes\n" % (time.time() - start_time))

#*********************************** TACHE D ******************************************#

for i in fichier_instances:
	instance = al.lire_instance(i)
	x, y, taille_x, taille_y = instance
	print("Instance : <{}>".format(i))
	start_time = time.time()
	mot1, mot2 = al.SOL_2(x,y)
	print("Temps d execution : %.6s secondes" % (time.time() - start_time))
	print("Alignement minimale :\nmot1 : {}\nmot2 : {}\n".format(mot1,mot2))
