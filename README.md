# Insight
Sorting Drugs

Definition of the global lists:
In the main python program you will see 6 global list as follow:
listDrugCount=0    Contains the number of unique drugs prescribed 
listDrugName=[]    Name of each drug in the order of the input file
listDrugNoPres=[]  Number of unique prescriber for each drug corresponding to the previous list
listDrugTotalCost=[]  Total cost of each unique drug
listLastName=[[]]  the 2D nested list of the last name prescribing each drug, each element of the 2D list is the list of the last names prescribed that specific drugs, this list gets updated in two case: 1) if there is a new drug: a new list is added the main list. For example if the array has 3 list with different sizes such as listLast Name:[[Smith, Johnson, Peterson],[Williams],[Davis, Taylor]] and a new drug comes in with a prescriber’s last name of “Smith”, the “adddNewDrug” faction adds one list to the end of this list and it would be like: listLast Name:[[Smith, Johnson, Peterson],[Williams],[Davis, Taylor],[Smith]]. 2) if there is a new prescriber for one of the currently registered drugs: At this situation, the “updateDrugList” function, will append one element to the corresponding drug list. So in the case of listLast Name=[[Smith, Johnson, Peterson],[Williams],[Davis, Taylor]] and a prescription of the second drug from a person with last name of “Thomas”, the list will be updated as: listLast Name:[[Smith, Johnson, Peterson],[Williams, Thomas],[Davis, Taylor]].
P.S.
One reason I chose this type of global 2D nested list is that the program can work online without the need of scanning the whole documents and can provide the output even if there is still stream of input data coming in. This is very important and can make decision makings much easier as we are dealing with real-time data in most of the applications with big data analysis. The code is simpler and much easier if we want to just run it as an offline analyzing tool and scan the whole document first to define our array sizes and other specific parameters. I personally think this is less generic and useful. 
listFirstName=[[]]  this is similar to the last name, it only records dynamically the first name of each drug prescribers. 
drugExistIndex=0 the index of the drug that exist in the history and is prescribed again, this is to store redundant drugs and just update the total cost of that drug and/or the first and last name nested list of that drug











Definition of the functions:
The rest of the code is very simple with the above description of global lists. There are three main functions as follow:
checkHistory: This function loop over the entire list of drug names to see if the current drug request has been already registered or not. Then it will return two flags: drugExists and DrugExistIndex which show if the drug exist in the registry (“listDrugCount”) and what’s its index in the registry if so, respectively. 
Depending on the result of the “checkHistory” function, either addNewDrug or updateDrugList functions are called. 
addNewDrug: this function append the entire list of drug registry (“listDrugCount”) with a new drug. The first and last name of the only prescriber, as well as the total cost is updated correspondingly in the global list as follow: 
	listDrugTotalCost.append(intreqDrugCost)
	listLastName.append([reqLastName])
	listFirstName.append([reqFirstName])
The number of prescriber for this new drug is set to be “1” and the “listDrugCount” which keeps track of the number of drugs in the registry is also advanced by one. 

updateDrugList : When this function is called, it means the drug exists in the registry. So, this function first check to see if the current requested prescriber is a new prescriber or not. If the current prescriber already has request the same drug, this function only adds the new costs to the corresponding cost of the drug and returns. However, if the request is from a new prescriber for the already existed drug, this function append the his/her first and last name to the corresponding elements in the global listFirstName and listLastName; increment the number of unique prescriber for this drug and adds the cost to the total cost already archived in the corresponding list(“listDrugTotalCost”).





The main body of the program:
Starting by reading the first line of the file which should be header, the program advances to the second line and store all information’s in the global lists as there hasn’t been any requests before this. These lines initiate all the global lists. Then the program advances to a conditional loop which reads the file line by line until it reaches the end of the file. If the input file is updated online, the loop continuous to work and sort the drugs. As explained before by using the three main function, it simply reads the file line by line and either update the list of the drugs or append to the list if the drug is new. After the end of the file is reach. The program shows the global lists for the unique drug names, their corresponding prescribers and total costs respectively. 

Creating the output file:
With having the global list of unique drugs and their prescriber, this section of the program simply find the maximum total cost and store its corresponding prescribers details in local variables as follow:
outputTotalCost=listDrugTotalCost[i_iter]maximum drug cost
outputDrug=listDrugName[i_iter]nume of the drug with maximum cost
	outputNoPres=listDrugNoPres[i_iter]number of prescriber for that drug
	outputIndex=i_iterthe location of the drug in global lists
 This temporary variable is checked with the entire list of the drugs to make sure it’s the drug with the maximum cost. As requested by the problem, in case of a draw, it compares the drug’s name alphabetically and update these variables with the drug starts with the first letter with lower alphabetical order. 
After checking with the entire list, the drug with maximum cost(minimum alphabetical order) is printed in the file and its corrospoding cost in the “listDrugTotalCost” global list is set to zero so it couldn’t be chosen again. The outer loop goes to the size of the drug name list and then the program closes by closing the file.
