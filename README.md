In First code, I opened the file sample.txt with "with" keyword as duplicate name "f" under "try" so that if any error occur it will be transfered to except block and code will execute accordingly
I used readlines so that all the content of the text file is stored as a string element of a list. And then used a for loop to print each line of the file which was stored as string in the list and used rstrip('\n') so that I can remove unwanted newline character in the output
Then in except block I wrote the error name "FileNotFoundError" and printed required line.

In Second code, I opened a file in write mode as "o" and wrote some data using "write" function then again opened the file but now in "appened" mode and added new data through write function
Then again opened it in read mode and used readlines function which stored every line as string element of a list and printed that using a for loop and used rstrip('\n') so that unwanted newline is removed.
