if __name__ == "__main__":

    days = int(input())
    result = 0
    people = 5

    for i in range(days):
        liked_advertisement = int(people / 2)
        result += liked_advertisement
        people = liked_advertisement * 3

    print("{}".format(result))

