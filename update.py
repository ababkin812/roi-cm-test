import yaml
import os
import xml.etree.ElementTree as xml

f = open('properties.yaml','r')
version_list = yaml.load(f)
f.close()

#print(r);
curr_dir_list = os.listdir("./")
#print(curr_dir_list)
pom_list=[]
for dir_list in curr_dir_list:
    if os.path.isdir(dir_list) and os.path.isfile(dir_list+"/pom.xml"):
        pom_list.append(dir_list+"/pom.xml")
#print(pom_list)

for pom in pom_list:
    xml.register_namespace("","http://maven.apache.org/POM/4.0.0")
    xml_doc = xml.parse(pom)
    name = xml_doc.find("{http://maven.apache.org/POM/4.0.0}"+"artifactId").text
    #print(name)
    if name in version_list:
        version = xml_doc.find("{http://maven.apache.org/POM/4.0.0}"+"version")
        version.text = version_list[name]
        xml_doc.write(pom)