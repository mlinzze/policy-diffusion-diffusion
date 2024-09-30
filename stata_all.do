/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_A06sln.csv
stset stop, failure(event==1) id(id)

/* models */
stcox climate_action_plan_21_sln pc01 pc03 pc08 pc09 pc12 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_A06sln.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_A06sln.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_A06sld.csv
stset stop, failure(event==1) id(id)

/* models */
stcox climate_action_plan_21_sld pc01 pc03 pc08 pc09 pc12 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_A06sld.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_A06sld.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_A06slg.csv
stset stop, failure(event==1) id(id)

/* models */
stcox climate_action_plan_21_slg pc01 pc03 pc08 pc09 pc12 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_A06slg.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_A06slg.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_A00slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox climate_action_plan_21_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_A00slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_A00slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_A06slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox climate_action_plan_21_slp pc01 pc03 pc08 pc09 pc12 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_A06slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_A06slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_A06slpm.csv
stset stop, failure(event==1) id(id)

/* models */
stcox climate_action_plan_21_slpm pc01 pc03 pc08 pc09 pc12 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_A06slpm.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_A06slpm.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_B06sln.csv
stset stop, failure(event==1) id(id)

/* models */
stcox community_solar_sln pc01 pc03 pc05 pc08 pc09 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_B06sln.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_B06sln.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_B06sld.csv
stset stop, failure(event==1) id(id)

/* models */
stcox community_solar_sld pc01 pc03 pc05 pc08 pc09 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_B06sld.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_B06sld.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_B06slg.csv
stset stop, failure(event==1) id(id)

/* models */
stcox community_solar_slg pc01 pc03 pc05 pc08 pc09 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_B06slg.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_B06slg.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_B00slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox community_solar_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_B00slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_B00slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_B06slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox community_solar_slp pc01 pc03 pc05 pc08 pc09 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_B06slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_B06slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_B06slpm.csv
stset stop, failure(event==1) id(id)

/* models */
stcox community_solar_slpm pc01 pc03 pc05 pc08 pc09 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_B06slpm.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_B06slpm.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_C06sln.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pc01 pc03 pc05 pc07 pc11 pc13 environment_ca_car_emission_sln , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_C06sln.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_C06sln.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_C06sld.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pc01 pc03 pc05 pc07 pc11 pc13 environment_ca_car_emission_sld , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_C06sld.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_C06sld.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_C06slg.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pc01 pc03 pc05 pc07 pc11 pc13 environment_ca_car_emission_slg , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_C06slg.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_C06slg.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_C00slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox environment_ca_car_emission_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_C00slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_C00slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_C06slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pc01 pc03 pc05 pc07 pc11 pc13 environment_ca_car_emission_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_C06slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_C06slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_C06slpm.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pc01 pc03 pc05 pc07 pc11 pc13 environment_ca_car_emission_slpm , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_C06slpm.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_C06slpm.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_D06sln.csv
stset stop, failure(event==1) id(id)

/* models */
stcox environment_ghg_cap_21_sln pc01 pc03 pc09 pc11 pc12 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_D06sln.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_D06sln.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_D06sld.csv
stset stop, failure(event==1) id(id)

/* models */
stcox environment_ghg_cap_21_sld pc01 pc03 pc09 pc11 pc12 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_D06sld.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_D06sld.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_D06slg.csv
stset stop, failure(event==1) id(id)

/* models */
stcox environment_ghg_cap_21_slg pc01 pc03 pc09 pc11 pc12 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_D06slg.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_D06slg.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_D00slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox environment_ghg_cap_21_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_D00slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_D00slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_D06slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox environment_ghg_cap_21_slp pc01 pc03 pc09 pc11 pc12 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_D06slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_D06slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_D06slpm.csv
stset stop, failure(event==1) id(id)

/* models */
stcox environment_ghg_cap_21_slpm pc01 pc03 pc09 pc11 pc12 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_D06slpm.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_D06slpm.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_E06sln.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pc01 pc02 pc03 pc09 pc11 pc12 environment_publicbenefit_f_sln , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_E06sln.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_E06sln.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_E06sld.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pc01 pc02 pc03 pc09 pc11 pc12 environment_publicbenefit_f_sld , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_E06sld.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_E06sld.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_E06slg.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pc01 pc02 pc03 pc09 pc11 pc12 environment_publicbenefit_f_slg , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_E06slg.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_E06slg.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_E00slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox environment_publicbenefit_f_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_E00slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_E00slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_E06slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pc01 pc02 pc03 pc09 pc11 pc12 environment_publicbenefit_f_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_E06slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_E06slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_E06slpm.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pc01 pc02 pc03 pc09 pc11 pc12 environment_publicbenefit_f_slpm , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_E06slpm.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_E06slpm.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_F06sln.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pc01 pc02 pc03 pc07 pc11 pc13 environment_utility_deregul_sln , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_F06sln.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_F06sln.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_F06sld.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pc01 pc02 pc03 pc07 pc11 pc13 environment_utility_deregul_sld , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_F06sld.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_F06sld.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_F06slg.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pc01 pc02 pc03 pc07 pc11 pc13 environment_utility_deregul_slg , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_F06slg.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_F06slg.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_F00slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox environment_utility_deregul_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_F00slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_F00slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_F06slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pc01 pc02 pc03 pc07 pc11 pc13 environment_utility_deregul_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_F06slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_F06slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_F06slpm.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pc01 pc02 pc03 pc07 pc11 pc13 environment_utility_deregul_slpm , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_F06slpm.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_F06slpm.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_G06sln.csv
stset stop, failure(event==1) id(id)

/* models */
stcox fgd_21_sln pc01 pc03 pc04 pc07 pc09 pc12 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_G06sln.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_G06sln.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_G06sld.csv
stset stop, failure(event==1) id(id)

/* models */
stcox fgd_21_sld pc01 pc03 pc04 pc07 pc09 pc12 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_G06sld.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_G06sld.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_G06slg.csv
stset stop, failure(event==1) id(id)

/* models */
stcox fgd_21_slg pc01 pc03 pc04 pc07 pc09 pc12 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_G06slg.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_G06slg.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_G00slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox fgd_21_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_G00slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_G00slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_G06slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox fgd_21_slp pc01 pc03 pc04 pc07 pc09 pc12 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_G06slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_G06slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_G06slpm.csv
stset stop, failure(event==1) id(id)

/* models */
stcox fgd_21_slpm pc01 pc03 pc04 pc07 pc09 pc12 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_G06slpm.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_G06slpm.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_H06sln.csv
stset stop, failure(event==1) id(id)

/* models */
stcox ghg_standards_21_sln pc01 pc03 pc04 pc09 pc12 pc14 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_H06sln.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_H06sln.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_H06sld.csv
stset stop, failure(event==1) id(id)

/* models */
stcox ghg_standards_21_sld pc01 pc03 pc04 pc09 pc12 pc14 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_H06sld.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_H06sld.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_H06slg.csv
stset stop, failure(event==1) id(id)

/* models */
stcox ghg_standards_21_slg pc01 pc03 pc04 pc09 pc12 pc14 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_H06slg.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_H06slg.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_H00slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox ghg_standards_21_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_H00slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_H00slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_H06slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox ghg_standards_21_slp pc01 pc03 pc04 pc09 pc12 pc14 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_H06slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_H06slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_H06slpm.csv
stset stop, failure(event==1) id(id)

/* models */
stcox ghg_standards_21_slpm pc01 pc03 pc04 pc09 pc12 pc14 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_H06slpm.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_H06slpm.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_I06sln.csv
stset stop, failure(event==1) id(id)

/* models */
stcox netmeter_yearadopted_21_sln pc01 pc03 pc04 pc09 pc12 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_I06sln.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_I06sln.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_I06sld.csv
stset stop, failure(event==1) id(id)

/* models */
stcox netmeter_yearadopted_21_sld pc01 pc03 pc04 pc09 pc12 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_I06sld.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_I06sld.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_I06slg.csv
stset stop, failure(event==1) id(id)

/* models */
stcox netmeter_yearadopted_21_slg pc01 pc03 pc04 pc09 pc12 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_I06slg.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_I06slg.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_I00slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox netmeter_yearadopted_21_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_I00slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_I00slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_I06slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox netmeter_yearadopted_21_slp pc01 pc03 pc04 pc09 pc12 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_I06slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_I06slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_I06slpm.csv
stset stop, failure(event==1) id(id)

/* models */
stcox netmeter_yearadopted_21_slpm pc01 pc03 pc04 pc09 pc12 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_I06slpm.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_I06slpm.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_J06sln.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pace_21_sln pc01 pc02 pc03 pc08 pc11 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_J06sln.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_J06sln.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_J06sld.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pace_21_sld pc01 pc02 pc03 pc08 pc11 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_J06sld.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_J06sld.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_J06slg.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pace_21_slg pc01 pc02 pc03 pc08 pc11 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_J06slg.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_J06slg.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_J00slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pace_21_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_J00slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_J00slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_J06slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pace_21_slp pc01 pc02 pc03 pc08 pc11 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_J06slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_J06slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_J06slpm.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pace_21_slpm pc01 pc02 pc03 pc08 pc11 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_J06slpm.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_J06slpm.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_K06sln.csv
stset stop, failure(event==1) id(id)

/* models */
stcox public_building_standards_sln pc01 pc02 pc03 pc08 pc10 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_K06sln.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_K06sln.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_K06sld.csv
stset stop, failure(event==1) id(id)

/* models */
stcox public_building_standards_sld pc01 pc02 pc03 pc08 pc10 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_K06sld.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_K06sld.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_K06slg.csv
stset stop, failure(event==1) id(id)

/* models */
stcox public_building_standards_slg pc01 pc02 pc03 pc08 pc10 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_K06slg.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_K06slg.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_K00slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox public_building_standards_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_K00slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_K00slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_K06slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox public_building_standards_slp pc01 pc02 pc03 pc08 pc10 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_K06slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_K06slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_K06slpm.csv
stset stop, failure(event==1) id(id)

/* models */
stcox public_building_standards_slpm pc01 pc02 pc03 pc08 pc10 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_K06slpm.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_K06slpm.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_L06sln.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w4_electric_decoupling_21_sln pc01 pc02 pc03 pc08 pc09 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_L06sln.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_L06sln.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_L06sld.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w4_electric_decoupling_21_sld pc01 pc02 pc03 pc08 pc09 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_L06sld.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_L06sld.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_L06slg.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w4_electric_decoupling_21_slg pc01 pc02 pc03 pc08 pc09 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_L06slg.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_L06slg.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_L00slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w4_electric_decoupling_21_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_L00slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_L00slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_L06slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w4_electric_decoupling_21_slp pc01 pc02 pc03 pc08 pc09 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_L06slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_L06slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_L06slpm.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w4_electric_decoupling_21_slpm pc01 pc02 pc03 pc08 pc09 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_L06slpm.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_L06slpm.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_M06sln.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w4_environment_state_rps_21_sln pc01 pc03 pc04 pc09 pc12 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_M06sln.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_M06sln.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_M06sld.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w4_environment_state_rps_21_sld pc01 pc03 pc04 pc09 pc12 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_M06sld.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_M06sld.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_M06slg.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w4_environment_state_rps_21_slg pc01 pc03 pc04 pc09 pc12 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_M06slg.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_M06slg.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_M00slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w4_environment_state_rps_21_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_M00slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_M00slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_M06slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w4_environment_state_rps_21_slp pc01 pc03 pc04 pc09 pc12 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_M06slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_M06slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_M06slpm.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w4_environment_state_rps_21_slpm pc01 pc03 pc04 pc09 pc12 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_M06slpm.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_M06slpm.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_N06sln.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w4_gas_decoupling_21_sln pc01 pc02 pc03 pc05 pc08 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_N06sln.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_N06sln.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_N06sld.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w4_gas_decoupling_21_sld pc01 pc02 pc03 pc05 pc08 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_N06sld.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_N06sld.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_N06slg.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w4_gas_decoupling_21_slg pc01 pc02 pc03 pc05 pc08 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_N06slg.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_N06slg.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_N00slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w4_gas_decoupling_21_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_N00slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_N00slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_N06slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w4_gas_decoupling_21_slp pc01 pc02 pc03 pc05 pc08 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_N06slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_N06slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_N06slpm.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w4_gas_decoupling_21_slpm pc01 pc02 pc03 pc05 pc08 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_N06slpm.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_N06slpm.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_O06sln.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pc01 pc02 pc03 pc07 pc09 pc13 w_environment_solar_taxcred_sln , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_O06sln.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_O06sln.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_O06sld.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pc01 pc02 pc03 pc07 pc09 pc13 w_environment_solar_taxcred_sld , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_O06sld.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_O06sld.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_O06slg.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pc01 pc02 pc03 pc07 pc09 pc13 w_environment_solar_taxcred_slg , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_O06slg.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_O06slg.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_O00slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_environment_solar_taxcred_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_O00slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_O00slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_O06slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pc01 pc02 pc03 pc07 pc09 pc13 w_environment_solar_taxcred_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_O06slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_O06slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_O06slpm.csv
stset stop, failure(event==1) id(id)

/* models */
stcox pc01 pc02 pc03 pc07 pc09 pc13 w_environment_solar_taxcred_slpm , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_O06slpm.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_O06slpm.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_P06sln.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_complete_streets_21_sln pc01 pc02 pc03 pc04 pc05 pc15 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_P06sln.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_P06sln.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_P06sld.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_complete_streets_21_sld pc01 pc02 pc03 pc04 pc05 pc15 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_P06sld.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_P06sld.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_P06slg.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_complete_streets_21_slg pc01 pc02 pc03 pc04 pc05 pc15 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_P06slg.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_P06slg.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_P00slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_complete_streets_21_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_P00slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_P00slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_P06slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_complete_streets_21_slp pc01 pc02 pc03 pc04 pc05 pc15 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_P06slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_P06slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_P06slpm.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_complete_streets_21_slpm pc01 pc02 pc03 pc04 pc05 pc15 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_P06slpm.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_P06slpm.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_Q06sln.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_ee_21_sln pc01 pc02 pc03 pc04 pc09 pc15 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_Q06sln.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_Q06sln.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_Q06sld.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_ee_21_sld pc01 pc02 pc03 pc04 pc09 pc15 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_Q06sld.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_Q06sld.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_Q06slg.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_ee_21_slg pc01 pc02 pc03 pc04 pc09 pc15 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_Q06slg.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_Q06slg.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_Q00slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_ee_21_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_Q00slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_Q00slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_Q06slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_ee_21_slp pc01 pc02 pc03 pc04 pc09 pc15 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_Q06slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_Q06slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_Q06slpm.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_ee_21_slpm pc01 pc02 pc03 pc04 pc09 pc15 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_Q06slpm.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_Q06slpm.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_R06sln.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_gg_rr_21_sln pc01 pc03 pc05 pc09 pc10 pc12 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_R06sln.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_R06sln.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_R06sld.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_gg_rr_21_sld pc01 pc03 pc05 pc09 pc10 pc12 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_R06sld.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_R06sld.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_R06slg.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_gg_rr_21_slg pc01 pc03 pc05 pc09 pc10 pc12 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_R06slg.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_R06slg.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_R00slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_gg_rr_21_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_R00slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_R00slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_R06slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_gg_rr_21_slp pc01 pc03 pc05 pc09 pc10 pc12 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_R06slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_R06slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_R06slpm.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_gg_rr_21_slpm pc01 pc03 pc05 pc09 pc10 pc12 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_R06slpm.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_R06slpm.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_S06sln.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_ghg_targets_21_sln pc01 pc03 pc05 pc09 pc11 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_S06sln.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_S06sln.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_S06sld.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_ghg_targets_21_sld pc01 pc03 pc05 pc09 pc11 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_S06sld.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_S06sld.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_S06slg.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_ghg_targets_21_slg pc01 pc03 pc05 pc09 pc11 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_S06slg.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_S06slg.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_S00slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_ghg_targets_21_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_S00slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_S00slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_S06slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_ghg_targets_21_slp pc01 pc03 pc05 pc09 pc11 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_S06slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_S06slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_S06slpm.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_ghg_targets_21_slpm pc01 pc03 pc05 pc09 pc11 pc13 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_S06slpm.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_S06slpm.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_T06sln.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_mgpo_21_sln pc01 pc03 pc06 pc08 pc09 pc10 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_T06sln.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_T06sln.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_T06sld.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_mgpo_21_sld pc01 pc03 pc06 pc08 pc09 pc10 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_T06sld.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_T06sld.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_T06slg.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_mgpo_21_slg pc01 pc03 pc06 pc08 pc09 pc10 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_T06slg.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_T06slg.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_T00slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_mgpo_21_slp , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_T00slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_T00slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_T06slp.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_mgpo_21_slp pc01 pc03 pc06 pc08 pc09 pc10 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_T06slp.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_T06slp.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
/* ssc install estout */
clear all
import delimited ./data/data_T06slpm.csv
stset stop, failure(event==1) id(id)

/* models */
stcox w_mgpo_21_slpm pc01 pc03 pc06 pc08 pc09 pc10 , nohr robust cluster(id)   iterate(500)
estat phtest, detail
mat g= r(chi2), r(df)
estout mat(g) using ./results/phtest_T06slpm.txt, delimiter(,) replace
estimates store model1
estout model1 using ./results/coeffs_T06slpm.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
