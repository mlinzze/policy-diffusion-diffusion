export CFLAGS=" -g -O2 -lm -ldl -Wall -Wpointer-arith -finline-functions -ffast-math -funroll-all-loops"
export LD_LIBRARY_PATH=/home/manuel/anaconda3/lib

install:
	make clean
	c++ -c functions.c -lm -ldl -o functions.o
	c++ montecarlo.c -I${NETCDF_HOME}/include -I./ -L${NETCDF_HOME}/lib -L./ -lm -ldl -o montecarlo.x functions.o

set0:
	make install
	./montecarlo.x slpm linear future_2050 none counterfactual 5 9
	./montecarlo.x slpm linear future_2050 none treatment 5 9
	./montecarlo.x sld linear future_2050 none counterfactual 5 9
	./montecarlo.x sld linear future_2050 none treatment 5 9

set1:
	make install
	./montecarlo.x slpm linear future_2050 none counterfactual 1 0
	./montecarlo.x slpm linear future_2050 none counterfactual 1 1
	./montecarlo.x slpm linear future_2050 none counterfactual 1 2
	./montecarlo.x slpm linear future_2050 none counterfactual 1 3
	./montecarlo.x slpm linear future_2050 none counterfactual 1 4
	./montecarlo.x slpm linear future_2050 none counterfactual 1 5
	./montecarlo.x slpm linear future_2050 none counterfactual 1 9
	./montecarlo.x slpm linear future_2050 none counterfactual 2 0
	./montecarlo.x slpm linear future_2050 none counterfactual 2 1
	./montecarlo.x slpm linear future_2050 none counterfactual 2 2
	./montecarlo.x slpm linear future_2050 none counterfactual 2 3
	./montecarlo.x slpm linear future_2050 none counterfactual 2 4
	./montecarlo.x slpm linear future_2050 none counterfactual 2 5
	./montecarlo.x slpm linear future_2050 none counterfactual 2 9
	./montecarlo.x slpm linear future_2050 none counterfactual 3 0
	./montecarlo.x slpm linear future_2050 none counterfactual 3 1
	./montecarlo.x slpm linear future_2050 none counterfactual 3 2
	./montecarlo.x slpm linear future_2050 none counterfactual 3 3
	./montecarlo.x slpm linear future_2050 none counterfactual 3 4
	./montecarlo.x slpm linear future_2050 none counterfactual 3 5
	./montecarlo.x slpm linear future_2050 none counterfactual 3 9
	./montecarlo.x slpm linear future_2050 none counterfactual 4 0
	./montecarlo.x slpm linear future_2050 none counterfactual 4 1
	./montecarlo.x slpm linear future_2050 none counterfactual 4 2
	./montecarlo.x slpm linear future_2050 none counterfactual 4 3
	./montecarlo.x slpm linear future_2050 none counterfactual 4 4
	./montecarlo.x slpm linear future_2050 none counterfactual 4 5
	./montecarlo.x slpm linear future_2050 none counterfactual 4 9
	./montecarlo.x slpm linear future_2050 none counterfactual 5 0
	./montecarlo.x slpm linear future_2050 none counterfactual 5 1
	./montecarlo.x slpm linear future_2050 none counterfactual 5 2
	./montecarlo.x slpm linear future_2050 none counterfactual 5 3
	./montecarlo.x slpm linear future_2050 none counterfactual 5 4
	./montecarlo.x slpm linear future_2050 none counterfactual 5 5
	./montecarlo.x slpm linear future_2050 none counterfactual 5 9
	./montecarlo.x slpm linear future_2050 none counterfactual 6 0
	./montecarlo.x slpm linear future_2050 none counterfactual 6 1
	./montecarlo.x slpm linear future_2050 none counterfactual 6 2
	./montecarlo.x slpm linear future_2050 none counterfactual 6 3
	./montecarlo.x slpm linear future_2050 none counterfactual 6 4
	./montecarlo.x slpm linear future_2050 none counterfactual 6 5
	./montecarlo.x slpm linear future_2050 none counterfactual 6 9
	./montecarlo.x slpm linear future_2050 none counterfactual 7 0
	./montecarlo.x slpm linear future_2050 none counterfactual 7 1
	./montecarlo.x slpm linear future_2050 none counterfactual 7 2
	./montecarlo.x slpm linear future_2050 none counterfactual 7 3
	./montecarlo.x slpm linear future_2050 none counterfactual 7 4
	./montecarlo.x slpm linear future_2050 none counterfactual 7 5
	./montecarlo.x slpm linear future_2050 none counterfactual 7 9
	./montecarlo.x slpm linear future_2050 none counterfactual 8 0
	./montecarlo.x slpm linear future_2050 none counterfactual 8 1
	./montecarlo.x slpm linear future_2050 none counterfactual 8 2
	./montecarlo.x slpm linear future_2050 none counterfactual 8 3
	./montecarlo.x slpm linear future_2050 none counterfactual 8 4
	./montecarlo.x slpm linear future_2050 none counterfactual 8 5
	./montecarlo.x slpm linear future_2050 none counterfactual 8 9
	./montecarlo.x slpm linear future_2050 none counterfactual 9 0
	./montecarlo.x slpm linear future_2050 none counterfactual 9 1
	./montecarlo.x slpm linear future_2050 none counterfactual 9 2
	./montecarlo.x slpm linear future_2050 none counterfactual 9 3
	./montecarlo.x slpm linear future_2050 none counterfactual 9 4
	./montecarlo.x slpm linear future_2050 none counterfactual 9 5
	./montecarlo.x slpm linear future_2050 none counterfactual 9 9
	./montecarlo.x slpm linear future_2050 none counterfactual 10 0
	./montecarlo.x slpm linear future_2050 none counterfactual 10 1
	./montecarlo.x slpm linear future_2050 none counterfactual 10 2
	./montecarlo.x slpm linear future_2050 none counterfactual 10 3
	./montecarlo.x slpm linear future_2050 none counterfactual 10 4
	./montecarlo.x slpm linear future_2050 none counterfactual 10 5
	./montecarlo.x slpm linear future_2050 none counterfactual 10 9

all:
	make install
	make set0
	make set1

clean:
	rm -f functions.o