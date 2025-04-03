## Using the Monte Carlo Algorithm to Estimate the Value of π

The goal of this project is to estimate the value of π as the ratio of the area occupied by a circle with radius equal to 1 to the area of a square with side length equal to 2.

The Monte Carlo method involves randomly generating n points in space, then determining whether or not each point lies within the circle. This allows for calculating the ratio of “hits” (points inside the circle) to "misses" (points outside the circle).

As expected, the estimated value will converge to the true value of π as the number of points n increases. 
This is illustrated by the included plots: one showing location of points, one showing calculated values for successive values of n, and a boxplot representing the distribution of estimated values for different n values (100 estimates for each n).
<br>

![obraz](https://github.com/user-attachments/assets/85c4872b-0617-4be3-bc7d-5007a998307f)<br>
![obraz](https://github.com/user-attachments/assets/2a75f112-54bd-4874-8125-f121302f9db8)<br>
![obraz](https://github.com/user-attachments/assets/9fdeec20-a1d4-40e5-aeec-5c73f116f09b)
