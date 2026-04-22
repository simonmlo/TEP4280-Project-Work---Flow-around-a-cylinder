# Simulation Set-up

## icoFoam-Reference - Reference Solution for Cylinder
To properly run the reference simulation, you should consider the following:

### 0 - Removing old data
```bash
foamListTimes -rm
rm -r postProcessing
```

You can also remove data in a given range if needed:
```bash
foamListTimes -rm -time 'start:end'
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
blockMesh -dict meshDict/<chosen mesh resolution>
```

#### Quick sidenote
I came across an interesting function in OpenFoam

```bash
transformPoints -scale "(x y z)"
```

This is interesting because it simplifies the meshing significantly! It basically stretches the mesh in a desired direction. In less than 5 minutes I was able to simulate three cases:

1. The Reference Cylinder

2. A long Oval
```bash
transformPoints -scale "(1 0.5 1)"
```

3. A tall Oval
```bash
transformPoints -scale "(1 1.5 1)"
```


### 2 - Initializing the velocity field
To reduce CPU-time we give the simulation a starting velocity field, which speeds up the time before the system is "dynamically steady". Run:

```bash
setFields
```

A better solution, instead of using setFields, would be to overwrite the first timestep with the latest data from the previous simulation. However this has a few setbacks, because you would have to first run the simulation once for all the different mesh resolutions. Since we are going to do multiple simulations for every mesh resolution, this is a better idea than using setFields. Another way to initialize a velocity field is to continue the simulation from a given time, which we also used.

```bash
cp -r 200/U 0/U
cp -r 200/p 0/p
```

```bash
foamListTimes -rm -time '200.05:300'
```

### Proper icoFoam-Reference Pre-Processing
```bash
blockMesh -dict meshDict/<chosen mesh resolution>  # Creates the correct mesh
checkMesh  # Important to check the blockMesh
icoFoam  # Starts the simulation
```
