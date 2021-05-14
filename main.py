def arithmetic_arranger(problems):
    # Checking errors
    if len(problems) > 5:
        return "Error: Too many problems."
    for i in problems:
        x = i.split()
        n1 = x[0]
        n2 = x[2]
        op = x[1]

        if n1.isdigit() and n2.isdigit() is False:
            return "Error: Numbers must only contain digits."
        if len(n1) and len(n2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if op not in "+""-":
            return "Error: Operator must be '+' or '-'."
        else:
            if op == "+":
                a = int(n1) + int(n2)
            else:
                a = int(n1) - int(n2)

            width = max(len(n1), len(n2)) + 2
            tab = " " * 4

            f_line = f"{n1.rjust(width) + tab}"
            s_line = f"{op}{n2.rjust(width - 1)}"
            t_line = "-" * width
            l_line = f"{str(a).rjust(width)}"

            print(f_line, s_line, t_line, l_line,"\n", sep="\n")


print(arithmetic_arranger(["30 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
