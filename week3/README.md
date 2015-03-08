#### Problem 1.

Look at the Problem 1 part in the script's main function.
To run the code, simply:

    python week3.py

Remember to set two input files and the min support value in main function:  
1. a text file containing the data of Sequence database (q1_Q.txt)  
2. a text file (q1_A.txt)  

The results are like the following:  
a bf is subsequence of:  
1 2 3 4  
a bf => True  
f bd is subsequence of:  
2 4  
f bd => False  
ab f is subsequence of:  
1 3  
ab f => False  
a b c is subsequence of:  
1  
a b c => False  

The first series of numbers are the indices of the sequences in database so that the subsequence is frequent of them.  
The next line shows whether the subsequence is frequent based on the min support value.  
