# -*- coding:UTF8 -*-

import os 
import re
import sys

filePath = sys.argv[1]
# filePath = '/Users/smb-lsp/Desktop/Switch/trunk_ezlive_switch/ios/EZViewer/Classes/ViewController/UVCloudLoginViewController.m'
fileName = os.path.basename(filePath).split('.')[0]
print('fileName: ' + fileName + '\n')

file = open(filePath, 'r+')
fileContent = file.read()
file.close()
pattern = re.compile('(?<=#import ")([^"]*)')   # 查找数字
result = pattern.findall(fileContent)

unusedHeaderList = []
def commentHeader(headerName):
    pattern = re.compile(r'#import ?\"' + headerName + '\"')   
    result = pattern.findall(fileContent)
    for headerImport in result:
        replacement = '//' + headerImport
        newFileContent = fileContent.replace(headerImport, replacement)
        file = open(filePath, 'w')
        file.write(newFileContent)
        file.close()
        if compileWithoutPrefixHeader() == 0:
            unusedHeaderList.append(headerName)
        file = open(filePath, 'w')
        file.write(fileContent)
        file.close()

def compileWithoutPrefixHeader():
    compileResult = os.system('sh /Users/smb-lsp/Desktop/组件化/PCH/CompileAndCheck/compileWithoutPrefixHeader.sh  ' + filePath)
    return compileResult

for headerName in result:
    if fileName in headerName :
        continue
    commentHeader(headerName)


print('unused header list:\n')
print(unusedHeaderList)
