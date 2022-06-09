# Double-Leg Quiet Stance
# Analysis of raw Force Plate Data - 30sec. @ 1,000Hz

# Import libraries that may be needed
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



df = pd.read_csv("E:/Biomechanics/Force Plate - Signal 1.csv")
#print(df.head())

"""We can assume that this data was collected at 1,000Hz
i.e.(30,000 rows / 30sec. = 1,000Hz)"""

# mm = millimeters

cop_x_mean = df['COP:X'].mean()
#print(cop_x_mean)
"246.54mm"
cop_x_median = df['COP:X'].median()
#print(cop_x_median)
"246.65mm"
cop_x_min = df['COP:X'].min()
#print(cop_x_min)
"198.29mm"
cop_x_max = df['COP:X'].max()
#print(cop_x_max)
"279.88mm"
cop_x_range = (df['COP:X'].max()) - (df['COP:X'].min())
#print(cop_x_range)
"81.59mm"
cop_x_std = df['COP:X'].std()
#print(cop_x_std)
"14.73mm"

# ax = plt.subplot()
# plt.boxplot(df['COP:X'], vert = False)
# ax.set_yticklabels(['30sec.'])
# plt.title('Medial/Lateral COP Data Distribution (mm)')
# plt.show()

cop_y_mean = df['COP:Y'].mean()
#print(cop_y_mean)
"314.43mm"
cop_y_median = df['COP:Y'].median()
#print(cop_y_median)
"316.50mm"
cop_y_min = df['COP:Y'].min()
#print(cop_y_min)
"291.49mm"
cop_y_max = df['COP:Y'].max()
#print(cop_y_max)
"344.69mm"
cop_y_range = (df['COP:Y'].max()) - (df['COP:Y'].min())
#print(cop_y_range)
"53.20mm"
cop_y_std = df['COP:Y'].std()
#print(cop_y_std)
"10.74mm"

# ax = plt.subplot()
# plt.boxplot(df['COP:Y'])
# ax.set_xticklabels(['30sec.'])
# plt.title('Anterior/Posterior COP Data Distribution (mm)')
# plt.show()

# N = Newtons

force_x_mean = df['Force:X'].mean()
#print(force_x_mean)
"2.44N"
force_x_median = df['Force:X'].median()
#print(force_x_median)
"2.65N"
force_x_min = df['Force:X'].min()
#print(force_x_min)
"-8.94N"
force_x_max = df['Force:X'].max()
#print(force_x_max)
"9.70N"
force_x_range = (df['Force:X'].max()) - (df['Force:X'].min())
#print(force_x_range)
"18.64N"
force_x_std = df['Force:X'].std()
#print(force_x_std)
"2.70N"

# ax = plt.subplot()
# plt.boxplot(df['Force:X'], vert = False)
# ax.set_yticklabels(['30sec.'])
# plt.title('Medial/Lateral Force Data Distribution (N)')
# plt.show()

force_y_mean = df['Force:Y'].mean()
#print(force_y_mean)
"-4.10N"
force_y_median = df['Force:Y'].median()
#print(force_y_median)
"-4.37N"
force_y_min = df['Force:Y'].min()
#print(force_y_min)
"-15.22N"
force_y_max = df['Force:Y'].max()
#print(force_y_max)
"8.35N"
force_y_range = (df['Force:Y'].max()) - (df['Force:Y'].min())
#print(force_y_range)
"23.58N"
force_y_std = df['Force:Y'].std()
#print(force_y_std)
"4.01N"

# ax = plt.subplot()
# plt.boxplot(df['Force:Y'])
# ax.set_xticklabels(['30sec.'])
# plt.title('Anterior/Posterior Force Data Distribution (N)')
# plt.show()

force_z_mean = df['Force:Z'].mean()
#print(force_z_mean)
"812.44N"
force_z_median = df['Force:Z'].median()
#print(force_z_median)
"812.46N"
force_z_min = df['Force:Z'].min()
#print(force_z_min)
"801.73N"
force_z_max = df['Force:Z'].max()
#print(force_z_max)
"819.14N"
force_Z_range = (df['Force:Z'].max()) - (df['Force:Z'].min())
#print(force_Z_range)
"17.41N"
force_z_std = df['Force:Z'].std()
#print(force_z_std)
"1.66N"

"We will be ignoring the 'Moment' (torque) data for this project"

#-----------------------------------------------------------------------------#
"VISUAL COMPARISON BETWEEN CENTER OF PRESSURE (X,Y) DATA"

"""First we will take a '30-point average' (i.e. average every 30 rows) so
that we can shrink the data from 30,000 to 1,000...which will allow for us to
better see variations over time."""

cop_point_avg = 30
cop_list = []

def point_avg(data):
    data_sum = 0
    count = 0
    for num in data:
        data_sum += num
        count += 1
        if count == cop_point_avg:
            cop_list.append(data_sum / cop_point_avg)
            data_sum = 0
            count = 0
    return cop_list

cop_x_30 = point_avg(df['COP:X'])
#print(cop_x_30)

# ax = plt.subplot()
# plt.plot(cop_x_30, range(len(cop_x_30)))
# plt.xlabel('Medial/Lateral Movement (mm)')
# plt.ylabel('Time')
# plt.title('Center of Pressure M/L Displacement (1000Hz)')
# ax.set_yticks([0.0, (5/30) * float(len(cop_x_30)),
#               (10/30) * float(len(cop_x_30)), (15/30) * float(len(cop_x_30)),
#               (20/30) * float(len(cop_x_30)), (25/30) * float(len(cop_x_30)),
#               (1.0) * float(len(cop_x_30))])
# ax.set_yticklabels(['0sec.', '5sec.', '10sec.', '15sec.', '20sec.', '25sec.',
#                     '30sec.'])
# plt.show()

            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

"Now we will do the same for the y-axis"


cop_y_30 = point_avg(df['COP:Y'])
#print(cop_y_30)

# ax = plt.subplot()
# plt.plot(range(len(cop_y_30)), cop_y_30)
# plt.ylabel('Anterior/Posterior Movement (mm)')
# plt.xlabel('Time')
# plt.title('Center of Pressure A/P Displacement (1000Hz)')
# ax.set_xticks([0.0, (5/30) * float(len(cop_y_30)),
#               (10/30) * float(len(cop_y_30)), (15/30) * float(len(cop_y_30)),
#               (20/30) * float(len(cop_y_30)), (25/30) * float(len(cop_y_30)),
#               (1.0) * float(len(cop_y_30))])
# ax.set_xticklabels(['0sec.', '5sec.', '10sec.', '15sec.', '20sec.', '25sec.',
#                     '30sec.'])
# plt.show()


#-----------------------------------------------------------------------------#
"VISUALIZATION OF FORCE (X,Y,Z) DATA"

"""Due to the nature of the negative(-) numbers in this data set, taking a
30-point average would not give us the most accurate data"""

force_x = df['Force:X']

# ax = plt.subplot()
# plt.plot(force_x, range(len(force_x)))
# plt.xlabel('Medial/Lateral Forces (N)')
# plt.ylabel('Time')
# plt.title('Medial/Lateral Force Production (1,000Hz)')
# ax.set_yticks([0.0, (5/30) * float(len(force_x)),
#               (10/30) * float(len(force_x)), (15/30) * float(len(force_x)),
#               (20/30) * float(len(force_x)), (25/30) * float(len(force_x)),
#                (1.0) * float(len(force_x))])
# ax.set_yticklabels(['0sec.', '5sec.', '10sec.', '15sec.', '20sec.',
#                     '25sec.', '30sec.'])
# plt.show()


            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

force_y = df['Force:Y']

# ax = plt.subplot()
# plt.plot(range(len(force_y)), force_y)
# plt.xlabel('Time')
# plt.ylabel('Anterior/Posterior Forces (N)')
# plt.title('Anterior/Posterior Force Production (1,000Hz)')
# ax.set_xticks([0.0, (5/30) * float(len(force_y)),
#               (10/30) * float(len(force_y)), (15/30) * float(len(force_y)),
#               (20/30) * float(len(force_y)), (25/30) * float(len(force_y)),
#                (1.0) * float(len(force_y))])
# ax.set_xticklabels(['0sec.', '5sec.', '10sec.', '15sec.', '20sec.',
#                     '25sec.', '30sec.'])
# plt.show()

            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

"""When it comes to measuring the Z Force during a quiet stance, it is usually
only useful when performing more complex calculations. But we can use it to
determine the weight of the individual that this data was taken from."""

weight_kg = force_z_mean / 9.81  # 9.81 = Force from gravity
# weight_kg = 82.82kg

weight_lbs = weight_kg * 2.2
# weight_lbs = 182.20lbs.


#-----------------------------------------------------------------------------#

"""Lastly, we will take a look to see if there are any outliers present. We can
use the center of pressure data since they have the largest standard deviations
and ranges (max/min differences). This may be due to the use 'mm' instead of
'cm' for the units of measure, but we will check anyways to be sure. We will
do it manually for this data set but will visualize it with plots/graphs for
Signal 4, which is a larger data set."""


x_upper_limit = cop_x_mean + (3 * cop_x_std)
x_lower_limit = cop_x_mean - (3 * cop_x_std)

#print(x_upper_limit)
# x_upper_limit = 290.74
#print(x_lower_limit)
# x_lower_limit = 202.34

# for i in df['COP:X']:
#     if i > x_upper_limit:
#         print(i)
# This for loop did not return any values, because 'upper_limit' is larger than
# cop_x_max which = 279.88.

# num_lower_outliers = []
# for i in df['COP:X']:
#     if i < x_lower_limit:
#         num_lower_outliers.append(i)
#     print(len(num_lower_outliers))
# According to this there are 277 out of 30,000+ rows with values considered to
# be outliers

            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

y_upper_limit = cop_y_mean + (3 * cop_y_std)
y_lower_limit = cop_y_mean - (3 * cop_y_std)

#print(y_upper_limit)
# 346.65
#print(y_lower_limit)
# 282.20

# Becuase we know that both the max (344.69mm) & min (291.49mm) values for
# df[COP:Y] are both within the upper & lower limits, we already know that
# there are no outliers in this column.
