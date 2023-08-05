
#include "PyBind.h"

//---------------------------------------------------------------
// Input data path and file
//---------------------------------------------------------------
py::dict PredictNonlinear_pybind( std::string pathIn,
                                  std::string dataFile,
                                  DF          dataList,
                                  std::string pathOut,
                                  std::string predictFile,
                                  std::string lib,
                                  std::string pred,
                                  int         E,
                                  int         Tp,
                                  int         tau,
                                  std::string columns,
                                  std::string target,
                                  bool        embedded,
                                  bool        verbose,
                                  unsigned    numThreads ) {

    DataFrame< double > PredictDF;

    if ( dataFile.size() ) {
        // dataFile specified, dispatch overloaded PredictNonlinear,
        // ignore dataList
        PredictDF  = PredictNonlinear( pathIn,
                                       dataFile,
                                       pathOut,
                                       predictFile,
                                       lib,
                                       pred,
                                       E,
                                       Tp,
                                       tau,
                                       columns,
                                       target,
                                       embedded,
                                       verbose,
                                       numThreads );
    }
    else if ( dataList.size() ) {
        DataFrame< double > dataFrame = DFToDataFrame( dataList );
        
        PredictDF  = PredictNonlinear( dataFrame,
                                       pathOut,
                                       predictFile,
                                       lib,
                                       pred,
                                       E,
                                       Tp,
                                       tau,
                                       columns,
                                       target,
                                       embedded,
                                       verbose,
                                       numThreads );
    }
    else {
        throw std::runtime_error("PredictNonlinear_pybind(): Invalid input.\n");
    }

    DF       df = DataFrameToDF( PredictDF );
    py::dict D  = DFtoDict( df );
    
    return D;
}
