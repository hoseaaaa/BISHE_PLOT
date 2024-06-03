
import matplotlib.pyplot as plt
import numpy as np


# data_1 = [0.138888889, 0.180327869, 0.056338028, 0.0625, 0.152941176, 0.129411765]
# data_2 = [0.163398693, 0.225409836, 0.059303188, 0.083333333, 0.179930796, 0.148749155]


data_1 =[0.793650794,0.925359712,0.072316384,0.661140907,0.518111255,0.146232439]

data_2 =[0.824603175,0.94028777,0.118700565,0.74585568,0.590394567,0.257222222]
# Assuming these are two different categories for the same groups
groups_new = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5', 'Group 6']
x = np.arange(len(groups_new))  # the label locations
width = 0.35  # the width of the bars


fig, ax = plt.subplots()

# Using different opacities for overlapping bars
rects1_overlap = ax.bar(x, data_1, width, label='Category 1', alpha=0.7)
rects2_overlap = ax.bar(x, data_2, width, label='Category 2', alpha=0.5)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Values')
ax.set_title('Overlapped Values by Group and Category')
ax.set_xticks(x)
ax.set_xticklabels(groups_new)
ax.legend()

ax.bar_label(rects1_overlap, padding=3, fmt='%.2f')
ax.bar_label(rects2_overlap, padding=3, fmt='%.2f')

fig.tight_layout()

plt.savefig("xingneng.png")
