Nx = 6
Ny = 6
nx = 10
ny = 10
dx = 20.0
dy = 10.0
with open('a.geo', 'w') as f:
    f.write("lc = 0.1;\n")
    for i in range(Nx):
        for j in range(Ny):
            f.write(f"""Point({i*Ny + j + 1}) = {{{i*dx}, {j*dy}, 0, lc}};\n""")
    for i in range(Nx):
        for j in range(Ny-1):
            f.write(f"Line({i*Ny + j + 1}) = {{{i*Ny + j + 1}, {i*Ny + j + 1 + 1}}};\n")
    for i in range(Nx):
        for j in range(Ny-1):
            f.write(f"Line({100000 + i*Ny + j + 1}) = {{{i + j*Nx + 1}, {i + (j+1)*Nx + 1}}};\n")
    for i in range(Nx-1):
        for j in range(Ny-1):
            f.write(f"Curve Loop({i*Ny + j + 1}) = {{{i + j*Nx + 1}, {100000 + (i+1)*Ny + j + 1}, -{i + (j+1)*Nx + 1}, -{100000 + i*Ny + j + 1}}};\n")
            f.write(f"Plane Surface({i*Ny + j + 1}) = {{{i*Ny + j + 1}}};\n")

    #    f.write("Physical Curve(\"Bottom\", 10001) = {")
    #    for i in range(Ny-1):
    #        if i == Ny-2:
    #            f.write(f"{1001 + i}}};\n")
    #        else:
    #            f.write(f"{1001 + i}, ")
    #    f.write("Physical Curve(\"Top\", 10002) = {")
    #    for i in range(Ny-1):
    #        if i == Ny-2:
    #            f.write(f"{1001 + (Nx-1)*Ny + i}}};\n")
    #        else:
    #            f.write(f"{1001 + (Nx-1)*Ny + i}, ")
    #    f.write("Physical Curve(\"Right\", 10003) = {")
    #    for i in range(Nx-1):
    #        if i == Nx-2:
    #            f.write(f"{i + 1}}};\n")
    #        else:
    #            f.write(f"{i + 1}, ")
    #    f.write("Physical Curve(\"Left\", 10004) = {")
    #    for i in range(Nx-1):
    #        if i == Nx-2:
    #            f.write(f"{i + 1 + Nx*(Ny-1)}}};\n")
    #        else:
    #            f.write(f"{i + 1 + Nx*(Ny-1)}, ")

    #    f.write("Physical Surface(\"M1\", 10005) = {")
    #    for i in range(Nx-1):
    #        for j in range(Ny-1):
    #            if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
    #                if (i == Ny-2) and (j == Ny-2 or j == Ny-3):
    #                    f.write(f"{i*Ny + j + 1}}};\n")
    #                else:
    #                    f.write(f"{i*Ny + j + 1}, ")
    #    f.write("Physical Surface(\"M2\", 10006) = {")
    #    for i in range(Nx-1):
    #        for j in range(Ny-1):
    #            if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
    #                if (i == Ny-2) and (j == Ny-2 or j == Ny-3):
    #                    f.write(f"{i*Ny + j + 1}}};\n")
    #                else:
    #                    f.write(f"{i*Ny + j + 1}, ")

    #    f.write("Physical Surface(\"M1\", 1) = {")
    #    for i in range(int((Nx-1)/nx -1)):
    #        for j in range(int((Ny-1)/ny-1)):
    #            if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
    #                for ii in range(nx):
    #                    for jj in range(ny):
    #                        if (i == int((Nx-1)/nx-2)) and (j == int((Ny-1)/ny-2) or j == int((Ny-1)/ny-3)) and (((ii == nx-1) and (jj == ny-1))):
    #                            print(f"i, j, ii, jj \n {i}, {j}, {ii}, {jj}")
    #                            f.write(f"{i*ny*Ny + ii*Ny + j*nx + jj + 1}}};\n")
    #                        else:
    #                            f.write(f"{i*ny*Ny + ii*Ny + j*nx + jj + 1}, ")
    #    f.write("Physical Surface(\"M2\", 2) = {")
    #    for i in range(int((Nx-1)/nx-1)):
    #        for j in range(int((Ny-1)/ny-1)):
    #            if (i % 2 == 1 and j % 2 == 0) or (i % 2 == 0 and j % 2 == 1):
    #                for ii in range(nx):
    #                    for jj in range(ny):
    #                        if (i == int((Nx-1)/nx-2)) and (j == int((Ny-1)/ny-2) or j == int((Ny-1)/ny-3)) and (((ii == nx-1) and (jj == ny-1))):
    #                            print(f"i, j, ii, jj \n {i}, {j}, {ii}, {jj}")
    #                            f.write(f"{i*ny*Ny + ii*Ny + j*nx + jj + 1}}};\n")
    #                        else:
    #                            f.write(f"{i*ny*Ny + ii*Ny + j*nx + jj + 1}, ")
