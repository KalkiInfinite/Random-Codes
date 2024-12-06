class Item:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit


def compare(itemA, itemB):
    ratioA = itemA.profit / itemA.weight
    ratioB = itemB.profit / itemB.weight
    if ratioA < ratioB:
        return 1  
    elif ratioA > ratioB:
        return -1
    return 0

if __name__ == "__main__":
    items = []
    Totalvalue = 0.0

    n = int(input("Enter the number of items: "))

    for i in range(n):
        weight, profit = map(float, input(f"Enter Weight and Profit for item[{i}]: ").split())
        items.append(Item(weight, profit))

    capacity = float(input("Enter the capacity of knapsack: "))


    items.sort(key=lambda x: x.profit / x.weight, reverse=True)

    print("Knapsack problem using Greedy Algorithm:")
    for i in range(n):
        if items[i].weight > capacity:
            break
        else:
            Totalvalue += items[i].profit
            capacity -= items[i].weight

    if i < n:
        Totalvalue += (items[i].profit / items[i].weight) * capacity

    print(f"The maximum value is: {Totalvalue:.2f}")