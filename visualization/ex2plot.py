import matplotlib.pyplot as pypl

whcTop10 = {'Italy': 50, 'China': 47, 'Spain': 44, 'Germany': 39, 'France': 39,  
            'Mexico': 32, 'India': 32, 'UK': 28, 'Russia': 26, 'USA': 22}


nSites = sorted(whcTop10.values(), reverse = True)  # the frequency for y axis
lands = sorted(whcTop10.keys(), key=whcTop10.__getitem__, reverse=True)     # the list of all top 10 lands
landAsX = range (10)   # the x locations for the groups

""" plot the bar chart """
pypl.barh (landAsX, nSites)

pypl.yticks(landAsX, lands, rotation=20)           # label rotation is optional


pypl.ylim([min(landAsX) - 0.3, max(landAsX) + 1])  # x axis gets more space at the extremes
pypl.xlim([0, max(nSites) + 3])                                    # y axis starts at 0, has some space on top

   # let's add a grid on y-axis
pypl.grid(True, axis='x')

pypl.title('Distribution of the WHC sites by land - Top 10', fontsize=18)  # chart title
pypl.xlabel('Number of WHC sites')             # y axis title


pypl.show()
