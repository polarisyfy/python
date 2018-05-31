#!/usr/bin/python3

import os, sys
from xml.dom.minidom import parse
import xml.dom.minidom

#Check fold paths
rootPath = "C:/3 - Study/Python/LIVE-package-CampaignSharing"
sourcePath = rootPath + "/SharingRuleNames"
if not (os.path.exists(sourcePath)):
	os.mkdir(sourcePath)

destructPackageContent = '<?xml version="1.0" encoding="UTF-8"?>\n\
<Package xmlns="http://soap.sforce.com/2006/04/metadata">\n\
	<types>'
DOMTree = xml.dom.minidom.parse(rootPath + "/src/sharingRules/Campaign.sharingRules")
collection = DOMTree.documentElement

sharingOwnerRules = collection.getElementsByTagName("sharingOwnerRules")
for sr in sharingOwnerRules:
	destructPackageContent += '\n		<members>Campaign' + '.' + sr.getElementsByTagName("fullName")[0].childNodes[0].data + '</members>'

destructPackageContent += '\n\
        <name>SharingOwnerRule</name>\n\
    </types>\n\
    <version>40.0</version>\n\
</Package>'
destructPackagePath = sourcePath + "/Campaign.xml"
f = open(destructPackagePath, "w+")
f.write(destructPackageContent)
f.close()