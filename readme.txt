PACCMAN Developer's Guide:
(Python Analysis of Conformal Cooling Molds And/or desigNs)

This guide is meant as a resource for using, adding to, or integrating the PACCMAN program. Feedback is welcome.


In it's current state, the program has three options presented to the user.

Selecting "N" uses the first material properties (KM1, etc.) and then gives choice of heat transfer coefficient correlation.

Selecting "M" compares the three materials using the Gnielinski correlation.

Selecting "H" compares the three heat transfer coefficient correlations using the first material property (KM1, etc.).

For all three choices, the program asks the user if they would like to save graphs of the average heat cycle temperature over time.
Choosing "Y", downloads the graph in .png and .eps formats.

The program is written so that by changing the variables, it can analyize any conformal cooling design.

The printed out data is as follows: flow velocity, kinematic viscosity, Reynolds number, Prandl number, Farcy friction factor, heat transfer coefficient, average heat cycle temperature of the mold, time constant, coolant pressure drop.

The program can by testing by running pytest in it's directory.

Please report all bugs to hughfeehan353 on Github. Thanks.