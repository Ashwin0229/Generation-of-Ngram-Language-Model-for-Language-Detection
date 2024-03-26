'''
Name   : Ashwin Sai C
Course : NLP - CS6320-001
Title  : Homework 2: Ngram Language Model : Notebook 1
Term   : Spring 2024

'''

import nltk
from   nltk.util import ngrams
import pickle

def Process_File(filename):
	'''
		parameters  : filename 
		Description : This function is used to read the given filename and return the file data

		return      : data 
	'''

	print("\n-----Filename : ",filename,"-----")
	file_handle = open(filename,"r", encoding="utf8")
	data        = file_handle.readlines()
	file_handle.close()

	return data

def Tokenize_File_Data(data):
	'''
		parameters  : data 
		Description : This function is used to tokenize file data

		return      : tokens list
	'''

	tokens_list   = []

	for line in data:
		temp_line = line.replace("\n","")
		tokenized_line = nltk.word_tokenize(line)
		for token in tokenized_line:
			tokens_list.append(token)


	return tokens_list

def Create_Ngrams_List(tokens_list, n):
	'''
		parameters  : tokens list, n (ngrams generation value) 
		Description : This function is used to generate n grams with the tokens

		return      : ngrams list
	'''

	ngrams_list = []
	ngrams_list = list(ngrams(tokens_list,n))


	return ngrams_list

def Create_Ngram_Dictionary(ngrams_list):
	'''
		parameters  : ngrams list 
		Description : This function is used map the values of the list with their occurence in the text/ngrams list

		return      : a dictionary of {key: count(key)}
	'''

	ngrams_dict = {}
	ngrams_dict = {element : ngrams_list.count(element) for element in set(ngrams_list)}


	return ngrams_dict

def Save_Dict_Pickle(dict_var, name):
	'''
		parameters  : ngrams dictionary, and name of file 
		Description : This function is used to write the ngrams dictionary into a pickle file

		return      : None
	'''

	file_handle = open(name+".pickle", "wb")
	pickle.dump(dict_var, file_handle, protocol=pickle.HIGHEST_PROTOCOL)
	file_handle.close()

	print("Pickle - ",name," saved!")

def Process_ngrams(filename):
	'''
		parameters  : filename 
		Description : This function is used to read the filename, tokenize the file data, create ngrams list and 
					  dictionary.

		return      : bi-gram and uni-gram dictionaries
	'''

	data           = Process_File(filename)
	tokens_list    = Tokenize_File_Data(data)                        #tokens_list by default serves as unigrams
	bigrams_list   = Create_Ngrams_List(tokens_list,2)
	unigrams_list  = Create_Ngrams_List(tokens_list,1)
	bigrams_dict   = Create_Ngram_Dictionary(bigrams_list)
	unigrams_dict  = Create_Ngram_Dictionary(unigrams_list)

	return [bigrams_dict, unigrams_dict]

def Initiate_Ngram():
	'''
		parameters  : None 
		Description : This function is used to initiate the program and save the data dict in pickle.

		return      : None 
	'''

	bigrams_dict_eng, unigrams_dict_eng = Process_ngrams("LangId.train.English.txt")
	bigrams_dict_fre, unigrams_dict_fre = Process_ngrams("LangId.train.French.txt")
	bigrams_dict_ita, unigrams_dict_ita = Process_ngrams("LangId.train.Italian.txt")

	Save_Dict_Pickle(bigrams_dict_eng,  "English_Bigrams")
	Save_Dict_Pickle(unigrams_dict_eng, "English_Unigrams")

	Save_Dict_Pickle(bigrams_dict_fre,  "French_Bigrams")
	Save_Dict_Pickle(unigrams_dict_fre, "French_Unigrams")

	Save_Dict_Pickle(bigrams_dict_ita,  "Italian_Bigrams")
	Save_Dict_Pickle(unigrams_dict_ita, "Italian_Unigrams")


if __name__ == "__main__":
	'''
		parameters  : None 
		Description : This function is main function

		return      : None 
	'''

	print("hi")

	Initiate_Ngram()

	