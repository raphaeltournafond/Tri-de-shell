N = 10

def Tri_shell(t):
    incr = N//2
    while True:

        for k in range (1, incr):
            # tri la k-ieme série

            for i in range (incr + k, N, incr):
                # insertion de t[i] dans sa série
                x = t[i]
                j = i - incr

                while j >= 1 and t[j]:
                    t[j + incr] = t[j]
                    j = j - incr

                t[j + incr] = x

        incr = incr//2
        if incr == 1:
            break

t = [5, 41, 53, 11, 20, 5, 1, 9, 12, 102, 15]
print("Avant : ", t)

Tri_shell(t)
print("Apres : ", t)
