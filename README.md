# Programming-Assignments
DEEP-SEA FISHING		
---------Hypothetical Scenario----------
This model is about a hypothetical scenario called 'Deep-sea fishing'.
The scenario is that fish live in the deep sea without light don’t have the visual ability.
All of the fish just move arbitrarily in the deep sea, and the predators will not chase their prey purposefully, but eat the food that accidentally swims to their mouth.
----------------------------------------------

-----------Agents Introduction-----------
There are two kinds of agents(fish) in this model, the first one is called ‘Redfish’ which is the predator and they will eat the prey around them, ‘Bluefish’. They both live in the deep sea which is presented by raster data, and the bluefish will and only eat the seaweed where they pass, redfish only eat bluefish.

Redfish is presented by a big red spot, and bluefish are presented by a smaller blue spot.
The area where seaweed is eaten by bluefish will become darker, bluefish will disappear(be eaten) if they have the same coordinate position with redfish.
-----------------------------------------------

--------------Problems you may encounter and resolution--------------
There are still some shortcomings of this program and you may have problems at runtime, here are some guidelines could help with:

0.Before you run this model in spider please set the backend to ‘TKinter’.
Tools → Preference C IPyython console → Graphics → Backend:TKinter 
 
1.When you press the ‘Run’ button, A GUI window and a figure window should appear the same time, please ignore the figure window(the best way is to minimize this window) and select ‘Start’ from the ‘Model’ menu in the upper left corner of the GUI window to run the model.

2.Sometimes when you try closing the figure window Spyder could be crashed, please restart Spyder in this case.

3.If you want to run the program multiple times, it would be better to select ‘start’ from the ‘Model’ menu again rather than close the GUI window and click the ‘Run’ button. 
----------------------------------------------------------------------------------

Appreciate for everyone who may read this document and run this model.

@author: FugangZhou    ´¯`·.¸¸.·´¯`·.¸ ><((((((º>
`·.¸¸.·´¯`·.¸¸.·´¯`·.¸ ><((((º>
