# Simulation Set-up

## icoFoam-Reference - Reference Solution for Cylinder
To properly run the reference simulation, you should consider the following:

### 0 - Removing old data
```bash
foamListTimes -rm
rm -r postProcessing
```

It might also be necessary to remove the VTK file, if that is present.
```
rm -r VTK
```

### 1 - Creating the blockMesh
When initializing the blockMesh I find it better, especially considering we're going to work on multiple meshes, that we do not use:

```bash
blockMesh
```

This initializes the previous blockMeshDict used in the original icoFoam cavity tutorial. Which is not what we are using. To initialize a chosen blockMesh dict we can do the following:

```bash
blockMesh -dict caseDict/blockMeshDict
```

#### Quick sidenote
I came across a fascinating function in OpenFoam

```bash
transformPoints -scale "(x y z)"
```

This is interesting because it simplifies the meshing significantly! It basically stretches the mesh in a desired direction. In less than 5 minutes I was able to simulate three cases:

1. The Reference Cylinder - Drag Coefficient = 2.706

2. A long Oval - Drag Coefficient = 1.116
```bash
transformPoints -scale "(1 0.5 1)"
```

3. A tall Oval - Drag Coefficient = 5.971
```bash
transformPoints -scale "(1 1.5 1)"
```


### 2 - Initializing the velocity field
To reduce CPU-time we give the simulation a starting velocity field, which speeds up the time before the system is "dynamically steady". Run:

```bash
setFields
```

A better solution, instead of using setFields, would be to overwrite the first timestep with the latest data from the previous simulation. However this has a few setbacks, because you would have to first run the simulation once for all the different mesh resolutions. Since we are going to do multiple simulations for every mesh resolution, this is a better idea than using setFields.

```bash
cp -r 200/U 0/U
cp -r 200/p 0/p
```

### Proper icoFoam-Reference Pre-Processing
```bash
blockMesh -dict caseDict/blockMeshDict		# Creates the correct mesh
transformPoints -scale "(x y z")		# Scales the mesh
checkMesh					# Important to check the blockMesh
setFields					# Initializes the velocity field
```
