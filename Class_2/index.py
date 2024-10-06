#name: str = "  muhammad"
#age : int = 18
#education : str = " intermediate"
#program : str = " machine learning"
#city : str = " faisalabad"
#id : int =  5000100
#overall_data : str = f"""
#Name of student: {name.lstrip().capitalize()}
#Age of student:{age}
#education of student:{education.lstrip().capitalize()}
#program chosen:{program.lstrip().capitalize()}
#city area:{city.lstrip().capitalize()}
#id number:{id}
#"""
#print(overall_data)


name: str = "  muhammad"
age : int = 18
education : str = " intermediate"
program : str = " machine learning"
city : str = " faisalabad"
id : int =  5000100
overall_data : str = """
Name of student:{}
Age of student:{}
education of student:{}
program chosen:{}
city area:{}
id number:{}
""".format(name,age,education,program,city,id)
print(overall_data)