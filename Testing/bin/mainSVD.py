#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys, os, datetime
from Matrix import Matrix

def main():
	svd_dimension = 250
	temp_folder = '../'
	input_file = temp_folder+'TestData.txt'
	svd_dimension = 2
	matrix_relation = Matrix(input_file, temp_folder, svd_dimension)		
	del matrix_relation

if __name__ == "__main__":
   main()

