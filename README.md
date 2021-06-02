
# Plot Residuals

This repository contains scripts for obtaining residual values generated in [Ansys Fluent](https://www.ansys.com/products/fluids/ansys-fluent) simulations through transcription files that are automatically generated throughout the simulations.

----

 * The ```main.py``` contains the whole script that:
 
	 * Read a ```.trn``` file
	 * Extract the residual name
	 * Extract the residual values, line by line
	 * Save all into a [```Pandas.DataFrame```](https://pandas.pydata.org)
	 * Plot all residuais using the [```Plotly```](https://plotly.com) package
	 
* The ```data``` folder is used to storage the ```.trn``` files that are generated by simulations
* The ```output``` folder is used to storage the ```.html``` files with the plot generated by [```Plotly```](https://plotly.com)
