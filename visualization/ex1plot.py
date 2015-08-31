import matplotlib.pyplot as pypl

whcTop10 = {'Italy': 50, 'China': 47, 'Spain': 44, 'Germany': 39, 'France': 39,  
            'Mexico': 32, 'India': 32, 'UK': 28, 'Russia': 26, 'USA': 22}


nSites = sorted(whcTop10.values(), reverse = True)  # the frequency for y axis
lands = sorted(whcTop10.keys(), key=whcTop10.__getitem__, reverse=True)     # the list of all top 10 lands
landAsX = range (10)   # the x locations for the groups

""" plot the bar chart """
bars = pypl.bar (landAsX, nSites)

        # set lands names as labels on X axis
pypl.xticks(landAsX, lands, rotation=20)   # label rotation is optional
        # add some space between bars and axes  
pypl.xlim([min(landAsX) - 0.3, max(landAsX) + 1])   # x axis
pypl.ylim([0, max(nSites) + 3])   # y axis
        # let's add a grid on y-axis
pypl.grid(True, axis='y')

         # add a red dashed line for the mean
nSitesMean = 35
pypl.hlines(nSitesMean, -0.3, 10, color='red', linestyles='dashed', label = '$\mu (top10) $')
#pypl.legend()    # display label for mean line into a legend

pypl.text(7, 36, '$\mu=35 $', color='red')

""" define the plot labels """
pypl.title('Distribution of the WHC sites by land - Top 10', fontsize=18)
pypl.ylabel('Number of WHC sites') 

         # change colour of single bars (the very first) and annotate it
bars[0].set_color('green')
pypl.annotate('Country with largest number of WHC sites', xy=(0.5,50), xytext=(2,49),
                arrowprops=dict(facecolor='green', shrink=0.2), color='green')

pypl.show()
