LOOPS:

Loop control variable:
    Creates the entry/exit conditions. Updated and checked during each iteration. 
    i++

Loop body:
    Instructions to execute during each iteration of the loop.
    print(arr[i])

Entry conditions:
    Boolean expression to start the loop.
    i < 10

Exit conditions:
    Boolean expression to end the loop.
    i > 10

While loops:
    Repeated while expression is true. May or may not execute at all.

Do while loops:
    Repeated until expression is false. Will run at least once. Checks conditional at the end of the iteration. Could be useful to get user input before running several potential loops. 

For loops:
    Definite amount of iterations. May or may not execute at all. 

Nested loops:
    Loop inside of another loop. Can be any type of loop. Helps iterating through multi dimensional arrays such as matrices and tensors. Need to be careful with nested loops due to the increased run time.

Infinite loops:
    An endless loop that runs forever. Normally avoided. 