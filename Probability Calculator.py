# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 19:45:32 2024

@author: jlove
"""

import copy
import random

class Hat:
    def __init__(self,**colors_nums):
        #透過 **colors_nums 取得 key-value 對，例如 black=6, red=4, green=3）
        #其中 key 是顏色名稱，value 是該顏色的球數量。
        self.contents =[]
        for color,num in colors_nums.items():
            self.contents.extend([color]*num)
            
    def draw(self,num_of_draw):
        if num_of_draw > len(self.contents):
            return self.contents
        drawn_balls = random.sample(self.contents[:], num_of_draw)
        return drawn_balls
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count=0
    for _ in range(num_experiments):
       drawn_balls = hat.draw(num_balls_drawn)
       drawn_balls_counts={}
       
       for ball in drawn_balls:
           #if drawn_balls_counts has ball, get() will return the value
           drawn_balls_counts[ball] =drawn_balls_counts.get(ball,0)+1
       print(drawn_balls_counts)
       if all(drawn_balls_counts.get(color,0)>=expected_balls[color] for color in expected_balls):
           count+=1
                 
    probability = count / num_experiments
    return probability


hat = Hat(black=6, red=4, green=3)

probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)