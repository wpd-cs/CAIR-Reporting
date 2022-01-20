# -*- coding: utf-8 -*-
"""

William Duong
Project started: January 19, 2023
wpduong@gmail.com

Last Updated: 01/19/22

"""

from sys import exit
from multiprocessing import Process
import datetime
import csv
import os



class Patient:
	def __init__ (self, cwid, lot = "", employee = "", student = "", status = ""):
		"""Initialize class data members"""
		self.__cwid = cwid
		self.__lot = lot
		self.__employee = employee
		self.__student = student
		self.__status = status

	def getCwid(self):
		"""Get CWID"""
		return self.__cwid

	def get/lot(self):
		"""Get status"""
		return self.__lot

	def getEmployee(self):
		"""Get status"""
		return self.__employee

	def getStudent(self):
		"""Get status"""
		return self.__student

	def getStatus(self):
		"""Get status"""
		return self.__status

	def setStatus(self, status):
		"""Set status"""
		self.__status = status



def readCairReport(group):
	"""Read in CAIR Report"""

	with open("sample.txt", "r") as f:
		temp = f.readline()
		del temp

		for line in f:
			myLine = line.split(',')

			if myLine[4] == '""' and myLine[7] == '"True"':
				patient = Patient(myLine[0], myLine[4], myLine[7], myLine[8])
				group["cairPop"].append(patient)



def readCompliance(group):
	"""Read in Compliance Report"""

	with open("compliance.txt", "r") as f:
		temp = f.readline()
		del temp

		for line in f:
			myLine = line.split(',')

			patient = {myLine[3]: myLine[7]}

			group["clearancePop"].append(patient)



def converge(group):
	"""Merge CAIR and Clearance dictionaries"""

	for patient in group["cairPop"]:
		cwid = patient.getCwid()
		if group["clearancePop"].has_key(cwid):
			patient.setStatus(group["clearancePop"][cwid])



def createEmployeeList(group):
	"""Output list of Non-CAIR employees"""
	pass


			
	


def concurrent(*functions):
	proc = []
	for fn in functions:
		p = Process(target=fn)
		p.start()
		proc.append(p)
	for p in proc:
		p.join()



group = {"cairPop": [], "clearancePop": {}, "mergePop": []}



if __name__ == "__main__":
	"""Main function"""

	# Initialize variables

	concurrent()
	
	# Get current time
	d = datetime.datetime.now()
	e = d.strftime("%m-%d-%y %H%M%S %p")

	# Get today's date
	t = d.strftime("%b-%d-%Y")

	# Create folder
	parent_dir = os.getcwd()
	path = os.path.join(parent_dir, e)
	os.mkdir(path)

	concurrent()