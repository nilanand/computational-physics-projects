# Radioactive Decay

A small numerical simulation of radioactive decay using Python, NumPy, and Matplotlib I made to practice looping through arrays.

The program solves

$$
\frac{dN}{dt} = -\lambda N
$$

numerically using Euler's method.

## Inputs

The program asks for:

```text
N0 decay_constant t dt
```

where:

* $N_0$ = initial number of undecayed particles
* $\lambda$ = decay constant
* $t$ = total simulation time
* $\Delta t$ = timestep

## Math

At each timestep, the decay rate is calculated using

$$
\frac{dN}{dt} = -\lambda N
$$

and the next value is approximated with

$$
N_{i+1} = N_i + \frac{dN}{dt}\Delta t
$$

## Output

The program plots the number of undecayed particles $N(t)$ as a function of time.

The result approaches zero as the particles decay.


