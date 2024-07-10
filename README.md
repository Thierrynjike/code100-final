# Solution of Code 100 final

I have the coordinates of the centres of the 2 "O". A "O" is a Thorn composed of two circles with the same centre. A point belongs to a "O" if it is outside the smaller circle and inside the larger one. 
The equation of a circle is (x-a)^2 + (y-b)^2 = r^2  with (a,b) the coordinates of the centre and (x,y) the coordinates of the point
a point is inside the circle if (x-a)^2 + (y-b)^2 < r^2 and outside if (x-a)^2 + (y-b)^2 > r^2
if r1 is the smaller radius and r2 the larger one, a point belongs to a "O" if
r1^2 <= (x-a)^2 + (y-b)^2 <= r2^2 assuming the edges count as included.
we repeat the same action for the second "O"

For the "1", the upper and lower bounds of the height and width are given. A point belongs to the "1" if
lbx <= x <= upx and lby <= y <= upy.  assuming the edges count as included

Finally a point is selected if it belongs either to the "1" or to one of the "O"

The max_right value is the end of the second "0". 

To svae calculation time, it does not worth to check if a point after max_right belongs to the logo. So we can save this time. Similarly, we exclude all the point above, below, and at the left of the "1".

