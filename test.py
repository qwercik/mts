#!/usr/bin/env python3

import subprocess

APP_BEEING_TESTED_PATH = './r2i.py'
INPUT_FILE_PATH = './tests/input.txt'
OUTPUT_FILE_PATH = './tests/output.txt'

inputFile = open(INPUT_FILE_PATH)
inputData = inputFile.readlines()

outputFile = open(OUTPUT_FILE_PATH)
outputData = outputFile.readlines()

for index, inputLine in enumerate(inputData):
    inputLine = inputLine.strip()
    outputLine = outputData[index].strip()
    
    output = subprocess.check_output(
        APP_BEEING_TESTED_PATH,
        input=inputLine.encode()
    ).strip()
    
    result = output == outputLine

    print('Test nr', index + 1, '-', result)

