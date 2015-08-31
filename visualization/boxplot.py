import matplotlib.pyplot as plt
from datascience import stats

agePhysics = [25,31,31,31,31,32,33,34,35,35,35,35,35,36,36,37,37,37,37,37,38,38,38,39,39,
              40,40,40,40,40,41,42,42,42,42,42,42,42,42,43,43,43,43,44,44,44,44,44,44,45,
              45,45,45,45,46,46,46,46,46,46,47,47,47,47,47,47,48,48,48,48,48,49,49,49,49,
              49,49,49,49,50,50,50,50,50,51,51,51,52,52,52,53,53,53,53,53,53,53,53,54,54,
              54,54,54,54,54,55,55,55,55,55,56,56,56,56,56,56,57,57,57,58,58,59,59,59,59,
              59,59,59,60,60,60,60,60,60,60,61,61,61,61,61,62,62,63,63,63,63,63,64,64,64,
              64,64,64,64,65,65,65,66,66,67,67,68,68,68,68,68,68,68,69,70,71,71,71,72,72,
              72,72,73,73,74,75,76,76,76,76,77,77,78,79,79,80,80,81,84,84,85,85,87,87,88]
            
ageLiterature = [42,44,45,46,46,47,48,49,49,50,51,51,52,52,52,52,53,54,54,55,55,55,55,56,
                 56,56,56,56,57,57,57,58,58,58,59,59,59,60,60,60,60,60,60,60,61,61,61,62,
                 62,62,62,63,63,63,63,65,67,67,67,67,68,68,68,68,68,68,69,69,69,69,69,69,
                 70,71,71,71,71,72,72,72,72,73,73,73,73,74,74,74,74,74,75,75,75,76,76,76,
                 77,77,78,78,78,79,79,79,80,80,82,83,85,88]
                 
ageEconomics = [51,53,55,55,56,56,56,56,57,58,58,58,60,60,61,61,61,61,61,61,62,62,62,62,
                63,63,63,63,63,64,64,64,64,65,65,66,66,67,67,67,67,67,67,67,68,68,68,69,
                69,70,70,70,71,71,71,73,73,74,74,74,75,75,75,76,76,77,77,77,78,78,81,82,
                84,89,90]
     
ages=[agePhysics, ageLiterature, ageEconomics]

print(stats.summary(agePhysics))
print("range = ", stats.range(agePhysics))

# basic plot
#plt.boxplot(agePhysics, showmeans=True, whis=99)
box = plt.boxplot(ages, showmeans=True, whis=99)

# add colours
  # physics = green
plt.setp(box['boxes'][0], color='green')
plt.setp(box['caps'][0], color='green')
plt.setp(box['caps'][1], color='green')
plt.setp(box['whiskers'][0], color='green')
plt.setp(box['whiskers'][1], color='green')
  # literature = red
plt.setp(box['boxes'][1], color='red')
plt.setp(box['caps'][2], color='red')
plt.setp(box['caps'][3], color='red')
plt.setp(box['whiskers'][2], color='red')
plt.setp(box['whiskers'][3], color='red')
  # economics = blue (default)

plt.ylim([20, 95])  # y axis gets more space at the extremes
plt.grid(True, axis='y')  # let's add a grid on y-axis
plt.title('Distribution of the Nobel Prize winner ages', fontsize=18)  # chart title
plt.ylabel('Age (years) at winning time')             # y axis title
plt.xticks([1,2,3], ['Physics','Literature','Economics']) # x axis labels


plt.show()