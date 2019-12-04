File_Object = open(r"C:\Users\patrick.wylie\source\repos\PythonFizzBuzz\Output.txt","w")
for num in range(1,100):
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    output_line = str(num) + " " + string
    File_Object.write(output_line + "\n")