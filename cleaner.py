#! /usr/bin/env python
# ~ encoding: utf-8 ~
#
# Res andy
# fixed by Vgr

import xml.etree.ElementTree as ET
import os

# This should be ran in Python 2.7 or any version of Python 3

###########################################################
#  - Always backup your map before launching this script  #
#  - Do that even so this script does its backup as well  # 
#  - Place this file directly into the map folder         # 
#  - Please report any errors to andys@deltaflyer.cz      #
#  - You can contact me on unofficial IRC ME channel too  #
#  - join #medieval-engineers on irc.esper.net - Andy_S   #
#  - Code improved and fixed by Vgr (also on IRC)         #
###########################################################

with open("SANDBOX_0_0_0_.sbs") as file, open("SANDBOX_0_0_0_.bak", "w") as backup:
    content = file.readlines()
    backup.write(os.linesep.join(content))
    header = content[1]

tree = ET.parse('SANDBOX_0_0_0_.sbs') # creates XML tree from sandbox.sbc file
root = tree.getroot() # creates XML root from the tree

to_remove = [] # list of stuff to remove

for i, child in enumerate(root):
    if child.tag == "SectorObjects":
        for obj in child:
            if "MyObjectBuilder_CubeGrid" not in obj.attrib.values():
                continue
            for element in obj:
                if element.tag == "CubeBlocks":
                    for block in element[0]:
                        if block.tag == "SubtypeName":
                            if block.text == "ScrapWoodBranches": 
                                to_remove.append(obj)

        break

for child in to_remove:
    root[i].remove(child)

print ("deleted %i branches" % len(to_remove)) # Python 2 & 3 compatibility
tree = ET.ElementTree(root)
tree.write('SANDBOX_0_0_0_.sbs', encoding='utf-8', xml_declaration=True) # save the file

with open("SANDBOX_0_0_0_.sbs") as world:
    data = world.readlines()

data[1] = header

with open("SANDBOX_0_0_0_.sbs", "w") as to_write:
    to_write.write(os.linesep.join(data))
