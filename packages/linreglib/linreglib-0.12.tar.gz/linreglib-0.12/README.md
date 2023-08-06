# Linreglib

Linreglib is my attempt at creating a libary of linear regression scripts. The goal of this project was to create a library of linear regression scripts that is efficent and easy to understand. So far I have only achivied Least Square Regression.

## Getting Started

The instructions below will get you a copy of my library. 

### Prequisites
So far, the only prequisitie you need are numpy. 

### Installing

#### Install Dependencies

```
pip install numpy
```
#### Get Linreg

```
pip install linreglib
```
### Updating

```
pip install linreglib --update
```

### How To Use Linreg

#### Example code
```
from linreglib import LSR
import matplotlib.pyplot as plt
from matplotlib import style

#This file is ment to show how one should use the scripts

style.use('fivethirtyeight')

x_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_list = [2 ,4 , 6, 8 , 10, 12, 14, 16, 18, 20]

test = LSR() #Picks which model
test.Model(x_list, y_list) #Caluclates Linear Regression using that model

y_approximate = [(test.slope*x)+test.intercept for x in x_list] 

plt.scatter(x_list, y_list)
plt.plot(x_list, y_approximate)
plt.show()
```
## How the code works

### Least Square Regression
To understand how the code works, we first need to understand the math behind Least Square Regression.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
