import numpy as np
import math
import matplotlib.pyplot as plt
G = 6.674e-11
#massFlowRate = float(input('massFlowRate'))
#mass0 = float(input('mass0'))
#exV = float(input('exaustVelocitvr'))
#h = float(input('height'))
#r = float(input('radius'))
#mE = float(input('mass of the planet'))

#inputPrvi = input("odaberi promenljivu: h, exV, massOfEarth, massFlowRate, massOfRocket")
promenljiva =  0
if True:
    startingHeight =  1000
    finishingHeight = 4000
    deltaH = np.linspace(startingHeight,finishingHeight,100)
    promenljiva = deltaH

    
    exV = 3000
        
    massFlowRate = 3000
    mass0 = 42e4
    #h = 500

    r = 6378*10**3

    mE = 59736*10**20


def acceleration(h):

    
    vr = massFlowRate * (2*h)**0.5/ mass0

    z = -G/mass0*(  mE*mass0 / (r+h)**2  - massFlowRate * exV)

    w = -G/((r+h)**2 * mass0)  * (mE * massFlowRate * (2*h) ** 2)
    
    
    p = z - vr**2 / 3

    q = w + 2 * vr**3/27 - z*vr/3
    
    product = (-q / 2 + (q **2 / 4  + p **3 /27)**0.5)**(1/3) + (-q / 2- (q**2/4 + p**3/ 27)**0.5)


    if product.any()> 0:
        alpha = abs(product)**(1/3)
    else:
        alpha =-abs(product)**(1/3)
    sqrtA = alpha - vr / 3

    acc = sqrtA **2
    
    

    #acc = -q/2+(q**2/4+p**3/27)**0.5
    mu = mass0 *.9 - massFlowRate*(h/acc)**0.5
    return acc
velocity = 0
time = (deltaH*2/acceleration(deltaH))**0.5
velocity += acceleration(deltaH) * time
mass = mass0 - time * massFlowRate

Ek = velocity **2*mass/2
Ep = -mass* mE/(r+deltaH) * G + mass0*mE*G/r 

force = mass * mass0/(r+deltaH)**0.5*G
# 100 linearlvr spaced numbers



fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('white')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(force, promenljiva, 'blue')

plt.show()


#simulating integration











