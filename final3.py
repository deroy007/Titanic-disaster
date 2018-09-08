import pandas as pd
import numpy as np
reader=pd.read_csv("train.csv")
low_memory=False
X_train=[]
y_train=[]
final_x=[]
final_y=[]
tot=0
count=0
avg=0.00
#print reader.index[0]
for index,row in reader.iterrows():
	for i in range(0,12):
		#if i==0:
		#	X_train.append(row[i])
		if i==1:
			final_y.append(row[i])
		elif i==2:
			X_train.append(row[i])
		elif i==4:
			if row[i]=="male":
				X_train.append(1)
			elif row[i]=="female":
				X_train.append(2)
		elif i==5:
			print type(row[i])
			if str(row[i])=="nan":
				X_train.append(avg)
			else:
				tot=tot+row[i]
				count+=1
				avg=tot/count
				X_train.append(row[i])
				
		elif i==6:
			X_train.append(row[i])
		elif i==7:
			X_train.append(row[i])
		elif i==9:
			X_train.append(row[i])
		elif i==11:
			if row[i]=="S":
				X_train.append(1)
			elif row[i]=="C":
				X_train.append(2)
			else:
				X_train.append(3)
			
		
		
	#x_train=np.array(X_train)
	#x_train=x_train.reshape(28,28)	
	final_x.append(X_train)
	#final_y.append(row[0])
	X_train=[]
#for i in range(0,len(final_x)):
	
	#print final_x[i],final_y[i]
final_x_train=np.array(final_x)
#final_x_train=final_x_train.reshape(891,)
final_y_train=np.array(final_y)
from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV
#iris = datasets.load_iris()
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
svc = svm.SVC()
clf = GridSearchCV(svc, parameters)
clf.fit(final_x_train,final_y_train)
X_test=[]
#from sklearn.datasets import make_classification
#clf = LinearSVC()

reader2=pd.read_csv("test.csv")
j=1
fi=open("submission.csv","w")
tot=0
count=0
avg=0
tota=0
counta=0
avga=0
fi.write("PassengerId")
fi.write(",")
fi.write("Survived")
fi.write("\n")
for index,row in reader2.iterrows():
	for i in range(0,11):
		#if i==0:
		#	X_test.append(row[i])
		if i==1:
			X_test.append(row[i])
		elif i==3:
			if row[i]=="male":
				X_test.append(1)
			else:
				X_test.append(2)
		elif i==4:
			#print type(row[i])
			if str(row[i])=="nan":
				X_test.append(avg)
			else:
				tot=tot+row[i]
				count+=1
				avg=tot/count
				X_test.append(row[i])
		elif i==5:
			X_test.append(row[i])
		elif i==6:
			X_test.append(row[i])
		elif i==8:
			if str(row[i])=="nan":
				X_test.append(avg)
			else:
				tota=tota+row[i]
				counta+=1
				avga=tot/count
				X_test.append(row[i])
		elif i==10:
			if row[i]=="S":
				X_test.append(1)
			elif row[i]=="C":
				X_test.append(2)
			elif row[i]=="Q":
				X_test.append(3)
			
		
#	x_test=np.array(X_test)
#	x_test.reshape(1,-1)
	print X_test
	y_predicted=clf.predict([X_test])
	X_test=[]
	print y_predicted[0],count
	fi.write(str(row[0]))
	fi.write(",")
	fi.write(str(y_predicted[0]))
	
	fi.write('\n')
	j=j+1



