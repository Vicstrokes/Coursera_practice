**One of the basic ways to test the Python developer's problem-solving skills is by**

**asking them how they would reverse a string,**

**knowing how to do this is very useful in the production environment.**

**Some programming languages have a built-in function to reverse a string,**

**Python doesn't have such a function.**

**But fortunately due to the language's flexibility,**

**there are several ways to do this.**

**In this video, I will show you two ways to reverse a string in python.**

**First I'll demonstrate how to do this with a slice function.**

**To start off, I create a file called string reversal .pi.**

**The format or**

**syntax of a slice function is that it always starts with the name of a string.**

**Open square bracket, the start parameter colon, the stop parameter,**

**another colon, and then the step parameter followed by a closed square bracket,**

**I'll add a hash symbol in front of this line to indicate that it is a note.**

**This is called the extended slice syntax.**

**The start and**

**stop parameters are the indices between which the function manipulates the string.**

**The step parameter is the hops or jumps.**

**The function makes Walter versus a given string.**

**I will now first define a string,**

**then manipulate the string with the slice function and finally print the string.**

**I'll call the string trial and assign the word reversal as its value by**

**typing trial, equal sign, and the word reversal between double-quotes.**

**To manipulate the string, I create a new string called a new trial.**

**Now I sign a value to a new trial with the slice function.**

**I type an equal sign trial and open square bracket.**

**To instruct python to use the entire string, I leave the value of the start and**

**stop parameters empty.**

**I simply type two colons and then add the value of the step parameter as**

**the number minus one, followed by a closed square bracket.**

**The negative value of the step parameter indicates that the string needs to be**

**traversed from the right one index position at a time.**

**Instead of the conventional method of starting from the left.**

**Finally, I print the manipulated string to test if it works.**

**I type print in between parentheses, I add the string name, new trial,**

**I click on run great in the terminal the string has successfully been reversed.**

**In summary, the entire string is traversed from right to left,**

**one index position at a time.**

**This new sliced object is then copied to**

**another string which is then rearranged and printed.**

**It should be noted that you can use the slice function to manipulate the same**

**variable.**

**I only used a second variable in this example for clarity.**

**The slice function is the simplest way to reverse a string.**

**I will now demonstrate another way you can use the slice function to reverse**

**a string, this time using recursion.**

**I start by creating a new file and saving it as string reversal 2.pi.**

**Next, I define a function and pass a string variable to it namely str.**

**I type deaf and the function name, string, reverse, and**

**str between parentheses followed by a colon.**

**This function will act as a conditional if statement I**

**type if len open parenthesis str close Parenthesis**

**two equal Signs the number zero followed by a colon.**

**On the next line, I'll return the value of str.**

**Now let's add the else statement.**

**The else statement will be recursive we call the slice function but**

**with a modified string every time.**

**On the next line, I add else and a colon.**

**Then on the next line, I type return string reverse str.**

**But before I close the parentheses, I add a slice function by typing the open square**

**bracket, the number one, and a colon followed by the closed square bracket.**

**This time the string is traversed from the front,**

**skipping the first character in every loop and**

**this first character skipped is appended to the remaining string.**

**So I now add a plus sign, str, and the value zero in between brackets.**

**Outside the function I give str the value of reversal,**

**then I create a second variable that will store the value of the return string.**

**I'll call this variable, reverse, and assign to it the value of the function.**

**Finally, I add a print statement for the variable reverse.**

**Let's run the code.**

**Success.**

**The string displays in reverse order in the terminal, essentially the function**

**calls itself by passing a different string in each recursion and**

**appending the element it has kept right after it.**

**In this video, You learned two different methods to reverse a string in python,**

**the first by just using a slice function and**

**the second by using a slice function with record recursion.**
