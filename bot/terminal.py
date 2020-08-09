import os
import random
from time import strftime

x = random.randint(5, 10)

os.system("git remote add origin https://github.com/SahanChan/keepingStreakAlive.git")
for i in range(0, x):

    my_file = open("DateAndTime_Commit.dat", 'a')

    my_file.write(str(strftime("%Y-%m-%d")))
    my_file.write(" - ")
    my_file.write(str(strftime("%H:%M:%S")))
    my_file.write("\t")
    my_file.write("Made a Commit")
    my_file.write("\n")
    my_file.close()
    os.system('git add .')
    os.system("git commit -m 'Bot_commit'")
    os.system("git push -u origin master")
