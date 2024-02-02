**In programming, recursion is used for solving**

**problems that can be broken down**

**into smaller, repetitive problems.**

**It's especially good for working on things that have**

**many possible branches and too**

**complex for an iterative approach.**

**One good example of this would be**

**searching through a file system.**

**What is recursion?**

**Recursion is essentially a function that calls itself.**

**Recursion creates a pattern of**

**repeating itself over and over and over.**

**What does that mean from a coding perspective?**

**In this example, a function**

**accepts a single argument and inside the function,**

**it has some logic to**

**deal with the problem it's trying to solve.**

**The key part is the return.**

**In the code, the return statement**

**is returning the same function.**

**Recursion is quite similar to a for loop.**

**It will iterate, or in the case of a recursive function,**

**call itself multiple times.**

**But a warning when you create a recursive function,**

**you must always consider the results.**

**If you don't, it will spin**

**into an infinite loop and suck up**

**all the memory until the program**

**eventually crashes or gets terminated.**

**Let's compare how to use a looping and**

**a recursive solution to find**

**the factorial of a number that can be solved.**

**Let's start with the looping solution.**

**The looping function accepts a single integer called n as**

**an argument and first checks**

**if the number is less than zero.**

**If it is, it returns zero as you**

**can't have a factorial negative number.**

**The else condition sets the factorial to**

**one and then loops through the range of the argument,**

**which is five in this case.**

**The loop will calculate 1 times**

**2 times 3 times 4 times 5,**

**which will give the answer as 120,**

**the factor of five.**

**Now let's explore the**

**recursive solution to the same problem.**

**The recursive function is simpler and more compact.**

**The main reason for this is that you no longer need**

**the for-loop to do the iteration of the argument.**

**The first line of the function verifies that**

**the number is one and returns one if true.**

**The else condition multiplies**

**the argument n by calling the find**

**factorial recursive function and passing in n minus one.**

**Recursion can be difficult to understand.**

**By way of explanation,**

**let's demonstrate exactly what**

**happened as the function calls itself.**

**The function is being called over and over and the part**

**that changes is the value being**

**passed into the function each time.**

**The argument of n or five in this case,**

**is decreased by one each time until it finally is one.**

**This stops the function from being called**

**again and exits out of the recursive process.**

**How exactly did this code to get the results of 120?**

**This is provided by the return statement.**

**It keeps a reference to the incremented value,**

**and this is the final return after it has been completed.**

**It's time to review the advantages**

**and disadvantages of recursion.**

**First, the advantages are**

**recursive code can make your code neater and less bulky.**

**Complex tasks can be broken down**

**into easier to read sub-problems.**

**Generation of sequences can be**

**easier to understand than nested loops,**

**but there are disadvantages.**

**It can be harder to follow the logic in recursive code.**

**In terms of memory, they are**

**expensive and sometimes inefficient.**

**It can also be difficult to**

**debug and step through the code.**

**You should now be able to explain what recursion**

**is and how it can be used to solve problems.**

**I believe you'll benefit from**

**using recursion in your code in the future.**
