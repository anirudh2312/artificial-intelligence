# artificial-intelligence
This is a constraint satisfaction problem which deals with the assignment of pilots to UAVs (unmanned aerial vehicles) and UAVs to field missions under some given constraints. 

Given the set of different missions, UAV models and pilots and some constraints on: mission types, acceptable models for each mission, UAV model control types, acceptable models for each pilot according to their flying skills and preferences, the project aims to solve a CSP to find a mapping of missions, UAV and pilots such that all the mission requests are satisfied without violating any constraint.

The constraints are:
1) Each pilot can perform atmost 3 missions.
2) Each UAV model requires certain flying and control skills, which not every pilot has. So, the pilots should be able to fly their          assigned UAV.
3) Each UAV model has different set of controls and each missions requires some particular sets of controls to be accomplished. So, the      assigned UAV should be able to perform the mission. 
4) Each pilot should be assigned an unique UAV and it should perform all its missions with that UAV.

test.txt file contains the test input to the CSP. It has different types of UAV models, Mission types and their acceptable models, pilot names and the models that they can fly and their preference for particular UAV models. 

output_test.txt file contains the output of the CSP. It represents the following:

mission - UAV model assigned - pilot assigned - Does pilot prefer this assigned UAV model.


