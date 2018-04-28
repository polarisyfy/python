from GetCentersByBU import xlsxHandler
from GetDestructSharingRules import generateDestructByBU
from CreateXML import generateXML

rootPath = input("1/5. Input origin sharingRules folder path: ")
rootPath.replace("\\", "/")

listObjs = input("2/5. Input the objects: ").replace(" ", "").split(",")

listCenters = []
dictCenters = {}
wbPath = input("3/5. Input the excel file path for center list: ")
gotoNext = "Y"
while gotoNext == "Y":
	targetBU = input ("4/5. Input the targetBU: ")
	(listCenters, dictCenters) = xlsxHandler(wbPath, targetBU, listCenters, dictCenters)
	# generateDestructByBU(rootPath, listObjs, listCenters)
	generateXML(rootPath, targetBU, dictCenters, listObjs)
	gotoNext = input("Has next BU? (Y/N):")

print ("5/5 Done!")