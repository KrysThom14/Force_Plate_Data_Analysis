# Force-Plate-Data-Analysis-1
This was initially part of an assignment I had from grad school (Exercise Science) in my Biomechanics class. This is just a result of me taking a deeper dive into the analysis of the data using Python. This part of the assignment had to do with analyzing a 30sec. recording of someone performing a Double-Leg Quiet Stance on a Force Plate. The primary measurements in question are Center of Pressure (COP) & Force Data. I have the results of the calculations in each section commented out, as well as the calculations themselves so that I can run one at a time...instead of all at once.


### Quick Glimpse Into What The DF Looks Like
* This is just for reference. I primarily used the csv sheet itself to view the data in full.

![Signal1-1](https://user-images.githubusercontent.com/94875597/172917753-9d7c9201-e8fc-4747-a4cb-5fa69cbc8417.png)


### Calculating Common Aggregates
* The pictures show the calculations for the COP data in the X direction (i.e. Medial/Lateral) and a box plot showing a quick visual summary of the values in that column. This was also done for COP:Y and the forces in the X & Y directions.

![Signal1-2](https://user-images.githubusercontent.com/94875597/172919480-bb1f3a4e-3746-43d9-9e64-4b946012f505.png)

![Signal1-3](https://user-images.githubusercontent.com/94875597/172919496-c18c509a-b14f-4d27-b1b1-ee6e3fd20ab5.png)


### Moving-Point Average
* Only did this because it was part of my original assignment in grad school, and I wanted to see if I could replicate it in python. I created a function that took a 30-point average (i.e. average every 30 rows together) of the COP data and then graphed that. The purpose of this was that it allowed us to better see variations over time. The graph below just shows the data for COP in the anterior/posterior direction.

![Signal1-4-1](https://user-images.githubusercontent.com/94875597/172921505-56a89c95-47a8-48ae-91e4-ad27dda8e9ad.png)

![Signal1-4](https://user-images.githubusercontent.com/94875597/172921538-a3e4bb9d-57f4-4135-99ec-cbe45cdb0a6d.png)

![Signal1-5](https://user-images.githubusercontent.com/94875597/172921555-38cd23a0-b620-4c52-b613-00593e929c94.png)


### Force Data
* This is a visual of the forces in the anterior/posterior direction over time (no moving-point average).

![Signal1-6](https://user-images.githubusercontent.com/94875597/172922381-e5aec0ee-7cff-4898-ad07-16c170cda1c0.png)

![Signal1-7](https://user-images.githubusercontent.com/94875597/172922424-d76ee84f-0cc1-4165-b966-a49324e2867a.png)


### Outliers
* Just did some quick manual calculations to see if there were any outliers in the COP data. Just did it this way because it was a smaller data set compared to the other Force Plate Analysis project I did that was about 60sec. worth of data (60,000+ rows). Also, because it just shows off another python skill that I know. This image is just for the X direction (medial/lateral).

![Signal1-8](https://user-images.githubusercontent.com/94875597/172924176-4ec8f04f-4daf-466e-90b1-b0b492fec45b.png)








