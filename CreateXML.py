#!/usr/bin/python3

import os, sys

def generateXML(rootPath, targetBU, dictCenters, listObjs):
	dictBU2Alias = {"China Own" : "CN_OWN",
					"China Franchise" : "CN_FRA",
					"Russia Own" : "RU_OWN",
					"Indonesia Franchise" : "ID_FRA"}
	bu = dictBU2Alias[targetBU]
	# listObjs = ["Lead",
	# 			"Account",
	# 			"Opportunity",
	# 			"Campaign",
	# 			"Apttus_Config2__AssetLineItem__c",
	# 			"B25__Availability__c",
	# 			"B25__Group__c",
	# 			"B25__Group_Membership__c",
	# 			"Apttus_Config2__Order__c",
	# 			"Payment__c",
	# 			"Apttus_Proposal__Proposal__c",
	# 			"B25__Reservation__c",
	# 			"B25__Resource__c",
	# 			"B25__Staff__c",
	# 			"Usage__c"]

	#Check fold paths
	targetPath = rootPath + "/AddSharingRules" + "/" + bu
	if not (os.path.exists(targetPath)):
		os.makedirs(targetPath)
	for obj in listObjs:
		objPath = targetPath + "/" + obj + "/src/sharingRules"
		if not (os.path.exists(objPath)):
			os.makedirs(objPath)

	dictObj2Group = {'Lead' : {'CN_OWN' : 'R', 'CN_FRA' : 'R', 'RU_OWN' : 'RS', 'ID_FRA' : 'RS'},
					 'Account' : {'CN_OWN' : 'R', 'CN_FRA' : 'R', 'RU_OWN' : 'RS', 'ID_FRA' : 'RS'},
					 'Opportunity' : {'CN_OWN' : 'R', 'CN_FRA' : 'R', 'RU_OWN' : 'RS', 'ID_FRA' : 'RS'},
					 'Campaign' : {'CN_OWN' : 'R', 'CN_FRA' : 'R', 'RU_OWN' : 'R', 'ID_FRA' : 'RS'},
					 'Apttus_Config2__AssetLineItem__c' : {'CN_OWN' : 'R', 'CN_FRA' : 'R', 'RU_OWN' : 'R', 'ID_FRA' : 'R'},
					 'B25__Availability__c' : {'CN_OWN' : 'RS', 'CN_FRA' : 'RS', 'RU_OWN' : 'RS', 'ID_FRA' : 'RS'},
					 'B25__Group__c' : {'CN_OWN' : 'RS', 'CN_FRA' : 'RS', 'RU_OWN' : 'RS', 'ID_FRA' : 'RS'},
					 'B25__Group_Membership__c' : {'CN_OWN' : 'RS', 'CN_FRA' : 'RS', 'RU_OWN' : 'RS', 'ID_FRA' : 'RS'},
					 'Apttus_Config2__Order__c' : {'CN_OWN' : 'R', 'CN_FRA' : 'R', 'RU_OWN' : 'RS', 'ID_FRA' : 'RS'},
					 'Payment__c' : {'CN_OWN' : 'R', 'CN_FRA' : 'R', 'RU_OWN' : 'R', 'ID_FRA' : 'R'},
					 'Apttus_Proposal__Proposal__c' : {'CN_OWN' : 'R', 'CN_FRA' : 'R', 'RU_OWN' : 'R', 'ID_FRA' : 'R'},
					 'B25__Reservation__c' : {'CN_OWN' : 'RS', 'CN_FRA' : 'RS', 'RU_OWN' : 'RS', 'ID_FRA' : 'RS'},
					 'B25__Resource__c' : {'CN_OWN' : 'RS', 'CN_FRA' : 'RS', 'RU_OWN' : 'RS', 'ID_FRA' : 'RS'},
					 'B25__Staff__c' : {'CN_OWN' : 'RS', 'CN_FRA' : 'RS', 'RU_OWN' : 'RS', 'ID_FRA' : 'RS'},
					 'Usage__c' : {'CN_OWN' : 'R', 'CN_FRA' : 'R', 'RU_OWN' : 'R', 'ID_FRA' : 'R'},
					 'News__c' : {'CN_OWN' : 'R', 'CN_FRA' : 'R', 'RU_OWN' : 'R', 'ID_FRA' : 'R'}}

	dictObjAcc = {'Lead' : {'CN_OWN' : 'Read', 'CN_FRA' : 'Read', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'},
				  'Account' : {'CN_OWN' : 'Read', 'CN_FRA' : 'Read', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'},
				  'Opportunity' : {'CN_OWN' : 'Read', 'CN_FRA' : 'Read', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'},
				  'Campaign' : {'CN_OWN' : 'Edit', 'CN_FRA' : 'Edit', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'},
				  'Apttus_Config2__AssetLineItem__c' : {'CN_OWN' : 'Edit', 'CN_FRA' : 'Edit', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'},
				  'B25__Availability__c' : {'CN_OWN' : 'Read', 'CN_FRA' : 'Read', 'RU_OWN' : 'Read', 'ID_FRA' : 'Read'},
				  'B25__Group__c' : {'CN_OWN' : 'Edit', 'CN_FRA' : 'Edit', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'},
				  'B25__Group_Membership__c' : {'CN_OWN' : 'Edit', 'CN_FRA' : 'Edit', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'},
				  'Apttus_Config2__Order__c' : {'CN_OWN' : 'Edit', 'CN_FRA' : 'Edit', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'},
				  'Payment__c' : {'CN_OWN' : 'Edit', 'CN_FRA' : 'Edit', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'},
				  'Apttus_Proposal__Proposal__c' : {'CN_OWN' : 'Edit', 'CN_FRA' : 'Edit', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'},
				  'B25__Reservation__c' : {'CN_OWN' : 'Edit', 'CN_FRA' : 'Edit', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'},
				  'B25__Resource__c' : {'CN_OWN' : 'Read', 'CN_FRA' : 'Read', 'RU_OWN' : 'Read', 'ID_FRA' : 'Read'},
				  'B25__Staff__c' : {'CN_OWN' : 'Edit', 'CN_FRA' : 'Edit', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'},
				  'Usage__c' : {'CN_OWN' : 'Read', 'CN_FRA' : 'Read', 'RU_OWN' : 'Read', 'ID_FRA' : 'Read'},
				  'News__c' : {'CN_OWN' : 'Edit', 'CN_FRA' : 'Edit', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'}}

	leadContentTemplate = '\n \
		<sharingOwnerRules>\n \
			<fullName>{0}_{1}_{2}</fullName>\n \
			<accessLevel>{3}</accessLevel>\n \
			<description>OMS-2390, internally share the center data</description>\n \
			<label>{0}_{1}_{2}</label>\n \
			<sharedTo>\n \
				<group>{0}_{1}_{2}</group>\n \
			</sharedTo>\n \
			<sharedFrom>\n \
				<roleAndSubordinates>{4}</roleAndSubordinates>\n \
			</sharedFrom>\n \
		</sharingOwnerRules>'
	accountContentTemplate = '\n\
		<sharingOwnerRules>\n\
			<fullName>{0}_{1}_{2}</fullName>\n\
			<accessLevel>{3}</accessLevel>\n\
			<description>OMS-2390, internally share the center data</description>\n\
			<accountSettings>\n\
				<caseAccessLevel>None</caseAccessLevel>\n\
				<contactAccessLevel>Read</contactAccessLevel>\n\
				<opportunityAccessLevel>None</opportunityAccessLevel>\n\
			</accountSettings>\n\
			<label>{0}_{1}_{2}</label>\n\
			<sharedTo>\n\
				<group>{0}_{1}_{2}</group>\n\
			</sharedTo>\n\
			<sharedFrom>\n\
				<roleAndSubordinates>{4}</roleAndSubordinates>\n\
			</sharedFrom>\n\
		</sharingOwnerRules>'
	dictObjContentTemplate = {'Lead' : leadContentTemplate,
							  'Account' : accountContentTemplate,
							  'Opportunity' : leadContentTemplate,
							  'Campaign' : leadContentTemplate,
							  'Apttus_Config2__AssetLineItem__c' : leadContentTemplate,
							  'B25__Availability__c' : leadContentTemplate,
							  'B25__Group__c' : leadContentTemplate,
							  'B25__Group_Membership__c' : leadContentTemplate,
							  'Apttus_Config2__Order__c' : leadContentTemplate,
							  'Payment__c' : leadContentTemplate,
							  'Apttus_Proposal__Proposal__c' : leadContentTemplate,
							  'B25__Reservation__c' : leadContentTemplate,
							  'B25__Resource__c' : leadContentTemplate,
							  'B25__Staff__c' : leadContentTemplate,
							  'Usage__c' : leadContentTemplate,
							  'News__c' : leadContentTemplate}

	for obj in listObjs:
		packageContent = '<?xml version="1.0" encoding="UTF-8"?>\n\
    <Package xmlns="http://soap.sforce.com/2006/04/metadata">\n\
        <types>'

		content = '<?xml version="1.0" encoding="UTF-8"?>\n<SharingRules xmlns="http://soap.sforce.com/2006/04/metadata">'
		for center in dictCenters.keys():
			content += dictObjContentTemplate[obj].format(bu, dictObj2Group[obj][bu], center, dictObjAcc[obj][bu],
				dictCenters[center])
			packageContent += '\n		<members>' + obj + '.' + bu + '_' + dictObj2Group[obj][bu] + '_' + center + '</members>'
		content += '\n</SharingRules>'
		filepath = targetPath + "/" + obj + "/src/sharingRules/" + obj + ".sharingRules"
		f = open(filepath,"w+")
		f.write(content)
		f.close()

		packageContent += '\n\
        <name>SharingOwnerRule</name>\n\
    </types>\n\
    <version>40.0</version>\n\
</Package>'
		packagePath = targetPath + "/" + obj + "/src/package.xml"
		f = open(packagePath, "w+")
		f.write(packageContent)
		f.close()