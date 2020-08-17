#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) This is a linear run time because it will take n runs through the loop for the conditional to be met

b) I think this one is n log n. I say this because the for loop will run n times, but the while loop will run half of n times (give or take 1). This function appears to behave in the opposite manner of dividing n by two.

c) This is a linear function. When we see recursion where n is decremented by 1, we can think of this like a loop because the recursive case will be called n times

## Exercise II

- define a function find_safe_floor which will take in n
- initialize a variable named safe with the value of 0 - safe will be our ultimate return value
- loop through a range of n
- check to see if the egg breaks
- if the egg does not break, increment the safe floor variable
- if the egg does break, exit the loop
- return safe floor
