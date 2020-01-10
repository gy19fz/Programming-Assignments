
"""
——————version 1.0.0—————————
Welcome to the Deep-sea Fishing
Reading the "Read me!" document before running this model will help you better
understand this model.
@author: FUGANGZHOU
"""
import csv
import agentframework
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.animation
import matplotlib.pyplot
import tkinter
import requests
import bs4

'''Step 1: Initialise parameters'''
neighbourhood = 20
# The number of predators-redfish
a = int(input('Please input the number (an integer) of predators and then press enter.\n(Integers from 5 to 10 are recommended): '))
num_of_redfish = a
# The number of prey-bluefish 
b = int(input('Please input the number (an integer) of prey and then press enter.\n(Integers from 20 to 30 are recommended): '))  
num_of_bluefish = b
num_of_iterations = 50# The number of iterations

# Tell the user how many redfish and bluefish are in the environment that they just have entered.
# Here I changed the colour of the string for the clarity.
print('There are\033[1;35m\n%d redfish \033[0m and\033[1;34m %d bluefish\033[0m\nin the deep-sea！' % (num_of_redfish,num_of_bluefish))

'''Step 2: Initialise GUI main window.'''

root = tkinter.Tk()
root.wm_title("Deep-sea Fishing")

'''Step 3: Get data from the web'''

url = 'https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html'
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_xs = soup.find_all(attrs={"class" : "x"})
td_ys = soup.find_all(attrs={"class" : "y"})
td_zs = soup.find_all(attrs={"class" : "z"})

'''Step 4: Initialize the environment where agents act'''
# The spatial environment is generated from a raster data file.
environment = []
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    parsed_row = row
    rowlist = []				
    for value in parsed_row:				
        rowlist.append(value)
    environment.append(rowlist) 				
f.close()

'''Step 5: Initialise agents'''
# Sometimes Initializing the agent with data on the web can cause problems due to 
# the Internet environment and other factors.
agents = []
redfish = []
'''
for i in range(num_of_bluefish):
    agents.append(agentframework.Agent(environment, agents))
for i in range(num_of_redfish):
    redfish.append(agentframework.Agent(environment, agents))
'''  
for i in range(num_of_bluefish):
    j = i
    while (i > len(td_ys)): 
        j -= len(td_ys)
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)

    agents.append(agentframework.Agent(environment, agents, x, y))
for i in range(num_of_redfish):
    j = i
    while (i > len(td_ys)): 
        j -= len(td_ys)
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)

    redfish.append(agentframework.Agent(environment, agents, x, y))
    
    
'''Step 6: Initialise the GUI'''

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1]) 
carry_on = True
print('A GUI window should appear. Please select\"Start\" from the \"Model\" menu to run the model.") ')

'''Step 7: Animate acting agents'''

def update(frame_number):
    # Updates the display in the animation.
    global carry_on
    # The number of iterations will be printed
    print("Iteration", frame_number)
    # Stop if all bluefish are eaten 
    if len(agents) == 0:
        carry_on = False
        print('All bluefish have been eaten!')
        exiting()    
    fig.clear() 
    # Process bluefish and redfish in a randomish order
    for j in range(num_of_iterations):    
        for each_fish in redfish:
            each_fish.move()
            pos_wolve = each_fish.move()
            #It's dangerous to remove items from an iterator, so I used a slice copy of the list instead.
            for each_agent in agents[:]:
                each_agent.move()
                each_agent.eat()
                each_agent.share_with_neighbourhoods(neighbourhood)
                pos_agent = each_agent.move()
                '''
                If the bluefish has the same coordinates as the redfish, the bluefish will be 
                removed from the bluefish list and it will disappear from the environment.
                That is how bluefish are eat by redfish.
                '''
                if pos_wolve == pos_agent:
                    agents.remove(each_agent)
                    print('A bluefish has been eaten!\033[1;35;46m><((((º>\033[0m')
     
    # plot
    # plot bluefish   
    for each_agent in agents:
        matplotlib.pyplot.scatter(each_agent.x, each_agent.y, s=50., color=(0.,0.,1.0))
    # plot redfish
    for each_wolf in redfish:
        matplotlib.pyplot.scatter(each_wolf.x,each_wolf.y, s=200., color=(0.8,0.,0.))
    # plot environment       
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.ylim(0, 300)
    matplotlib.pyplot.imshow(environment)
    
'''Step 8: A halting function for the animation.'''
def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a<num_of_iterations)&(carry_on):
        yield a
        a = a + 1
    else:
        end()
        print('Select \'start\' to run model again\nClose the GUI window to exit')
        
# Tell the user how many fish were eaten and how many fish left after the iteration ends.        
def end():
    l = len(agents)
    print('\033[1;34m%d bluefish\033[0m have been eaten! There are \033[1;34m %d bluefish\033[0m left!' % ((num_of_bluefish-l),l))
    
# Create animated plot.Continues to update the plot until stopping criteria meets.    
# Display the plot  
def run():
    global animation
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=500,frames=gen_function,repeat=False)
    canvas.draw()

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Start", command=run) 

#The process is quit and destroy the main window.
def exiting():
    print(' \nEnd program!')
    end()
    root.quit()
    root.destroy()
    
root.protocol('WM_DELETE_WINDOW', exiting)
 
tkinter.mainloop()
# I add a fish symbol at the end of the string for beauty.
print('Thank you for running the model!\n\033[1;35;46m`·.¸¸.·´¯`·.¸¸.·´¯`·.¸ ><((((º>\n´¯`·.¸¸.·´¯`·.¸ ><((((((º>     \033[0m')



































