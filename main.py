GlowScript 3.0 VPython

x_ax=curve(pos=[vector(-15,0,0),vector(15,0,0)],color=color.white)
y_ax=curve(pos=[vector(0,-15,0),vector(0,15,0)],color=color.white)

tgraph=graph(title="Amplitude vs time graph",xtitle="Time[seconds]",ytitle="Amplitude[theta]")
f1=gcurve(color=color.blue)
f2=gcurve(color=color.red)
f3=gcurve(color=color.green)

g=9.8  # acceleration due to gravity

bob=sphere(pos=vector(5,2,0),radius=1,color=color.red)
pivot=vector(0,15,0)
roof=box(pos=pivot,size=vector(4,1,1),color=color.white)
string=cylinder(pos=pivot,axis=bob.pos-pivot,radius=0.1,color=color.blue)
t=0 # time 
dt=0.01 # time interval 
len=mag(bob.pos-pivot) # length of pendulum
cosX=(pivot.y-bob.pos.y)/len # calculation of cos(theta) 
theta=acos(cosX) # angle with vertical direction
w=0.25 # angular velocity
while (t<25):
 rate(500) # maximum 500 calculations per second
 acc=-g/len*sin(theta) # updating of angular acceleration
 theta=theta+w*dt # updating of angular position
 w=w+acc*dt # updating of angular velocity
 bob.pos=vector(len*sin(theta),pivot.y-len*cos(theta),0) # calculating position
 string.axis=bob.pos-string.pos # updating other end of string of pendulum
 t=t+dt # updating time
 f1.plot(t,theta)

#greater angle1
bob=sphere(pos=vector(5,2,0),radius=1,color=color.red)
pivot=vector(0,15,0)
roof=box(pos=pivot,size=vector(4,1,1),color=color.white)
string=cylinder(pos=pivot,axis=bob.pos-pivot,radius=0.1,color=color.blue)
t=0 # time 
dt=0.01 # time interval 
len=mag(bob.pos-pivot) # length of pendulum
cosX=(pivot.y-bob.pos.y)/len # calculation of cos(theta) 
theta=acos(cosX) # angle with vertical direction
w=0.5
while (t<25):
 rate(500) # maximum 500 calculations per second
 acc=-g/len*sin(theta) # updating of angular acceleration
 theta=theta+w*dt # updating of angular position
 w=w+acc*dt # updating of angular velocity
 bob.pos=vector(len*sin(theta),pivot.y-len*cos(theta),0) # calculating position
 string.axis=bob.pos-string.pos # updating other end of string 
 t=t+dt # updating time
 f2.plot(t,theta)
 

#greater angle2
bob=sphere(pos=vector(5,2,0),radius=1,color=color.red)
pivot=vector(0,15,0)
roof=box(pos=pivot,size=vector(4,1,1),color=color.white)
string=cylinder(pos=pivot,axis=bob.pos-pivot,radius=0.1,color=color.blue)
t=0 # time 
dt=0.01 # time interval 
len=mag(bob.pos-pivot) # length of pendulum
cosX=(pivot.y-bob.pos.y)/len # calculation of cos(theta) 
theta=acos(cosX) # angle with vertical direction
w=0.75
while (t<25):
 rate(500) # maximum 500 calculations per second
 acc=-g/len*sin(theta) # updating of angular acceleration
 theta=theta+w*dt # updating of angular position
 w=w+acc*dt # updating of angular velocity
 bob.pos=vector(len*sin(theta),pivot.y-len*cos(theta),0) # calculating position
 string.axis=bob.pos-string.pos # updating other end of string 
 t=t+dt # updating time
 f3.plot(t,theta) 


