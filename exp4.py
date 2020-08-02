import numpy as np
import matplotlib.pyplot as plt

def plot_polygon(polygon):
   size = len(polygon)
   x = np.zeros(size+1, dtype=float)
   y = np.zeros(size+1, dtype=float)
   for i in range(size):
       x[i] = polygon[i][0]
       y[i] = polygon[i][1]
   x[size] = polygon[0][0]
   y[size] = polygon[0][1]
   plt.plot(x, y,color='Blue', linestyle='-.')
   plt.title("General Polygon: {} sided.".format(size))
   plt.xlabel("x axis")
   plt.ylabel("y axis")
   plt.grid(True)
   plt.show()
   return size
    
def check_polygon(polygon, point):
     size = len(polygon)
     xcg, ycg = 0.0, 0.0 
     
     for i in range(size):
        xcg  +=  polygon[i][0]
        ycg += polygon[i][1]
         
     xcg = xcg/size
     ycg = ycg/size
     pcg = [xcg,ycg]
     status = False
     area=0.0
     area1=0.0
     
     for i in range(size):
         if i<size-1:
             p1 = [polygon[i][0], polygon[i][1]]
             p2 = [polygon[i+1][0], polygon[i+1][1]]
         else:
             p1 = [polygon[i][0], polygon[i][1]]
             p2 = [polygon[0][0], polygon[0][1]]
             
         area += 0.5*abs((pcg[0]*(p1[1]-p2[1])
                +p1[0]*(p2[1]-pcg[1])
                +p2[0]*(pcg[1]-p1[1])))
         
        
         if i<size-1:
             p1 = [polygon[i][0], polygon[i][1]]
             p2 = [polygon[i+1][0], polygon[i+1][1]]
         else:
             p1 = [polygon[i][0], polygon[i][1]]
             p2 = [polygon[0][0], polygon[0][1]]
             
         area1 += 0.5*abs((point[0]*(p1[1]-p2[1])
                +p1[0]*(p2[1]-point[1])
                +p2[0]*(point[1]-p1[1])))
     
     print("Area of polygon is: ",area)
     
     if area1==area:
         status=True
         
     if status==True:
         print("Point inside polygon")
     else:
         print("Point outside polygon")
         
     return area, status, xcg, ycg


polygon=[(0.0,0.0),(4.0,0.0),(6.0,2.0),(4.0,4.0),(0.0,4.0),(-2.0,2.0)]
point =[1.0, -1.0]
sz = plot_polygon(polygon)
a,b,c,d = check_polygon(polygon, point)
