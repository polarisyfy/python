#!/usr/bin/python3

import os, sys
from xml.dom.minidom import parse
import xml.dom.minidom

listCenterCodes = ["DIDTES01", "DEB", "DEA", "MRA", "MLA", "JRA", "JMR", "GRA", "MLB", "KEA", "SUA", "SUB", "SUC", "SDA", "SBY", "SUD", "JAK", "BDC", "BEC", "BEB", "BEA", "BDE", "BDD", "BDB", "BDA", "GWA", "PTA", "PAD", "YYA", "MTR", "MDC", "LPA", "JAO", "KPG", "PBA", "SMA", "STR", "CBA", "SLA", "SMB", "MED", "MKS", "PKA", "PJT", "TGC", "PDG", "KRW", "KHI", "JAR", "JAM", "JAF", "JAE", "JAC", "CLA", "BMS", "BAA", "DPA", "JAP", "BIA", "JAA", "SAA", "RMG", "KWA", "PUR", "TGR", "JAS", "JAN", "JAI", "JAH", "GAD", "BGA", "BGB", "TGB", "C0023"]
listObjs = ["Lead",
			"Account",
			"Opportunity",
			"Campaign",
			"Apttus_Config2__AssetLineItem__c",
			"B25__Availability__c",
			"B25__Group__c",
			"B25__Group_Membership__c",
			"Apttus_Config2__Order__c",
			"Payment__c",
			"Apttus_Proposal__Proposal__c",
			"B25__Reservation__c",
			"B25__Resource__c",
			"B25__Staff__c",
			"Usage__c"]

#Check fold paths
rootPath = "C:/3 - Study/Python/DestructSharingRules"
if not (os.path.exists(rootPath)):
	os.mkdir(rootPath)

for obj in listObjs:
	destructPackageContent = '<?xml version="1.0" encoding="UTF-8"?>\n\
<Package xmlns="http://soap.sforce.com/2006/04/metadata">\n\
	<types>'
	DOMTree = xml.dom.minidom.parse("C:/3 - Study/Python/LIVE-package-SharingRule/src/sharingRules/" + obj + ".sharingRules")
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
	destructPackagePath = rootPath + "/destruct" + obj + ".xml"
	f = open(destructPackagePath, "w+")
	f.write(destructPackageContent)
	f.close()