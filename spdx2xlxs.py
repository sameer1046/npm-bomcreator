import sys, os, json, xlwt
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1', cell_overwrite_ok=True)
spdx_json_file = open(sys.argv[1], 'r')
spdx_json = json.load(spdx_json_file)
spdx_json_file.close()
#print(spdx_json)
packages = spdx_json.get('packages')
i = 0
for package in packages:
    sha256 = ""
    checksum = package.get("checksums","")
    if checksum:
        sha256 = checksum[0].get("checksumValue","")
    name = package.get("name")
    version = package.get("versionInfo")
    licenseConcluded = package.get("licenseConcluded","")
    sheet1.write(i, 0, name)
    sheet1.write(i, 1, version)
    sheet1.write(i, 2, sha256)
    sheet1.write(i, 3, licenseConcluded)
    i=i+1
    print(i, sha256, '\n')
wb.save("spdx2xlx.xls")
