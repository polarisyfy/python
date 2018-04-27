#!/usr/bin/python3

import os, sys

bu = 'RU_OWN'
dictCenters = {'Novosibirsk':'NSA',
'Bolshevikov':'SNF',
'Pionerskaya':'SNC',
'Veteranov':'SNB',
'Nevsky_KnT':'SNA',
'Preobrazhenka':'MOU',
'Degunino':'MOK',
'Universitet':'MOV',
'Aeroport':'MOI',
'Sevastopolskaya':'MOH',
'Zhulebino':'MOF',
'Marino':'MOE',
'Alexeevskaya':'MOD',
'Yugo_Zapadnaya':'MOC',
'Novye_Cheryemushki':'MOB'}

# bu = 'ID_FRA'
# dictCenters = {'Bali_Kuta':'DEB',
# 'Bali_HW':'DEA',
# 'Lombok':'MRA',
# 'Malang_1_Ijen':'MLA',
# 'Jember':'JRA',
# 'Sby_Jemursari':'JMR',
# 'Gresik':'GRA',
# 'Malang_2_Sawojajar':'MLB',
# 'Kediri':'KEA',
# 'Sby_Kayun':'SUA',
# 'Sby_Plaza':'SUB',
# 'Sby_Bukit_Mas':'SUC',
# 'Sidoarjo':'SDA',
# 'Sby_PTC':'SBY',
# 'Sby_Klampis':'SUD',
# 'Kalimalang':'JAK',
# 'Bdg_BKR':'BDC',
# 'Bekasi_Summarecon':'BEC',
# 'Cikarang':'BEB',
# 'Bekasi':'BEA',
# 'Cimahi':'BDE',
# 'Bandung_Antapani':'BDD',
# 'Bdg_Banda':'BDB',
# 'Bdg_Ciwalk':'BDA',
# 'Grand_Wisata':'GWA',
# 'Pontianak':'PTA',
# 'Padang':'PAD',
# 'Yog_YAPSquare':'YYA',
# 'Matraman':'MTR',
# 'Manado':'MDC',
# 'Lampung':'LPA',
# 'Gunung_Sahari':'JAO',
# 'Kupang':'KPG',
# 'Palembang':'PBA',
# 'Semarang1_MT_Haryono':'SMA',
# 'Sunter':'STR',
# 'Cirebon':'CBA',
# 'Solo':'SLA',
# 'Semarang2_Prof_Soedarto':'SMB',
# 'Medan':'MED',
# 'Makassar':'MKS',
# 'Pekanbaru':'PKA',
# 'Pejaten':'PJT',
# 'Pamulang':'TGC',
# 'Taman_Mini':'PDG',
# 'Karawaci':'KRW',
# 'Kota_Harapan_Indah':'KHI',
# 'Permata_Hijau':'JAR',
# 'Cibubur':'JAM',
# 'Kelapa_Gading':'JAF',
# 'Pondok_Indah':'JAE',
# 'Cipete':'JAC',
# 'Cilegon':'CLA',
# 'Banjarmasin':'BMS',
# 'Balikpapan':'BAA',
# 'Depok':'DPA',
# 'Cinere':'JAP',
# 'Bintaro':'BIA',
# 'Gajah_Mada':'JAA',
# 'Samarinda':'SAA',
# 'Rawamangun':'RMG',
# 'Kota_Wisata':'KWA',
# 'Puri_Indah':'PUR',
# 'Tangerang_City':'TGR',
# 'Cengkareng':'JAS',
# 'Tanjung_Duren':'JAN',
# 'Tebet':'JAI',
# 'Pluit':'JAH',
# 'Gading_Serpong':'GAD',
# 'Bgr_Padjajaran':'BGA',
# 'Bgr_Yasmin':'BGB',
# 'BSD_Tangerang':'TGB',
# 'Cikupa':'C0023'}

# bu = "CN_OWN"
# dictCenters = {'FZ2CS1':'DCNFOC03',
# 'FZ1JA1':'DCNFOC02',
# 'CQ8YZ':'DCNCKG10',
# 'CQ9XYJ':'DCNCKG11',
# 'CQ7RH':'DCNCKG09',
# 'CQ1DP':'CQA',
# 'CQ6SPB':'DCNCKG08',
# 'CQ5NP':'DCNCKG07',
# 'CQ4YJP':'DCNCKG06',
# 'CQ2BC':'CQB',
# 'SZ12LG1':'DCNSZX20',
# 'SZ11LH1':'DCNSZX19',
# 'SZ10FT4':'DCNSZX17',
# 'SZ1FT1':'SZA',
# 'SZ2FT2':'SZH',
# 'SZ6NS3':'SZP',
# 'SZ7FT3':'SZQ',
# 'KS1KC1':'DCNSUZ09',
# 'GZ11BY1':'DCNCAN20',
# 'BJ18CY6':'DCNBJS31',
# 'BJ17HD5':'DCNBJS30',
# 'SZ15FT6':'DCNSZX23',
# 'SZ16LG2':'DCNSZX22',
# 'SZ15FT5':'DCNSZX21',
# 'SZ19NS5':'DCNSZX28',
# 'SZ18LH3':'DCNSZX27',
# 'SZ17LH2':'DCNSZX26',
# 'BJ11CY4':'DCNBJS22',
# 'APU':'APU',
# 'SZ5NS2':'SZO',
# 'SZ4BA1':'SZJ',
# 'SZ3NS1':'SZI',
# 'SH20PD4':'SXG',
# 'SH19BS1':'SXF',
# 'SH17ZB1':'SXB',
# 'SH16PT3':'SXA',
# 'SH15PD3':'SHZ',
# 'SH13CN2':'SHU',
# 'BJ9HD3':'BJV',
# 'BJ8DC3':'BJU',
# 'BJ7DC2':'BJP',
# 'BJ6CY3':'BJO',
# 'BJ5HD2':'BJN',
# 'BJ4CY2':'BJM',
# 'BJ3CY1':'BJL',
# 'BJ2DC1':'BJK',
# 'BJ1HD1':'BJJ',
# 'SH12PD2':'SHT',
# 'SH11HP1':'SHS',
# 'SH10CN1':'SHR',
# 'SH9YP1':'SHQ',
# 'SH8XH2':'SHP',
# 'SH7HK1':'SHO',
# 'SH6MH3':'SHN',
# 'SH3MH1':'SHE',
# 'SH2PD1':'SHB',
# 'SH1PT1':'SHA',
# 'GZ8HZ3':'GZS',
# 'GZ7TH2':'GZP',
# 'FS2NH1':'GZO',
# 'FS1SD1':'GZM',
# 'GZ6HZ2':'GZL',
# 'GZ5PY1':'GZK',
# 'GZ4LW1':'GZG',
# 'GZ3TH1':'GZD',
# 'GZ2HZ1':'GZB',
# 'GZ1YX1':'GZA',
# 'SZ9BA2':'DCNSZX16',
# 'SZ8NS4':'DCNSZX13',
# 'SH23MH4':'DCNSHA33',
# 'SH22CN3':'DCNSHA32',
# 'SH21BS2':'DCNSHA31',
# 'SH18PD5':'DCNSHA26',
# 'GZ10YX3':'DCNCAN19',
# 'GZ9YX2':'DCNCAN18',
# 'BJ16CY5':'DCNBJS29',
# 'BJ15HD4':'DCNBJS26',
# 'BJ12YZ1':'DCNBJS25',
# 'BJ10FT1':'DCNBJS21',
# 'CQ3XN':'CQC',
# 'GZ12YX4':'C0018'}

# bu = "CN_FRA"
# dictCenters = {'ChangChun6':'CHG',
# 'Harbin2':'HBC',
# 'Shenyang3':'SYC',
# 'Qingdao3':'QDC',
# 'Chengdu11':'CEK',
# 'Chengdu10':'CEJ',
# 'Nanjing5':'NJE',
# 'Jinzhou2':'JZB',
# 'Wuhan7':'WNG',
# 'ChengDu13':'CEM',
# 'Changzhou1':'CZA',
# 'Changshu1':'CSA',
# 'Changsha2':'CGB',
# 'Changsha1':'CGA',
# 'Changchun4':'CHE',
# 'Changchun3':'CHD',
# 'Changchun2':'CHB',
# 'Changchun1':'CHA',
# 'Baotou1':'BTB',
# 'Zhenjiang1':'ZGA',
# 'Zhengzhou4':'ZZD',
# 'Zhengzhou3':'ZZC',
# 'Zhengzhou1':'ZZA',
# 'Zhengzhou2':'ZZB',
# 'Zhangjiagang2':'ZJB',
# 'Zhangjiagang1':'ZJA',
# 'Yuyao1':'YUA',
# 'Yiwu1':'YWA',
# 'Yantai1':'YTA',
# 'Xuzhou2':'XZB',
# 'Xuzhou1':'XZA',
# 'Xiaoshan1':'XSA',
# 'Xian4':'XAD',
# 'Xian3':'XAC',
# 'Xian1':'XAA',
# 'Xian2':'XAB',
# 'Xiamen1':'XMA',
# 'Xiamen2':'XMB',
# 'Wuxi5':'WXE',
# 'Wuxi3':'WXC',
# 'Wuxi4':'WXD',
# 'Wuxi2':'WXB',
# 'Wuxi1':'WXA',
# 'Wuhan5':'WNE',
# 'Wuhan4':'WND',
# 'Wuhan3':'WNC',
# 'Wuhan2':'WNB',
# 'Wuhan1':'WNA',
# 'Weihai1':'WHA',
# 'Urumqi4':'URD',
# 'Urumqi3':'UMC',
# 'Urumqi2':'UMB',
# 'Urumqi1':'UMA',
# 'Tianjin7':'TJG',
# 'Tianjin6':'TJF',
# 'Tianjin5':'TJE',
# 'Tianjin4':'TJD',
# 'Tianjin3':'TJC',
# 'Tianjin2':'TJB',
# 'Tianjin1':'TJA',
# 'Tangshan2':'TSB',
# 'Tangshan1':'TSA',
# 'Taizhou2':'TZB',
# 'Taizhou3':'TZC',
# 'Taizhou1':'TZA',
# 'Taiyuan2':'TYB',
# 'Taiyuan3':'TYC',
# 'Taiyuan1':'TYA',
# 'Suzhou3':'SOD',
# 'Suzhou2':'SOB',
# 'Suzhou1':'SOA',
# 'Shijiazhuang3':'SIC',
# 'Shijiazhuang2':'SIB',
# 'Shijiazhuang1':'SIA',
# 'Shenyang2':'SYB',
# 'Shenyang1':'SYA',
# 'Shaoxing1':'SAB',
# 'Qinhuangdao1':'QHA',
# 'Qingdao2':'QDB',
# 'Qingdao1':'QDA',
# 'Ningbo3':'NBC',
# 'Ningbo1':'NBA',
# 'Ningbo2':'NBB',
# 'Nantong1':'NTA',
# 'Nanning1':'NNA',
# 'Nanjing3':'NJC',
# 'Nanjing2':'NJB',
# 'Lanzhou1':'LZB',
# 'Nanjing1':'NJA',
# 'Jinzhou1':'JZA',
# 'Jinhua1':'JHA',
# 'Jiaxing1':'JIA',
# 'Hohhot1':'NMG',
# 'Huizhou1':'HZA',
# 'Huzhou1':'HOA',
# 'Hefei4':'HED',
# 'Hefei3':'HEC',
# 'Hefei2':'HEB',
# 'Hefei1':'HEA',
# 'Harbin1':'HBA',
# 'Hangzhou7':'HZG',
# 'Hangzhou6':'HAG',
# 'Hangzhou5':'HAH',
# 'Hangzhou4':'HZE',
# 'Hangzhou3':'HAD',
# 'Hangzhou1':'HAA',
# 'Hangzhou2':'HAB',
# 'Guiyang1':'GBA',
# 'Dongying1':'DGA',
# 'Dongguan2':'DOB',
# 'Dongguan1':'DOA',
# 'Daqing1':'DQA',
# 'Daqing2':'DQB',
# 'Chengdu9':'CEI',
# 'Chengdu8':'CEH',
# 'Chengdu7':'CEG',
# 'Chengdu6':'CEF',
# 'Chengdu4':'CED',
# 'Chengdu3':'CEC',
# 'Chengdu5':'CDE',
# 'Chengdu2':'CEB',
# 'Chengdu1':'CEA',
# 'Dalian2':'DAB',
# 'Dalian1':'DAA',
# 'Cixi1':'CXA',
# 'Dalian3':'DAC',
# 'Nanjing4':'NJD',
# 'Hefei5':'HFE',
# 'Hohhot2':'NMB',
# 'Xuzhou3':'XZC',
# 'Wuhan6':'WNF',
# 'Zhengzhou5':'ZZE',
# 'XiAn5':'XAE',
# 'Suzhou4':'SOE',
# 'Dongguan3':'DOC',
# 'Jiaxing2':'JIB',
# 'Zhengzhou6':'ZZF',
# 'Changchun5':'CHF',
# 'Changsha3':'CGC',
# 'Ningbo4':'NBD',
# 'Zhengzhou7':'ZZG',
# 'NanJing6':'NJF',
# 'Chengdu12':'CEL',
# 'HangZhou8':'HAJ',
# 'Hefei6':'HEF'}

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
listObjs = ["News__c"]

#Check fold paths
rootPath = "C:/3 - Study/Python/AddSharingRules"
if not (os.path.exists(rootPath)):
	os.mkdir(rootPath)
for obj in listObjs:
	objPath = rootPath + "/" + obj + "/src/sharingRules"
	print (objPath)
	print (os.path.exists(rootPath))
	if not (os.path.exists(rootPath)):
		os.makedirs(objPath)

# dictObj2Group = {'Lead' : {'CN_OWN' : 'R', 'CN_FRA' : 'R', 'RU_OWN' : 'RS', 'ID_FRA' : 'RS'},
# 				 'Account' : {'CN_OWN' : 'R', 'CN_FRA' : 'R', 'RU_OWN' : 'RS', 'ID_FRA' : 'RS'},
# 				 'Opportunity' : {'CN_OWN' : 'R', 'CN_FRA' : 'R', 'RU_OWN' : 'RS', 'ID_FRA' : 'RS'},
# 				 'Campaign' : {'CN_OWN' : 'R', 'CN_FRA' : 'R', 'RU_OWN' : 'R', 'ID_FRA' : 'RS'},
# 				 'Apttus_Config2__AssetLineItem__c' : {'CN_OWN' : 'R', 'CN_FRA' : 'R', 'RU_OWN' : 'R', 'ID_FRA' : 'R'},
# 				 'B25__Availability__c' : {'CN_OWN' : 'RS', 'CN_FRA' : 'RS', 'RU_OWN' : 'RS', 'ID_FRA' : 'RS'},
# 				 'B25__Group__c' : {'CN_OWN' : 'RS', 'CN_FRA' : 'RS', 'RU_OWN' : 'RS', 'ID_FRA' : 'RS'},
# 				 'B25__Group_Membership__c' : {'CN_OWN' : 'RS', 'CN_FRA' : 'RS', 'RU_OWN' : 'RS', 'ID_FRA' : 'RS'},
# 				 'Apttus_Config2__Order__c' : {'CN_OWN' : 'R', 'CN_FRA' : 'R', 'RU_OWN' : 'RS', 'ID_FRA' : 'RS'},
# 				 'Payment__c' : {'CN_OWN' : 'R', 'CN_FRA' : 'R', 'RU_OWN' : 'R', 'ID_FRA' : 'R'},
# 				 'Apttus_Proposal__Proposal__c' : {'CN_OWN' : 'R', 'CN_FRA' : 'R', 'RU_OWN' : 'R', 'ID_FRA' : 'R'},
# 				 'B25__Reservation__c' : {'CN_OWN' : 'RS', 'CN_FRA' : 'RS', 'RU_OWN' : 'RS', 'ID_FRA' : 'RS'},
# 				 'B25__Resource__c' : {'CN_OWN' : 'RS', 'CN_FRA' : 'RS', 'RU_OWN' : 'RS', 'ID_FRA' : 'RS'},
# 				 'B25__Staff__c' : {'CN_OWN' : 'RS', 'CN_FRA' : 'RS', 'RU_OWN' : 'RS', 'ID_FRA' : 'RS'},
# 				 'Usage__c' : {'CN_OWN' : 'R', 'CN_FRA' : 'R', 'RU_OWN' : 'R', 'ID_FRA' : 'R'}}
dictObj2Group = {'News__c' : {'CN_OWN' : 'R', 'CN_FRA' : 'R', 'RU_OWN' : 'R', 'ID_FRA' : 'R'}}

# dictObjAcc = {'Lead' : {'CN_OWN' : 'Read', 'CN_FRA' : 'Read', 'RU_OWN' : 'Read', 'ID_FRA' : 'Read'},
# 			  'Account' : {'CN_OWN' : 'Read', 'CN_FRA' : 'Read', 'RU_OWN' : 'Read', 'ID_FRA' : 'Read'},
# 			  'Opportunity' : {'CN_OWN' : 'Read', 'CN_FRA' : 'Read', 'RU_OWN' : 'Read', 'ID_FRA' : 'Read'},
# 			  'Campaign' : {'CN_OWN' : 'Edit', 'CN_FRA' : 'Edit', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'},
# 			  'Apttus_Config2__AssetLineItem__c' : {'CN_OWN' : 'Edit', 'CN_FRA' : 'Edit', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'},
# 			  'B25__Availability__c' : {'CN_OWN' : 'Read', 'CN_FRA' : 'Read', 'RU_OWN' : 'Read', 'ID_FRA' : 'Read'},
# 			  'B25__Group__c' : {'CN_OWN' : 'Edit', 'CN_FRA' : 'Edit', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'},
# 			  'B25__Group_Membership__c' : {'CN_OWN' : 'Edit', 'CN_FRA' : 'Edit', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'},
# 			  'Apttus_Config2__Order__c' : {'CN_OWN' : 'Edit', 'CN_FRA' : 'Edit', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'},
# 			  'Payment__c' : {'CN_OWN' : 'Edit', 'CN_FRA' : 'Edit', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'},
# 			  'Apttus_Proposal__Proposal__c' : {'CN_OWN' : 'Edit', 'CN_FRA' : 'Edit', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'},
# 			  'B25__Reservation__c' : {'CN_OWN' : 'Edit', 'CN_FRA' : 'Edit', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'},
# 			  'B25__Resource__c' : {'CN_OWN' : 'Read', 'CN_FRA' : 'Read', 'RU_OWN' : 'Read', 'ID_FRA' : 'Read'},
# 			  'B25__Staff__c' : {'CN_OWN' : 'Edit', 'CN_FRA' : 'Edit', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'},
# 			  'Usage__c' : {'CN_OWN' : 'Read', 'CN_FRA' : 'Read', 'RU_OWN' : 'Read', 'ID_FRA' : 'Read'}}
dictObjAcc = {'News__c' : {'CN_OWN' : 'Edit', 'CN_FRA' : 'Edit', 'RU_OWN' : 'Edit', 'ID_FRA' : 'Edit'}}

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
# dictObjContentTemplate = {'Lead' : leadContentTemplate,
# 						  'Account' : accountContentTemplate,
# 						  'Opportunity' : leadContentTemplate,
# 						  'Campaign' : leadContentTemplate,
# 						  'Apttus_Config2__AssetLineItem__c' : leadContentTemplate,
# 						  'B25__Availability__c' : leadContentTemplate,
# 						  'B25__Group__c' : leadContentTemplate,
# 						  'B25__Group_Membership__c' : leadContentTemplate,
# 						  'Apttus_Config2__Order__c' : leadContentTemplate,
# 						  'Payment__c' : leadContentTemplate,
# 						  'Apttus_Proposal__Proposal__c' : leadContentTemplate,
# 						  'B25__Reservation__c' : leadContentTemplate,
# 						  'B25__Resource__c' : leadContentTemplate,
# 						  'B25__Staff__c' : leadContentTemplate,
# 						  'Usage__c' : leadContentTemplate}
dictObjContentTemplate = {'News__c' : leadContentTemplate}

for obj in dictObjContentTemplate.keys():
	packageContent = '<?xml version="1.0" encoding="UTF-8"?>\n\
	<Package xmlns="http://soap.sforce.com/2006/04/metadata">\n\
	    <types>'

	content = '<?xml version="1.0" encoding="UTF-8"?>\n<SharingRules xmlns="http://soap.sforce.com/2006/04/metadata">'
	for center in dictCenters.keys():
		content += dictObjContentTemplate[obj].format(bu, dictObj2Group[obj][bu], center, dictObjAcc[obj][bu],
			dictCenters[center])
		packageContent += '\n		<members>' + obj + '.' + bu + '_' + dictObj2Group[obj][bu] + '_' + center + '</members>'
	content += '\n</SharingRules>'
	filepath = "C:/3 - Study/Python/AddSharingRules/" + obj + "/src/sharingRules/" + obj + ".sharingRules"
	f = open(filepath,"w+")
	f.write(content)
	f.close()

	packageContent += '\n\
        <name>SharingOwnerRule</name>\n\
    </types>\n\
    <version>40.0</version>\n\
</Package>'
	packagePath = "C:/3 - Study/Python/AddSharingRules/" + obj + "/src/package.xml"
	f = open(packagePath, "w+")
	f.write(packageContent)
	f.close()