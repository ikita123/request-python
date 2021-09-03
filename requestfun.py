import requests
import json
def request():
    url=requests.get("http://saral.navgurukul.org/api/courses")
    new_data=url.json()
    b=open("courses.json","w")
    c=json.dump(new_data,b,indent=4)
    def courses():
        serial_no=0
        for i in range(0,len(new_data["availableCourses"])):
            print(serial_no,new_data["availableCourses"][i]["name"],"ID:",new_data["availableCourses"][i]["id"])
            serial_no+=1
    courses()
    courses_name=int(input("enter your course number which you want to learn   :"))
    print(new_data["availableCourses"][courses_name-1]["name"])
    print(courses_name)
    user_input=input("if you want to previous oe next p/n")
    if user_input=="p":
        serial_no=0
        for i in range(0,len(new_data["availableCourses"])):
            print(serial_no,new_data["availableCourses"][i]["name"],new_data["availableCourses"][i]["id"])
            serial_no+=1
    courses_name=int(input("enter your course which you want to learn"))
    print(new_data["availableCourses"][courses_name-1]["name"])
    url_1=parents_api='http://saral.navgurukul.org/api/courses/'+str(new_data["availableCourses"][courses_name-1]["id"])+'/exercises'
    new_data1=requests.get(url_1)
    d=new_data1.json()
    e=open("parents.json","w")
    f=json.dump(d,e,indent=4)
    def parents():
            j=0
            for i in d["data"]:
                print("",j+1,i["name"])
                if d["data"][j]["childExercises"]==[]:
                    slug=(d["data"][j]["slug"])
                    print("    ",slug)
                else:
                    for k in range(0,len(d["data"][j]["childExercises"])):
                        a=d["data"][j]["childExercises"][k]["name"]
                        print("  ",k+1,".",a)
                        k=k+1
                j=j+1
    parents()
    topic_no=int(input("choose topic which you want"))
    print(d["data"][topic_no-1]["name"])
    list=[]
    b=input("if you to go previous or next p/n    :")
    if b=="p":
        u=0
        for i in d["data"]:
            print("",u+1,i["name"])
            if d["data"][u]["childExercises"]==[]:
                slug=i["slug"]
                print("    ",slug)
            else:
                for v in range(0,len(d["data"][u]["childExercises"])):
                    a=d["data"][u]["childExercises"][v]["name"]
                    print("  ",v+1,".",a)
            u=u+1
            topic_no1=int(input("choose topic which you want"))
            print(d["data"][topic_no1-1]["name"])
    else:
        for n in range(0,len(d["data"][topic_no-1]["childExercises"])):
            print("     ",n+1,d["data"][topic_no-1]["childExercises"][n]["name"])
            url2=("http://saral.navgurukul.org/api/courses/"+str(new_data["availableCourses"][courses_name-1]["id"])+"/exercise/getBySlug?slug="+(d["data"][topic_no-1]["childExercises"][n]["slug"]))
            new_data3=requests.get(url2)
            data_1=new_data3.json()
            with open("child.json","w")as file:
                json.dump(data_1,file,indent=4)
                list.append(data_1["content"])
    def question():
        question_no=int(input("enter a question number which you want"))-1
        print(list[question_no])
        while question_no>=0:
            previous_next=input("enter where you want to go privious or next")
            if previous_next=="p":
                question_no-=1
                print(list[question_no])
            elif previous_next=="n":
                if question_no==len(list)-1:
                    print("no more question")  
                    break
                question_no+=1
                print(list[question_no])
            else:
                print("invalid")
        else:
            print("no more")
    question()
request()



        


