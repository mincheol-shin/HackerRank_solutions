import re



if __name__ == '__main__':
    N = int(input())
    gmail_list = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        p = re.compile("@gmail.com")

        if p.search(emailID):
            gmail_list.append(firstName)

    gmail_list.sort()
    print(*gmail_list, sep = "\n")
