#!/usr/bin/env python3

import shutil
import os

def main():
    #Move into a Working Directory. -- It's like using 'cd ~/my code/5g_research/"""
    os.chdir("/home/student/mycode/")

    # Copy file a to b -- It's like using 'cp filea fileb'
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    #Copy the entire directoryA to directoryB
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research", "5g_research_backup/")

if __name__=="__main__":
    main()
