'''
Name   : Ashwin Sai C
Course : NLP - CS6320-001
Title  : Homework 2: Ngram Language Model : Notebook 2
Term   : Spring 2024

'''

import os
import nltk
from   nltk.util import ngrams
import pickle
import math


def load_pickle(filename):
	'''
		parameters  : filename 
		Description : This function is used to read the given filename using pickle and return the file data

		return      : data 
	'''

	file_handle = open(filename,"rb")
	data        = pickle.load(file_handle)
	file_handle.close()

	return data

def Read_File_Data(filename):
	'''
		parameters  : filename 
		Description : This function is used to read the given filename and return the file data

		return      : data 
	'''

	file_handle = open(filename,'r')
	data        = file_handle.readlines()
	file_handle.close()

	return data

def Calculate_Probabilty(line, unigram_dict, bigram_dict, v):
	'''
		parameters  : test data, unigram, bigrams and v 
		Description : This function is used to calculate the probablity whether the test data is English, French or Italian.

		return      : probability of the test data w.r.t language
	'''


	unigram_list = nltk.word_tokenize(line)
	bigram_list  = list(ngrams(unigram_list,2))
	line_proba   = 1

	for bigram in bigram_list:
		if bigram in list(bigram_dict.keys()):
			b = bigram_dict[bigram]
		else:
			b = 0

		if bigram[0] in list(unigram_dict.keys()):
			u = unigram_dict[bigram[0]]
		else:
			u = 0

		line_proba = line_proba * ((b + 1)/(u + v))                    # with laplace smoothing

	return line_proba

def Compare_Probabilities(Eng_proba, Fre_proba, Ita_proba):
	'''
		parameters  : English, French and Italian probabilities 
		Description : This function is used to calculate the maximum probability of the 3 languages.

		return      : Language name 
	'''

	if Eng_proba >= Fre_proba and Eng_proba >= Ita_proba:
		return "English"
	elif Fre_proba >= Eng_proba and Fre_proba >= Ita_proba:
		return "French"
	else:
		return "Italian"

	return "NA"

def Predict_Language(data, v, English_Bigram_data, English_Unigram_data, French_Bigram_data, French_Unigram_data, Italian_Bigram_data, Italian_Unigram_data):
	'''
		parameters  : test data, v, all ngrams dict 
		Description : This function is used to calculate the max probability and store the result in a list

		return      : Output list of predictions
	'''

	Result_list = []

	for index, line in enumerate(data):
		temp_line = line.replace("\n","")

		proba_English = Calculate_Probabilty(temp_line, English_Unigram_data, English_Bigram_data, v)
		proba_French  = Calculate_Probabilty(temp_line, French_Unigram_data, French_Bigram_data, v)
		proba_Italian = Calculate_Probabilty(temp_line, Italian_Unigram_data, Italian_Bigram_data, v)

		# print("Probablity of English : ",proba_English)
		# print("Probablity of French  : ",proba_French)
		# print("Probablity of Italian : ",proba_Italian)
		# print("\n")
		result = Compare_Probabilities(proba_English, proba_French, proba_Italian)
		#print(index+1," ",result)
		Result_list.append(result)
	
	return Result_list	

def Write_Result(Result_list):
	'''
		parameters  : prediction list 
		Description : This function is used to write the given filename and test data

		return      : None
	'''

	file_handle = open("AlgorithmResult.txt","w")
	for index, lang in enumerate(Result_list):
		file_handle.write(str(index+1)+" "+lang+"\n")

	file_handle.close()

def Calculate_Accuracy(Result_list):
	'''
		parameters  : prediction list 
		Description : This function is used to calculate the accuracy of the predicted list with the expected list.

		return      : accuracy
	'''

	file_handle  = open("LangId.sol.txt","r")
	data         = file_handle.readlines()
	file_handle.close()
	actual_list  = []
	correct_pred = 0
	accuracy     = 0

	for line in data:
		actual_list.append(line.replace("\n","").split(" ")[-1])

	if len(actual_list) != len(Result_list):
		print("Number of Predictions is not the same.")		
	
	else:
		for index, value in enumerate(actual_list):
			if value.lower() == Result_list[index].lower():
				correct_pred += 1
				# print("Correct")
			else:
				print("Index : ",index," Actual : ",value.lower()," Predicted : ",Result_list[index].lower())

		accuracy = (correct_pred / len(actual_list)) * 100

	return accuracy

def load_data_Pickle():
	'''
		parameters  : None 
		Description : This function is used to load the pickle data

		return      : pickle ngrams data 
	'''
	English_Bigram_data  = load_pickle("English_Bigrams.pickle")
	English_Unigram_data = load_pickle("English_Unigrams.pickle")
	French_Bigram_data   = load_pickle("French_Bigrams.pickle")
	French_Unigram_data  = load_pickle("French_Unigrams.pickle")
	Italian_Bigram_data  = load_pickle("Italian_Bigrams.pickle")
	Italian_Unigram_data = load_pickle("Italian_Unigrams.pickle")

	return English_Bigram_data, English_Unigram_data, French_Bigram_data, French_Unigram_data, Italian_Bigram_data, Italian_Unigram_data

def Initiae_Prediction():
	'''
		parameters  : None 
		Description : This function is used to initiate the program

		return      : None 
	'''

	test_file_name       = "LangId.test.txt"

	English_Bigram_data, English_Unigram_data, French_Bigram_data, French_Unigram_data, Italian_Bigram_data, Italian_Unigram_data = load_data_Pickle()	

	data                 = Read_File_Data(test_file_name)
	v                    = len(English_Unigram_data) + len(French_Unigram_data) + len(Italian_Unigram_data)

	Result_List          = Predict_Language(data, v, English_Bigram_data, English_Unigram_data, French_Bigram_data, French_Unigram_data, Italian_Bigram_data, Italian_Unigram_data)
	Write_Result(Result_List)
	accuracy             = Calculate_Accuracy(Result_List)
	print("Accuracy : ",round(accuracy,2),"% ")


if __name__ == "__main__":
	print("Hi")

	'''
		parameters  : None 
		Description : This function is the main function

		return      : None 
	'''
	Initiae_Prediction()