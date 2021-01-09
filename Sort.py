from tkinter import *
import random
import time

root = Tk()
w = Canvas(root, width=1200, height=600)

class Sort():
    def __init__(self, id):
        self.id = id

    def BubbleSort(arr):
        for i in range (0, len(arr)-1):
            for j in range(0, len(arr)-1-i):

                arrJ = w.coords(arr.__getitem__(j).id) # rect-object coordinates[x0,y0,x1,y1]
                arrJ1 = w.coords(arr.__getitem__(j+1).id) # rect-object coordinates[x0,y0,x1,y1]
                if arrJ[1] < arrJ1[1]:

                    #Move the bars to a new location based on bubblesort
                    #Will do for now instead of deleting the bars that need to be sorted
                    #And create new ones
                    myrect1 = arr[j]
                    myrect2= arr[j+1]
                    xmove = colWidth
                    w.move(arr[j].id, xmove, 0)
                    w.move(arr[j+1].id, -xmove, 0)
                    w.update()

                    #Pop the rect-objects that need sorting and insert them at the new location
                    arr.pop(j+1)
                    arr.insert(j+1, myrect1)

                    arr.pop(j)
                    arr.insert(j, myrect2)
                    #time.sleep(0.05)

    #After the sorting is done, draw the final result.
    def printArr(self):

        arrTemp = []
        for i in range(0,len(arr)):
            c = w.coords(arr.__getitem__(i).id) # object coordinates[x0,y0,x1,y1]
            arrTemp.append(c[1])

        for k in range(0, len(arr)):
            w.create_rectangle(k*colWidth, arrTemp[k], k*colWidth+colWidth, 600, fill="red", outline = 'blue')
            w.update()

numColums = 400
colWidth = 3
arr = []
# Create random rectangle bar objects
for i in range(0,numColums):
    n = random.randint(0,550)
    arr.append(Sort(w.create_rectangle(i*colWidth, 600-n, i*colWidth+colWidth, 1200, fill="red", outline = 'blue')))

w.pack()

#Sort and visualize
Sort.BubbleSort(arr)

#Draw after all is done
Sort.printArr(arr)

w.mainloop()
