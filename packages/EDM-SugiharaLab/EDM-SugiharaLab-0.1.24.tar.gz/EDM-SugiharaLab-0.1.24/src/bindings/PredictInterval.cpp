
#include "PyBind.h"

//---------------------------------------------------------------
// Input data path and file
//---------------------------------------------------------------
py::dict PredictInterval_pybind( std::string pathIn,
                                 std::string dataFile,
                                 DF          dataList,
                                 std::string pathOut,
                                 std::string predictFile,
                                 std::string lib,
                                 std::string pred,
                                 int         E,
                                 int         tau,
                                 std::string columns,
                                 std::string target,
                                 bool        embedded,
                                 bool        verbose,
                                 unsigned    numThreads ) {

    DataFrame< double > PredictDF;

    if ( dataFile.size() ) {
        // dataFile specified, dispatch overloaded PredictInterval,
        // ignore dataList
        PredictDF = PredictInterval( pathIn,
                                     dataFile,
                                     pathOut,
                                     predictFile,
                                     lib,
                                     pred,
                                     E,
                                     tau,
                                     columns,
                                     target,
                                     embedded,
                                     verbose,
                                     numThreads );
    }
    else if ( dataList.size() ) {
        DataFrame< double > dataFrame = DFToDataFrame( dataList );
        
        PredictDF = PredictInterval( dataFrame,
                                     pathOut,
                                     predictFile,
                                     lib,
                                     pred,
                                     E,
                                     tau,
                                     columns,
                                     target,
                                     embedded,
                                     verbose,
                                     numThreads );
    }
    else {
        throw std::runtime_error("PredictInterval_pybind(): Invalid input.\n");
    }

    DF       df = DataFrameToDF( PredictDF );
    py::dict D  = DFtoDict( df );
    
    return D;
}
