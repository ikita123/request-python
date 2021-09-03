import requests
import json
import os
if os.path.isfile("c.json"):
    with open("c.json","r") as s:
        d=json.load(s)
else:
    url=("http://saral.navgurukul.org/api/courses")
    url_1=requests.get(url)
    d=url_1.json()
    with open("c.json","w") as s:
        json.dump(d,s,indent=4)
serial_no=0
for i in range(0,len(d["availableCourses"])):
    print(serial_no,d["availableCourses"][i]["name"],"ID:",d["availableCourses"][i]["id"])
    serial_no+=1
courses_name=int(input("enter your course number which you want to learn   :"))
a=(d["availableCourses"][courses_name-1]["name"])
b=(d["availableCourses"][courses_name-1]["id"])
print((d["availableCourses"][courses_name-1]["name"]))
print(courses_name)
if os.path.isfile("t.json"):
    with open("t.json","r") as t:
        d_1=json.load(t)
else:
    url_2=parents_api='http://saral.navgurukul.org/api/courses/'+str(d["availableCourses"][courses_name-1]["id"])+'/exercises'
    new_data1=requests.get(url_2)
    d_1=new_data1.json()
    with open("t.json","w") as t:
        json.dump(d_1,t,indent=4)
j=0
for i in d_1["data"]:
    print("",j+1,i["name"])
    if d_1["data"][j]["childExercises"]==[]:
        slug=(d_1["data"][j]["slug"])
        print("    ",slug)
    else:
        for k in range(0,len(d_1["data"][j]["childExercises"])):
            a=d_1["data"][j]["childExercises"][k]["name"]
            print("  ",k+1,".",a)
            k=k+1
    j=j+1
topic_no=int(input("choose topic which you want"))
list=[]
k=0
while k<len(d_1["data"][topic_no-1]["childExercises"]):
    print("     ",k+1,d_1["data"][topic_no-1]["childExercises"][k]["name"])
    if os.path.isfile("s.json"):
        with open("s.json","r") as q:
            data_1=json.load(q)
    else:
        url2=("http://saral.navgurukul.org/api/courses/"+str(d["availableCourses"][courses_name-1]["id"])+"/exercise/getBySlug?slug="+(d_1["data"][topic_no-1]["childExercises"][k]["slug"]))
        new_data3=requests.get(url2)
        data_1=new_data3.json()
        with open("s.json","w")as file:
            json.dump(data_1,file,indent=4)
    k=k+1
question_no=int(input("enter a question which you want to print"))
print(data_1["content"])
    

    


