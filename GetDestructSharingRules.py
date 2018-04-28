#!/usr/bin/python3

import os, sys
from xml.dom.minidom import parse
import xml.dom.minidom

def generateDestructByBU(rootPath, listObjs, listCenterCodes):

	#Check fold paths
	sourcePath = rootPath + "/DestructSharingRules"
	if not (os.path.exists(sourcePath)):
		os.mkdir(sourcePath)

	for obj in listObjs:
		destructPackageContent = '<?xml version="1.0" encoding="UTF-8"?>\n\
<Package xmlns="http://soap.sforce.com/2006/04/metadata">\n\
	<types>'
		DOMTree = xml.dom.minidom.parse(rootPath + "/src/sharingRules/" + obj + ".sharingRules")
		collection = DOMTree.documentElement

		sharingOwnerRules = collection.getElementsByTagName("sharingOwnerRules")


		for sr in sharingOwnerRules:
			sharedFrom = sr.getElementsByTagName('sharedFrom')[0]
			groupR = sharedFrom.getElementsByTagName('role')
			if len(groupR) > 0:
				groupRName = groupR[0].childNodes[0].data
				if groupRName in listCenterCodes:
					destructPackageContent += '\n		<members>' + obj + '.' + sr.getElementsByTagName("fullName")[0].childNodes[0].data + '</members>'
			groupRS = sharedFrom.getElementsByTagName('roleAndSubordinates')
			if len(groupRS) > 0:
				groupRSName = groupRS[0].childNodes[0].data
				if groupRSName in listCenterCodes:
					destructPackageContent += '\n		<members>' + obj + '.' + sr.getElementsByTagName("fullName")[0].childNodes[0].data + '</members>'

		destructPackageContent += '\n\
        <name>SharingOwnerRule</name>\n\
    </types>\n\
    <version>40.0</version>\n\
</Package>'
		destructPackagePath = sourcePath + "/destruct" + obj + ".xml"
		f = open(destructPackagePath, "w+")
		f.write(destructPackageContent)
		f.close()