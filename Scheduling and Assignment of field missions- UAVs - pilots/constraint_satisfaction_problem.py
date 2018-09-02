from constraint import *

p = Problem()
fp = open('test.txt', 'r')
file = open("output_test.txt", "w")

models = []
mission_type = {}
pilot_names = []
pilot_ability = []
pilot_pref = {}
missions = []
nuas = []
pilot_skills = []
mission_compatibility = []

lines = fp.readlines()
parse = []

for line in lines:
    parse.append(line.split())

# parsing the input file
for i in range(len(parse)):
    if(parse[i] != []):
        if(parse[i][0] == str('MT')):
            mission_type[parse[i][1]] = parse[i][2]
        elif (parse[i][0] == 'P'):
            pilot_names.append(parse[i][1])
            pilot_ability.append(parse[i][2])
            pilot_pref[parse[i][1]] = (parse[i][3])
        elif (parse[i][0] == 'NUAS'):
            number = parse[i][1]
        elif (parse[i][0] == 'M'):
            missions.append(parse[i][2])
        else:
            models.append(parse[i][0])

for i in range(len(models)):
    nuas.append(number[i])

# Condition for the failure of problem satisfaction (each pilot can go on maximum of 3 missions)
if((len(pilot_names))*3) < len(missions):
    file.write('No mapping can be satisfied because of insufficient number of pilots since each pilot can perform maximum of 3 missions. The maximum missions that can be performed are : ' + str((len(pilot_names))*3))
    fp.close()
    exit()

# mission model compatibility (each mission can be performed by a particular set of aircraft models)
mission_model_comp = {}
for key in mission_type:
    list2 = []
    value = mission_type[key]
    for i in range(len(models)):
        if(value[i]=='1'):
            for j in range(int(nuas[i])):
                list2.append(models[i]+'_'+str(j))
    mission_model_comp[key] = list2

# set of all models including their instances
modelset = []
for i in range(len(nuas)):
    for j in range(int(nuas[i])):
        modelset.append(models[i] + '_' + str(j))

# pilot skills to fly the uas
for i in range(len(pilot_ability)):
    uas_model = []
    for j in range(len(models)):
        if (pilot_ability[i][j] == '1'):
            for k in range(int(nuas[j])):
                uav = models[j] + '_' + str(k)
                uas_model.append(uav)
    pilot_skills.append(uas_model)

pilots = {}
for i in range(len(pilot_skills)):
    pilots[pilot_names[i]] = pilot_skills[i]

def expression1(uas, pilot):
    for k in pilots[pilot]:
        if(k==uas):
            return 1
    return 0


def expression2(uas, mission):
    for k in mission_model_comp[missions[mission]]:
        if(k==uas):
            return 1
    return 0

def func(pilot_i, pilot_j, uas_i, uas_j):
    if(pilot_i==pilot_j):
        return (uas_i == uas_j)
    elif(pilot_i!=pilot_j):
        return (uas_i != uas_j)
    else:
        return False

# problem variables and domains
for i in range(len(missions)):
    p.addVariable("suas"+str(i), modelset)
    p.addVariable("pilot"+str(i), (pilot_names))
    p.addVariable("mission"+str(i), [i])

# problem constraints

# each pilot can perform atmost 3 missions
for i in pilot_names:
    p.addConstraint(SomeNotInSetConstraint([i], len(missions)-3), ["pilot" + str(j) for j in range(len(missions))])

# pilot should be able to fly the assigned uas
for i in range(len(missions)):
    p.addConstraint(lambda uas, pilot: expression1(uas, pilot)==1, ("suas%d" % i, "pilot%d" % i))

# assigned uas should be able to perform the mission
for i in range(len(missions)):
    p.addConstraint(lambda uas, mission: expression2(uas, mission)==1, ("suas%d" % i, "mission%d" % i))

# each pilot should be assigned an unique uas and it should perform all its missions with that uas
for i in range(len(missions)):
    for j in range(i+1, len(missions)):
        p.addConstraint(lambda pilot_i, pilot_j, uas_i, uas_j: func(pilot_i, pilot_j, uas_i, uas_j), ("pilot"+str(i), "pilot"+str(j), "suas"+str(i), "suas"+str(j)))


modelnumber = {}
n = 0
for m in models:
    modelnumber[m] = n
    n=n+1

# getting the solution of the problem
ans = p.getSolution()

if((int(len(ans)/3)) != len(missions)):
    file.write('The complete mapping for all the missions is not found')
else:
    for j in range(len(missions)):
        m_no = modelnumber[ans["suas%d"%j].split('_')[0]]
        if(pilot_pref[ans["pilot%d"%j]][m_no] == '1'):
            p = 'Yes'
        else:
            p = 'No'
        a = ans["mission%d"%j] + 1
        file.write('M'+str(a)+ ' '+ str(ans["suas%d"%j].split('_')[0])+ ' '+ str(ans["pilot%d"%j]) +' '+ p + '\n')

fp.close()
file.close()
