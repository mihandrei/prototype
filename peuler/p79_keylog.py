def read_data():
    with open('p079_keylog.txt') as f:
        kl = []
        for l in f:
            t = int(l[0]), int(l[1]), int(l[2])
            kl.append(t)
        return kl

print read_data()