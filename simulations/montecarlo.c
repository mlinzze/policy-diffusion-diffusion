#include  <stdio.h>
#include  <math.h>
#include  <string.h>
#include "functions.h"

int main(int argc, char *argv[])
{

	int DEBUG = 0;
	int ncountries = 50;
	int nvariables = 5;

	const char* metric = argv[1];
	const char* model = argv[2];
	const char* time_period = argv[3];
	const char* policies = argv[4];
	const char* scenario = argv[5];
	const char* parameter_constant = argv[6];
	const char* parameter_beta_W = argv[7];

	printf("## ======================================== ##\n");
	printf("*** Metric: %s \n", metric);
	printf("*** Model: %s \n", model);
	printf("*** Time period: %s \n", time_period);
	printf("*** Policies: %s \n", policies);
	printf("*** Scenario: %s \n", scenario);
	printf("*** Parameter constant: %s \n", parameter_constant);
	printf("*** Parameter beta_W: %s \n", parameter_beta_W);

	int first_year;
	int ntimes;
	int nmontecarlo;
	int treatment;
	int ntreated;

	if (!strcmp(time_period, "past")) {
		printf(" ERROR: Not implemented ");
		return(1);
	}
	if (!strcmp(time_period, "future_2050")) {
		first_year = 2024;
		ntimes = 27;
	}
	if (!strcmp(time_period, "future_2100")) {
		first_year = 2024;
		ntimes = 77;
	}
	if (!strcmp(time_period, "past")) {
		if (!strcmp(policies, "current")) {
			printf(" ERROR: Not implemented ");
			return(1);
		}
	}
	if (!strcmp(scenario, "treatment")) {
		nmontecarlo = 10000;
		treatment = 1;
		ntreated = ncountries;
	}
	if (!strcmp(scenario, "counterfactual")) {
		nmontecarlo = 10000;
		treatment = 0;
		ntreated = 1;
	}

	int precision;
	if(nmontecarlo % 10 == 0)
	{
		get_precision(nmontecarlo, &precision);
	} else {
		precision = 4;
	}

	char filenameW_temp[120];
	sprintf(filenameW_temp, "./data_W_%s_%s.csv", metric, time_period);
	const char* filenameW = &filenameW_temp[0];

	char filenameX_temp[120];
	sprintf(filenameX_temp, "./data_X_%s_%s.csv", metric, time_period);
	const char* filenameX = &filenameX_temp[0];

	//char filenameP_temp[120];
	//sprintf(filenameP_temp, "./data_P_%s.csv", time_period);
	//const char* filenameP = &filenameP_temp[0];

	const char filenameCountries[120] = "./states.csv";

	char output_directory_temp[120];
	sprintf(output_directory_temp, "./results_%s_%s_%s_%s", metric, model, time_period, policies);
	const char* output_directory = &output_directory_temp[0];

	// allocate regression coefficients of covariates
	double beta_X[nvariables];
	double beta_W;

	// exponential parameter
	double constant;

	// assign values of coefficients
	if (!strcmp(model, "nonlinear")) {
		printf(" ERROR: Not implemented ");
		return(1);
	}

	if (!strcmp(metric, "slpm")) {
	if (!strcmp(model, "linear")) {
		beta_X[0] = 0.12726 ; // climate_concern
		beta_X[1] = -0.16823 ; // coal
		beta_X[2] = 0.41926 ; // log_gdppc
		beta_X[3] = -0.46885 ; // mininggdpshare
		beta_X[4] = -0.38170 ; // pcttransutilempl
		beta_X[5] = 0.23441 ; // popdens
		beta_X[6] = -0.44831 ; // share_evangelical
		beta_X[7] = -0.89127 ; // transutilgdpshare
		beta_W = 1.95002 ; // spatial lag
	}
	if (!strcmp(parameter_constant, "0")) {
		constant = 0.;
	}
	if (!strcmp(parameter_constant, "1")) {
		constant = -4.60517; // p = 0.01
	}
	if (!strcmp(parameter_constant, "2")) {
		constant = -3.91202; // p = 0.02
	}
	if (!strcmp(parameter_constant, "3")) {
		constant = -3.50656; // p = 0.03
	}
	if (!strcmp(parameter_constant, "4")) {
		constant = -3.21888; // p = 0.04
	}
	if (!strcmp(parameter_constant, "5")) {
		constant = -2.99573; // p = 0.05
	}
	if (!strcmp(parameter_constant, "6")) {
		constant = -2.81341; // p = 0.06
	}
	if (!strcmp(parameter_constant, "7")) {
		constant = -2.65926; // p = 0.07
	}
	if (!strcmp(parameter_constant, "8")) {
		constant = -2.52573; // p = 0.08
	}
	if (!strcmp(parameter_constant, "9")) {
		constant = -2.40795; // p = 0.09
	}
	if (!strcmp(parameter_constant, "10")) {
		constant = -2.30259; // p = 0.10
	}
	}

	if (!strcmp(metric, "sld")) {
	if (!strcmp(model, "linear")) {
		beta_X[0] = 0.16644 ; // climate_concern
		beta_X[1] = -0.18639 ; // coal
		beta_X[2] = 0.09896 ; // democrat
		beta_X[3] = 0.39163 ; // log_gdppc
		beta_X[4] = -0.52494 ; // mininggdpshare
		beta_X[5] = -0.39907 ; // pcttransutilempl
		beta_X[6] = 0.32233 ; // popdens
		beta_X[7] = -0.46406 ; // share_evangelical
		beta_X[8] = -0.93443 ; // transutilgdpshare
		beta_W = 1.95002 ; // spatial lag
	}
	if (!strcmp(parameter_constant, "0")) {
		constant = 0.;
	}
	if (!strcmp(parameter_constant, "1")) {
		constant = -4.60517; // p = 0.01
	}
	if (!strcmp(parameter_constant, "2")) {
		constant = -3.91202; // p = 0.02
	}
	if (!strcmp(parameter_constant, "3")) {
		constant = -3.50656; // p = 0.03
	}
	if (!strcmp(parameter_constant, "4")) {
		constant = -3.21888; // p = 0.04
	}
	if (!strcmp(parameter_constant, "5")) {
		constant = -2.99573; // p = 0.05
	}
	if (!strcmp(parameter_constant, "6")) {
		constant = -2.81341; // p = 0.06
	}
	if (!strcmp(parameter_constant, "7")) {
		constant = -2.65926; // p = 0.07
	}
	if (!strcmp(parameter_constant, "8")) {
		constant = -2.52573; // p = 0.08
	}
	if (!strcmp(parameter_constant, "9")) {
		constant = -2.40795; // p = 0.09
	}
	if (!strcmp(parameter_constant, "10")) {
		constant = -2.30259; // p = 0.10
	}
	}

	if (!strcmp(parameter_beta_W, "9")) {
		printf("Use estimated parameter for beta_W");
	}
	if (!strcmp(parameter_beta_W, "0")) {
		beta_W = 0.;
	}
	if (!strcmp(parameter_beta_W, "1")) {
		beta_W = 1.;
	}
	if (!strcmp(parameter_beta_W, "2")) {
		beta_W = 2.;
	}
	if (!strcmp(parameter_beta_W, "3")) {
		beta_W = 3.;
	}
	if (!strcmp(parameter_beta_W, "4")) {
		beta_W = 4.;
	}
	if (!strcmp(parameter_beta_W, "5")) {
		beta_W = 5.;
	}

	char *countrynames[ncountries];
	int t, c;

	// allocate X [ntimes, ncountries, nvariables]
	double ***X = (double ***)malloc(sizeof(double **) * ntimes);
	for (t = 0; t < ntimes; t++)
	{
		X[t] = (double **)malloc(sizeof(double *) * ncountries); 
		for (c = 0; c < ncountries; c++)
		{
			X[t][c] = (double *)malloc(sizeof(double) * nvariables); 
		}
	}

	// allocate Xt [ncountries, nvariables] # covariates
	double **Xt = (double **)malloc(sizeof(double *) * ncountries);
	for (c = 0; c < ncountries; c++)
		Xt[c] = (double *)malloc(sizeof(double) * nvariables); 

	// allocate W [ntimes, ncountries, countries]
	double ***W = (double ***)malloc(sizeof(double **) * ntimes);
	for (t = 0; t < ntimes; t++)
	{
		W[t] = (double **)malloc(sizeof(double *) * ncountries); 
		for (c = 0; c < ncountries; c++)
		{
			W[t][c] = (double *)malloc(sizeof(double) * ncountries); 
		}
	}

	// allocate Wt [ncountries, ncountries] # covariates
	double **Wt = (double **)malloc(sizeof(double *) * ncountries);
	for (c = 0; c < ncountries; c++)
		Wt[c] = (double *)malloc(sizeof(double) * ncountries); 

	// allocate Wt [ncountries, 1] # spatial lag
	double Wtc[ncountries];

	// allocate P [ntimes, ncountries] # actual adoption
	double **P = (double **)malloc(sizeof(double *) * ntimes);
	for (t = 0; t < ntimes; t++)
		P[t] = (double *)malloc(sizeof(double) * ncountries); 

	// allocate Pn [ntimes, ncountries] # adoption in specific run
	double **Pn = (double **)malloc(sizeof(double *) * ntimes);
	for (t = 0; t < ntimes; t++)
		Pn[t] = (double *)malloc(sizeof(double) * ncountries); 

	// allocate Pr [ntimes, ncountries] # store the results here
	double **Pr = (double **)malloc(sizeof(double *) * ntimes);
	for (t = 0; t < ntimes; t++)
		Pr[t] = (double *)malloc(sizeof(double) * ncountries); 

	// allocate Pf [ntimes, ncountries] # first adoption in that simulation
	double **Pf = (double **)malloc(sizeof(double *) * ntimes);
	for (t = 0; t < ntimes; t++)
		Pf[t] = (double *)malloc(sizeof(double) * ncountries); 

	// treatment
	int unit_treated;
	int time_treated = 0;

	// arrays for the hazard rate
	double hazard_X[ncountries];
	double hazard_W[ncountries];
	double hazard_baseline[ncountries];
	double hazard[ncountries];

	double draw; // for random number

	// ========================= assign values =========================

	readCountryNames(filenameCountries, ncountries, countrynames);

	readX(filenameX, ntimes, ncountries, nvariables, first_year, X);

	readW(filenameW, ntimes, ncountries, first_year, W);

	//readP(filenameP, ntimes, ncountries, first_year, P);

	// only for testing and debugging
	int unit_debug = 10;
	if (DEBUG == 1)
	{
		printf("Debug unit: %s\n", countrynames[unit_debug]);
		printf("Debug unit policy in last year: %f\n", P[ntimes-1][unit_debug]);
		nmontecarlo = 2;
		//printf("value of X: %f\n", X[0][0][0]);
		//printf("weight from W: %f\n", W[1][1]);
	}
	//fill_random_2d(ntimes, ncountries, P);
	//fill_random_2d(ncountries, ncountries, W);
	//fill_random_array(ncountries, Wtc);
	//fill_zeros_2d(ntimes, ncountries, P);
	fill_zeros_2d(ntimes, ncountries, P);
	fill_zeros_2d(ntimes, ncountries, Pr);

	int n;

	for(unit_treated = 0; unit_treated < ntreated; unit_treated++)
	{
		if (!strcmp(scenario, "treatment")) {
			printf("Treatment unit: %s\n", countrynames[unit_treated]);
		}

		fill_zeros_2d(ntimes, ncountries, Pr);

		for (n = 0; n < nmontecarlo; n++)
			{
			if (DEBUG == 1)
			{
				printf("Monte Carlo: %i\n", n);
			}

			if (!strcmp(policies, "none")) {
				fill_zeros_2d(ntimes, ncountries, Pn);
			}
			if (!strcmp(policies, "current")) {
				copy_values_2d(ntimes, ncountries, P, Pn);
			}

			Pn[time_treated][unit_treated] = treatment;

			for (t = time_treated+1; t < ntimes; t++)
				{
				if (DEBUG == 1)
				{
					printf("## =========== ##\n");
					printf("Country : %s\n", countrynames[unit_debug]);
					printf("Year : %i\n", t);
				}
				copy_values_2d(ncountries, ncountries, W[t-1], Wt);
				//print_matrix(ncountries, ncountries, countrynames, countrynames, Wt);
				matrixvectorproduct(ncountries, ncountries, Wt, Pn[t-1], Wtc);
				normalise_array(ncountries, ncountries, Wt, Wtc);
				if (DEBUG == 1)
				{
					printf("W: %f\n", Wtc[unit_debug]);
				}
				copy_values_2d(ncountries, nvariables, X[t-1], Xt);
				matrixvectorproduct(ncountries, nvariables, Xt, beta_X, hazard_X);
				if (!strcmp(model, "linear")) {
					scalarvectorproduct(ncountries, beta_W, Wtc, hazard_W);
				}
				if (!strcmp(model, "nonlinear")) {
					hazardnonlinear(ncountries, Wtc, hazard_W);
				}					
				if (DEBUG == 1)
				{
					printf("hazard X: %f\n", hazard_X[unit_debug]);
					printf("hazard W: %f\n", hazard_W[unit_debug]);
				}
				vectorplusvector(ncountries, hazard_X, hazard_W, hazard);
				for(c=0; c < ncountries; c++)
					hazard[c] = exp(hazard[c]);
				if (DEBUG == 1)
				{
					printf("exp hazard total: %f\n", hazard[unit_debug]);
				}
				fill_zeros_array(ncountries, hazard_baseline);
				
				for(c=0; c < ncountries; c++)
				{	
					hazard_baseline[c] = exp(constant);
				}
				if (DEBUG == 1)
				{
					printf("hazard baseline: %f\n", hazard_baseline[unit_debug]);
				}
				vectortimesvector(ncountries, hazard, hazard_baseline, hazard);
				if (DEBUG == 1)
				{
					printf("hazard total * baseline: %f\n", hazard[unit_debug]);
				}
				for(c=0; c < ncountries; c++)
				{
					if (Pn[t-1][c] == 1)
					{
						hazard[c] = 1;
					}
					if (hazard[c] > 1)
					{
						hazard[c] = 1;
					}
					if (hazard[c] < 0)
					{
						hazard[c] = 0;
					}
				}
				if (DEBUG == 1)
				{
					printf("hazard (effective): %f\n", hazard[unit_debug]);
				}
				for(c=0; c < ncountries; c++)
				{
					draw = ((double) rand() / (double) RAND_MAX);
					Pn[t][c] = 0;
					if (DEBUG == 1)
					{
						if (c == unit_debug)
							printf("draw: %f\n", draw);
					}
					if (draw <= hazard[c])
					{
						Pn[t][c] = 1;
					}
				}

				Pn[t][unit_treated] = treatment;
				if (DEBUG == 1)
				{
					printf("policy: %f\n", Pn[t][unit_debug]);
				}
			}
			
			fill_zeros_2d(ntimes, ncountries, Pf);

			for (c = 0; c < ncountries; c++)
			{
				for(t = 0; t < ntimes; t++)
				{
					if (Pn[t][c] == 1.)
					{
						Pf[t][c] = 1.;
						break;
					}
				}
			}

			matrixplusmatrix(ntimes, ncountries, Pr, Pf, Pr);			
		}
		
		double nmontecarlo_double = (double) nmontecarlo;
		normalise_matrix(ntimes, ncountries, nmontecarlo_double, Pr);

		char unit_name[3];
		if (!strcmp(scenario, "treatment")) {
			sprintf(unit_name, "%s", countrynames[unit_treated]);
		}
		if (!strcmp(scenario, "counterfactual")) {
			sprintf(unit_name, "%s", "ANY");
		}
		char string_filename[120];
		sprintf(string_filename,  "%s/result_%s_%i_%s_%s.csv", output_directory, unit_name, treatment, parameter_constant, parameter_beta_W);
		printf("Writing to file: %s\n", string_filename);
		writePr(string_filename, ntimes, ncountries, precision, countrynames, first_year, Pr);
	}
	return(0);
}
