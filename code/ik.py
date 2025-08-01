from roboticstoolbox import DHRobot, RevoluteDH
import numpy as np
import matplotlib.pyplot as plt
import time
import tkinter as tk
from tkinter import ttk
import threading

dh_params = [
    RevoluteDH(d=0, a=0, alpha=0, qlim=[-np.pi/2, np.pi/2]),              
    RevoluteDH(d=9.5, a=0, alpha=np.pi/2, qlim=[-110*np.pi/180, 110*np.pi/180]),      
    RevoluteDH(d=0, a=14.963, alpha=0, qlim=[-100*np.pi/180, 100*np.pi/180]),         
    RevoluteDH(d=8.149, a=0.515, alpha=np.pi/2, qlim=[-np.pi/2, np.pi/2]),   
    RevoluteDH(d=8.5, a=0, alpha=-np.pi/2, qlim=[-np.pi/2, np.pi/2]),       
    RevoluteDH(d=1, a=0, alpha=0, qlim=[-np.pi/2, np.pi/2]),              
]

robot = DHRobot(dh_params, name="xenox")


def get_jointangles(x, y, z):
    try:
        targetpos = np.array([x/100, y/100, z/100])
        solution = robot.ikine_LM(targetpos)
        
        if solution.success:
            jointrads = solution.q
            jointdegs = np.degrees(jointrads).tolist()
            return jointdegs
        else:
            print(f"No solution found :/ ({x}, {y}, {z})")
            return None
            
    except Exception as e:
        print(f"Error !!! {e}")
        return None
    
    
### stuff to get angles for each joint for a position