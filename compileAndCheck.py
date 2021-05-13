# -*- coding:UTF8 -*-

import os 
import re
import sys

# filePath = '/Users/smb-lsp/Desktop/Switch/trunk_ezlive_switch/ios/EZViewer/Classes/ViewController/UVCloudLoginViewController.m'
filePath = sys.argv[1]
fileName = os.path.basename(filePath).split('.')[0]

file = open(filePath, 'r+')
fileContent = file.read()
file.close()
pattern = re.compile(r'(?<=#import ")([^"]*)')   # 查找数字
result = pattern.findall(fileContent)

unusedHeaderList = []
def commentHeader(headerName):
    if '+' in headerName:
        headerName = headerName.replace('+', '\+')
    pattern = re.compile(r'#import ?"' + headerName + r'"')   
    result = pattern.findall(fileContent)
    for headerImport in result:
        replacement = '//' + headerImport
        newFileContent = fileContent.replace(headerImport, replacement)
        file = open(filePath, 'w')
        file.write(newFileContent)
        file.close()
        if compileWithoutPrefixHeader() == 0:
            if '\\' in headerName:
                headerName = headerName.replace('\\', '')
            unusedHeaderList.append(headerName)
        file = open(filePath, 'w')
        file.write(fileContent)
        file.close()

def compileWithoutPrefixHeader():
    compileResult = os.system('sh /Users/smb-lsp/Desktop/组件化/PCH/CompileAndCheck/compileWithoutPrefixHeader.sh  ' + filePath)
    return compileResult

for headerName in result:
    if headerName.split('.')[0] == fileName:
        continue
    print('\n')
    print('Start Compile And Check ' + headerName + '\n')
    commentHeader(headerName)
    print('\n')
    print('*' * 100)


print('unused header list:\n')
print(unusedHeaderList)

