import math

message = [145213650433152, 4562349440334, 24272724667960, 598242834066721, 89584939111364, 426756492371444, 511701778613016, 551732685650248, 296367799892003, 63113462897284, 198510931603899, 321201931522255, 401044612595398, 542697603423052, 213898535689643, 275839755798105, 185841409622217, 551732685650248, 121188708737752, 401044612595398, 512808963720303, 275839755798105, 198510931603899, 275839755798105, 401044612595398, 174484844253615, 551732685650248, 174486913717420, 575163265381617, 213898535689643, 401044612595398, 49103824223436, 551732685650248, 401044612595398, 598242834066721, 202722428784490, 306606077829794, 53801100921263, 401044612595398, 184805755675232, 405971446461049, 296367799892003, 275839755798105, 275839755798105, 401044612595398, 358054299396778, 4562349440334, 320837325468842, 401044612595398, 202722428784490, 551732685650248, 321201931522255, 228350651363859]

def getModInverse(a, m):
    if math.gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def main():
    # n factorized w/Wolfram Alpha gives: 13458281 x 46631887
    n = 627585038806247
    e = 65537
    p = 13458281
    q = 46631887

    # Compute phi(n)
    phi = (p - 1) * (q - 1)

    # Compute modular inverse of e
    d = getModInverse(e, phi)

    for ct in message:
        # Decrypt ciphertext
        pt = pow(ct, d, n)
        print(chr(pt), end='')
    print()
if __name__ == "__main__":
    main()