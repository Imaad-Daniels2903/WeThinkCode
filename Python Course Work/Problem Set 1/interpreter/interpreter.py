def main():
    expression = input("Expression: ").strip()
    exp_split = expression.split(" ")
    x = int(exp_split[0])
    y = exp_split[1]
    z = int(exp_split[-1])

    match y:
        case "+":
            answer = float(x + z)
            print(f"{answer:.1f}")

        case "-":
            answer = float(x - z)
            print(f"{answer:.1f}")

        case "*":
            answer = float(x * z)
            print(f"{answer:.1f}")

        case "/":
            answer = float(x / z)
            print(f"{answer:.1f}")

if __name__ == "__main__":
    main()