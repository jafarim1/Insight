listDrugCount=0
listDrugName=[]
listDrugNoPres=[]
listDrugTotalCost=[]
listLastName=[[]]
listFirstName=[[]]
drugExistIndex=0

def checkHistory(reqDrugName):
	"This Function checks to see if the drug is prescribed before"
	global listDrugCount
	global listDrugName
	global listDrugNoPres
	global drugExistIndex
	drugExists=0
	for i_iter in range(0, listDrugCount+1):
		if(reqDrugName==listDrugName[i_iter]):
			drugExistIndex=i_iter
			drugExists=1
	return drugExists,drugExistIndex


def addNewDrug( reqLastName,reqFirstName,reqDrugName,valueReqDrugCost ):
	"This Function adds a new drug to the list of saved drugs"
	global listDrugCount
	global listDrugName
	global listDrugNoPres
	global listDrugTotalCost
	global listLastName
	global listFirstName
	listDrugName.append(reqDrugName)
	listDrugNoPres.append(1)
	listDrugTotalCost.append(valueReqDrugCost)
	listLastName.append([reqLastName])
	listFirstName.append([reqFirstName])
	listDrugCount=listDrugCount+1
	return 
   
def updateDrugList( reqLastName,reqFirstName,reqDrugName,valueReqDrugCost,drugExistIndex ):
	"This Function updates the list"
	global listDrugCount
	global listDrugName
	global listDrugNoPres
	global listDrugTotalCost
	global listLastName
	global listFirstName
	for i_iter in range(0,listDrugNoPres[drugExistIndex]):
		print(reqDrugName)
		if(listDrugNoPres[drugExistIndex]==1):
			if (reqLastName==listLastName[drugExistIndex]):
				if (reqFirstName==listFirstName[drugExistIndex]):
					listDrugTotalCost[drugExistIndex]=listDrugTotalCost[drugExistIndex]+valueReqDrugCost
					return
		else:
			if (reqLastName==listLastName[drugExistIndex][i_iter]):
				if (reqFirstName==listFirstName[drugExistIndex][i_iter]):
					listDrugTotalCost[drugExistIndex]=listDrugTotalCost[drugExistIndex]+valueReqDrugCost
					return

	
	listLastName[drugExistIndex].append(reqLastName)
	listFirstName[drugExistIndex].append(reqFirstName)
	listDrugNoPres[drugExistIndex]+=1
	listDrugTotalCost[drugExistIndex]=listDrugTotalCost[drugExistIndex]+valueReqDrugCost

	return 
#Begining of the code and fetching the header
rawData=open("input/itcont.txt","r")
header=rawData.readline()
#fetching the first Drug no condition
request=rawData.readline()
reqId,reqLastName,reqFirstName,reqDrugName,reqDrugCost=request.split(",")
listDrugName.append(reqDrugName)
listDrugNoPres.append(1)
listLastName[listDrugCount].append(reqLastName)
valueReqDrugCost=float(reqDrugCost);
listDrugTotalCost.append(valueReqDrugCost)
listFirstName[listDrugCount].append(reqFirstName)
endOfFile=0;
while(endOfFile==0):
	request=rawData.readline()
	if request =='':
		print ("End of file reached")
		break
	reqId,reqLastName,reqFirstName,reqDrugName,reqDrugCost=request.split(",")
	valueReqDrugCost=float(reqDrugCost);
	drugExists,drugExistIndex=checkHistory(reqDrugName)
	if drugExists==0 :
		addNewDrug(reqLastName,reqFirstName,reqDrugName,valueReqDrugCost)
	else :
		drugExists=0;
		updateDrugList(reqLastName,reqFirstName,reqDrugName,valueReqDrugCost,drugExistIndex)

print(listDrugName)
print(listDrugNoPres)
print(listDrugTotalCost)

outputFile = open("output/top_cost_drug.txt", "w")
outputStr="drug_name,num_prescriber,total_cost\n"
outputFile.write(outputStr)
for j_iter in range (0,listDrugCount+1):
	outputTotalCost=0;
	outputDrug='aaa'
	outputNoPres=0
	for i_iter in range (0,listDrugCount+1):
		if	listDrugTotalCost[i_iter]>outputTotalCost:
			outputTotalCost=listDrugTotalCost[i_iter]
			outputDrug=listDrugName[i_iter]
			outputNoPres=listDrugNoPres[i_iter]
			outputIndex=i_iter
		elif listDrugTotalCost[i_iter]==outputTotalCost:
			if (listDrugName[i_iter]<outputDrug):
				outputTotalCost=listDrugTotalCost[i_iter]
				outputDrug=listDrugName[i_iter]
				outputNoPres=listDrugNoPres[i_iter]
				outputIndex=i_iter
			
	outputStr="%s,%s,%s\n"%(outputDrug,outputNoPres,outputTotalCost)
	outputFile.write(outputStr)
	listDrugTotalCost[outputIndex]=0;
outputFile.close()

