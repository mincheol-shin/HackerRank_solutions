N = int(input())
country_stamps = set()
for _ in range(N):
    country_stamps.add(input())
print("{}".format(len(country_stamps))