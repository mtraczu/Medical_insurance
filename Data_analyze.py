import csv 
# insurance.csv includes columns: age,sex,bmi,children,smoker,region,charges
age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []
#import insurance.csv
with open ("insurance.csv", newline="") as medical_database:
    patients = csv.DictReader(medical_database)
    for row in patients:
        age.append(row['age'])
        sex.append(row['sex'])
        bmi.append(row['bmi'])
        children.append(row['children'])
        smoker.append(row['smoker'])
        region.append(row['region'])
        charges.append(row['charges'])

#DATA CLEANING

#round bmi for two places after comma
rounded_bmi=[]
for num in bmi:
    num = float(num)
    rounded_bmi.append(round(num,2))
#print(bmi)

#round charges for two places after comma
rounded_charges=[]
for num in charges:
    num = float(num)
    rounded_charges.append(round(num,2))
#print(rounded_charges)
    
#First letter in region change to upper
region_upper_first_letter = []
for title in region:
    region_upper_first_letter.append(title.title())
#print(region_upper_first_letter)   

#change children from string to int
children_int = []
for num in children:
    num = int(num)
    children_int.append(num)
  
#change age from string to int
age_int = []
for num in age:
    num = int(num)
    age_int.append(num)
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#FUNCTIONS

#Function below zipping two lists        
def list_zipped(list1,list2): 
    zipped_list = [[x,y] for x,y in zip(list1, list2)]
    return zipped_list


#Function below prints info about selected patient
def all_info_printed(x):
    print("Age: " + str(x[0]))
    print("Sex: " + str(x[1]))
    print("Bmi: " + str(x[2]))
    print("Children: " + str(x[3]))
    print("Smoker: " + str(x[4]))
    print("Region: " + str(x[5]))
    print("Charge: " + str(x[6]))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
#Numbers of male and female patients
number_of_female = sex.count("female")
number_of_male = sex.count("male")
print("\nNumber of female persons: " + str(number_of_female))
print("Number of male persons: " + str(number_of_male) +"\n")

#Average male and female age
sex_age = list_zipped(sex,age_int) 
female_age_total = 0
male_age_total = 0
for x in sex_age:
    if x[0] == "male":
        male_age_total = male_age_total +x[1]
    elif x[0] == "female":
        female_age_total = female_age_total +x[1]

print("Average age for female: " + str(round(female_age_total/number_of_female)))
print("Average age for male: " + str(round(male_age_total/number_of_male)) + "\n")

#Average charge for male and female
sex_charges = list_zipped(sex,rounded_charges)
female_charges_total = 0
male_charges_total = 0

for x in sex_charges:
    if x[0] == "male":
        male_charges_total = male_charges_total +x[1]
    elif x[0] == "female":
        female_charges_total = female_charges_total +x[1]

print("Average charge for female: " + str(round(female_charges_total/number_of_female)))
print("Average charge for male: " + str(round(male_charges_total/number_of_male)) + "\n")

#Quantity of patients in each regions
Southeast_qty = region_upper_first_letter.count("Southeast")
Southwest_qty = region_upper_first_letter.count("Southwest")
Northeast_qty =region_upper_first_letter.count("Northeast")
Northwest_qty = region_upper_first_letter.count("Northwest")
print("Quantity of patients from Southeast: " + str(Southeast_qty))
print("Quantity of patients from Southwest: " + str(Southwest_qty))
print("Quantity of patients from Northeast: " + str(Northeast_qty))
print("Quantity of patients from Northwest: " + str(Northwest_qty) + "\n")

#Average charges in each regions
region_upper_first_letter_rounded_charges = list_zipped(region_upper_first_letter,rounded_charges)
Southeast_charges_total = 0 
Southwest_charges_total = 0
Northeast_charges_total = 0
Northwest_charges_total = 0

for x in region_upper_first_letter_rounded_charges:
    if x[0] == "Southeast":
        Southeast_charges_total = Southeast_charges_total +x[1]
    elif x[0] == "Southwest":
        Southwest_charges_total = Southwest_charges_total +x[1]
    elif x[0] == "Northeast":
        Northeast_charges_total = Northeast_charges_total +x[1]
    elif x[0] == "Northwest":
        Northwest_charges_total = Northwest_charges_total +x[1]

print("Average charge in Southeast: " + str(round(Southeast_charges_total/Southeast_qty)))
print("Average charge in Southwest: " + str(round(Southwest_charges_total/Southwest_qty)))
print("Average charge in Northeast: " + str(round(Northeast_charges_total/Northeast_qty)))
print("Average charge in Northwest: " + str(round(Northwest_charges_total/Northwest_qty)) + "\n")


#how much smokers in each regions
region_upper_first_letter_smoker=list_zipped(region_upper_first_letter,smoker)
smokers_in_Southeast = 0
smokers_in_Southwest = 0
smokers_in_Northeast = 0
smokers_in_Northwest = 0

for x in region_upper_first_letter_smoker:
    if x[0] == "Southeast" and x[1] =="yes":
        smokers_in_Southeast+=1
    elif x[0] == "Southwest"and x[1] =="yes":
        smokers_in_Southwest+=1
    elif x[0] == "Northeast"and x[1] =="yes":
        smokers_in_Northeast+=1
    elif x[0] == "Northwest" and x[1] =="yes":
        smokers_in_Northwest+=1

        
print("Quantity of smokers from Southeast: " + str(smokers_in_Southeast))
print("Quantity of smokers from Southeast: " + str(smokers_in_Southwest))
print("Quantity of smokers from Southeast: " + str(smokers_in_Northeast))
print("Quantity of smokers from Southeast: " + str(smokers_in_Northwest) + "\n")
                                                    
                                                    
# Average BMI in each regions
regions_bmi = list_zipped(region_upper_first_letter, rounded_bmi)

BMI_in_Southeast = 0
BMI_in_Southwest = 0
BMI_in_Northeast = 0
BMI_in_Northwest = 0

for x in regions_bmi:
    if x[0] == "Southeast":
        BMI_in_Southeast+=x[1]
    elif x[0] == "Southwest":
        BMI_in_Southwest+=x[1]
    elif x[0] == "Northeast":
        BMI_in_Northeast+=x[1]
    elif x[0] == "Northwest":
        BMI_in_Northwest+=x[1]
    
print("Average bmi in Southeast: " + str(round(BMI_in_Southeast/Southeast_qty)))
print("Average bmi in Southwest: " + str(round(BMI_in_Southwest/Southwest_qty)))
print("Average bmi in Northeast: " + str(round(BMI_in_Northeast/Northeast_qty)))
print("Average bmi in Northwest: " + str(round(BMI_in_Northwest/Northwest_qty)) + "\n")


Medical_insurance_costs_database = list(zip(age_int,sex,rounded_bmi,children,smoker,region_upper_first_letter,rounded_charges))
#sorting by the biggest charge
Medical_insurance_costs_database.sort(key = lambda x:x [6], reverse = True)
print("The most expensive insurance: ") 
all_info_printed(Medical_insurance_costs_database[0])

#sorting by the lowest charge
Medical_insurance_costs_database.sort(key = lambda x:x [6])
#print(Medical_insurance_costs_database)
print("\nThe cheapest insurance: ") 
all_info_printed(Medical_insurance_costs_database[0])

print("done")

