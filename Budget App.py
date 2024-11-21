# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:36:14 2024

@author: jlove
"""

class Category:
    def __init__(self,category):
        self.category = category
        self.ledger = []
        
    def __str__(self):
        title = f"{self.category:*^30}\n"
        items =''
        Total=0
        for item in self.ledger:
            items += f"{item['description'][:23]:23}"+f"{item['amount']:>7.2f}"+'\n'
            Total += item['amount']
        output = title+items+'Total: '+f'{Total:.2f}'
        return output
    
    def deposit(self,amount,description=''):
        
        if description is None:
            self.ledger.append({"amount": amount, "description": ' '})
        else:
            self.ledger.append({"amount": amount, "description": description})
        
    def withdraw(self,amount,description=''):
        if self.check_funds(amount):
            if description is None:
                self.ledger.append({"amount": -amount, "description": ' '})
                return True
            else:
                self.ledger.append({"amount": -amount, "description": description})
                return True
        else:
            return False
        
    def get_balance(self):
        balance=0
        for item in self.ledger:
            balance +=item['amount']
        return balance
    
    def transfer(self,amount,category):
        if self.check_funds(amount):
            self.withdraw(amount,f'Transfer to {category.category}')
            category.deposit(amount,f'Transfer from {self.category}')
            return True
        else:
            return False
    
    def check_funds(self,amount): 
        if amount <= self.get_balance():
            return True
        if amount >= self.get_balance():
            return False
    
    
    
    
    
def create_spend_chart(categories):
    total_cost =[]
    percent_list=[]
    category_list=[]
    word_length =[]
    y_bar=100
    chart ='Percentage spent by category\n'
    for item in categories:
        category_list.append(item.category)
        word_length.append(len(item.category))
        for draw in item.ledger:
            cost=0
            if draw['amount']<0:
                cost+=(-draw['amount'])
        total_cost.append(cost)
    
    x_bar = len(category_list)
    for index in range(x_bar):
        result = int(((total_cost[index])/sum(total_cost))*100)
        percent_list.append(result)
    
    
    for y in range(y_bar,-1,-10):
        line =f'{y:>3}| '
        for x in range(x_bar):    
            if percent_list[x]>= y:
                line+= 'o  '
            else:
                line+='   '
        chart += line+'\n'
        
    bottom_line = '    -'
    for x in range(x_bar):
        bottom_line +='---'
    chart += bottom_line +'\n'
    
    
    for H in range(max(word_length)):
        bottom_description='     '  
        for x in range(x_bar):
            charg = max(word_length)-len(category_list[x])
            if charg>=0:
                category_list[x]+= ' '*charg
            bottom_description += f'{category_list[x][H]}  '  
        chart += bottom_description +'\n'
    chart = chart.rstrip('\n')
    return chart

food = Category("Food")
entertaiment = Category("Entertaiment")
business = Category("Business")
food.deposit(900,"deposit")
entertaiment.deposit(900,"deposit")
business.deposit(900,"deposit")

food.withdraw(105.55)
entertaiment.withdraw(33.40)
business.withdraw(10.99)
print(food)
print(entertaiment)
print(business)
print(create_spend_chart([business,food,entertaiment]))