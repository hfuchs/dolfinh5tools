import numpy as np
import dolfin as df

from savingdata import Create, Read

mesh = df.UnitSquareMesh(10, 10)
filename = 'file_mpi'
functionspace = df.VectorFunctionSpace(mesh, 'CG', 1, 3)
f = df.Function(functionspace)
t_array = np.linspace(0, 1, 5)

# Load data.
ld = Read(filename)
for t in t_array:
    f.assign(df.Constant((1 + t, 2, 3)))
    f_loaded = ld.load_field('f', t)

    print "%1.50f" % df.assemble(f[0]*df.dx)
    print "%1.50f" % df.assemble(f_loaded[0]*df.dx)
    print "%1.50f" % (df.assemble(f[0]*df.dx) - df.assemble(f_loaded[0]*df.dx))
    assert np.abs(df.assemble(f[0]*df.dx) - df.assemble(f_loaded[0]*df.dx)) < 1e-14
    print '------------'
ld.close()
