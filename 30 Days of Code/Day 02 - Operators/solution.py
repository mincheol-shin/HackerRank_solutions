def main():
    mealCost,tipPercent,taxPercent = float(input()), int(input()), int(input())

    tipPercent = mealCost * tipPercent / 100
    taxPercent = mealCost * taxPercent / 100
    totalCost = mealCost + tipPercent + taxPercent
    # 반올림하여 정수값으로 출력
    print("{0}".format(int(round(totalCost))))

if __name__ == "__main__":
    main()