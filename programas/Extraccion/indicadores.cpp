#include <iostream>
#include <fstream>
#include <string>
#include <ctime>
#include <cstdlib>
#include <sstream>
#include <armadillo>
    
using namespace arma;
using namespace std;

  
int main (int argc, char* argv[]){

  string file0 = argv[1];

  //opennig non-stationary data (prices.txt)
  mat datos;
  datos.load(file0, raw_ascii);
  int N = datos.n_rows;
  int T = datos.n_cols;

  //Returns
  mat R(N,T-1);
  for (int i=0; i<N; i++){
    for (int j=0; j<T-1; j++){
      R(i,j)=(datos(i,j+1)-datos(i,j))/datos(i,j);
      if (isnan(R(i,j))){
	R(i,j)=0.0;
      }
      else if (isinf(R(i,j))){
	R(i,j)=datos(i,j+1);
      }
    }
  }

//Saving data
R.save("returns.txt", raw_ascii);



  return 0;
}