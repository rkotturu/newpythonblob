import json
import glob
print(glob.glob("*.json"))
with open('/Users/nisum/code/ff-config/shoppapp.json') as f:
  data = json.load(f)
version = data['Version']
appcode = data['AppCode']
print (version)
print (appcode)
newfile = appcode,version
f = open((newfile[0]+"_"+newfile[1]+".json").lower(),"w+")
f.close()