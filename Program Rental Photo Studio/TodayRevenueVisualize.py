import numpy as np 
import matplotlib.pyplot as plt 

#func to return total revenue of each studio
def total_revenue(nameFile):
    with open(nameFile) as k:
        rev_studio = [float(elem) for elem in k]
        total_studio = sum(rev_studio)
        return total_studio

#define variabel for total revenue of each studio
rev1 = round(total_revenue('RevenueMusicRoomStudio.txt'),2)
rev2 = round(total_revenue('RevenueCozyRoomStudio.txt'),2)
rev3 = round(total_revenue('RevenueWhiteScreenStudio.txt'),2)

#define columns and bars
X = ['Music Room Studio','Cozy Room Studio','White Screen Studio']
bars2 = [300,350,400]
bars1 = [rev1,rev2,rev3]
  
#X_axis = np.arange(len(X))
#define bar width and range in x axis
#plt.bar(X_axis - 0.2, bars2, 0.4, label = 'Actual Value')
#plt.bar(X_axis + 0.2, bars1, 0.4, label = 'Target Value')
barWidth1 = 0.076
barWidth2 = 0.040
x_range = np.arange(len(bars1) / 4, step=0.250)

#define x, y, style, and text for each bar
plt.style.use('bmh')
plt.bar(x_range, bars2, color='#acd8eb', width=barWidth1/2, edgecolor='#c3d5e8', label='Target Revenue')
plt.bar(x_range, bars1, color='#ac0e00', width=barWidth2/2, edgecolor='#c3d5e8', label='Actual Revenue')
for i, bar in enumerate(bars1):
    plt.text(i / 4 - 0.015, float(bar) + 1, bar, fontsize=12)
for j,bar in enumerate(bars2):
    plt.text(j / 4 - 0.015, float(bar) + 1, bar, fontsize=18)

plt.xticks(x_range, X)
plt.tick_params(
    bottom=False,
    left=False,
    labelsize=13
)
plt.ylabel("Revenue ($)")
plt.title("Today's Actual Revenue VS Target Revenue", fontsize=14)
plt.rcParams['figure.figsize'] = [30, 10]
plt.axhline(y=0, color='gray')
plt.box(False)
plt.legend()
plt.show()