# libsoc - Library to handle standardised output files
# Copyright (C) 2015 Rikard Nordgren
# 
# This file was autogenerated and should not be edited
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
# 
# his library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, see <http://www.gnu.org/licenses/>.

# Description of the so structure

# List of classes that need name as input to _new
need_name = [
    'Table', 'Matrix', 'ExternalFile', 'SimulationSubType'
]

namespaces = {
    'Table' : 'so',
    'Matrix' : 'so',
    'ExternalFile' : 'so',
    'SimulationSubType' : 'so',
}

structure = {
    'SO' : {
        'children' : [
            { 'name' : 'Description', 'type' : 'type_string', 'prefix' : 'ct' },
            { 'name' : 'PharmMLRef', 'type' : 'PharmMLRef' },
            { 'name' : 'SOBlock', 'type' : 'SOBlock', 'array' : True },
        ],
        'attributes' : [
            { 'name' : 'id', 'type' : 'type_string' },
            { 'name' : 'metadataFile', 'type' : 'type_string' },
        ],
        'fixed_attributes' : [
            { 'name' : "xmlns", 'value' : "http://www.pharmml.org/so/0.3/StandardisedOutput" },
            { 'name' : "xmlns:xsi", 'value' : "http://www.w3.org/2001/XMLSchema-instance" },
            { 'name' : "xmlns:ds", 'value' : "http://www.pharmml.org/pharmml/0.8/Dataset" },
            { 'name' : "xmlns:ct", 'value' : "http://www.pharmml.org/pharmml/0.8/CommonTypes" },
            { 'name' : "xmlns:po", 'value' : "http://www.pharmml.org/probonto/ProbOnto" },
            { 'name' : "xsi:schemaLocation", 'value' : "http://www.pharmml.org/so/0.3/StandardisedOutput" },
            { 'name' : "implementedBy", 'value' : "MJS" },
            { 'name' : "writtenVersion", 'value' : "0.3" },
        ],
        'xpath' : 'SO',
        'fields' : [ 'int error;' ],
        'namespace' : 'so'
    },
    'PharmMLRef' : {
        'children' : [
            { 'name' : 'Description', 'type' : 'type_string', 'prefix' : 'ct' },
        ],
        'attributes' : [
            { 'name' : 'name', 'type' : 'type_string' },
            { 'name' : 'id', 'type' : 'type_string' },
        ],
        'xpath' : 'SO/PharmMLRef',
        'namespace' : 'so'
    },
    'SOBlock' : {
        'children' : [
            { 'name' : 'ToolSettings', 'type' : 'ToolSettings' },
            { 'name' : 'RawResults', 'type' : 'RawResults' },
            { 'name' : 'TaskInformation', 'type' : 'TaskInformation' },
            { 'name' : 'Estimation', 'type' : 'Estimation' },
            { 'name' : 'Simulation', 'type' : 'Simulation' },
            { 'name' : 'ModelDiagnostic', 'type' : 'ModelDiagnostic' },
            { 'name' : 'OptimalDesign', 'type' : 'OptimalDesign' },
        ],
        'attributes' : [
            { 'name' : 'blkId', 'type' : 'type_string' },
        ],
        'xpath' : 'SO/SOBlock',
        'namespace' : 'so'
    },
    'ToolSettings' : {
        'children' : [
            { 'name' : 'File', 'type' : 'ExternalFile', 'array' : True },
        ],
        'xpath' : 'SO/SOBlock/ToolSettings',
        'namespace' : 'so'
    },
    'RawResults' : {
        'children' : [
            { 'name' : 'DataFile', 'type' : 'Table', 'array' : True },
            { 'name' : 'GraphicsFile', 'type' : 'ExternalFile', 'array' : True },
        ],
        'xpath' : 'SO/SOBlock/RawResults',
        'namespace' : 'so'
    },
    'TaskInformation' : {
        'children' : [
            { 'name' : 'Message', 'type' : 'Message', 'array' : True },
            { 'name' : 'OutputFilePath', 'type' : 'ExternalFile', 'array' : True },
            { 'name' : 'RunTime', 'type' : 'type_real' },
            { 'name' : 'NumberChains', 'type' : 'type_int' },
            { 'name' : 'NumberIterations', 'type' : 'type_int' },
        ],
        'xpath' : 'SO/SOBlock/TaskInformation',
        'namespace' : 'so'
    },
    'Message' : {
        'children' : [
            { 'name' : 'Toolname', 'type' : 'type_string' },
            { 'name' : 'Name', 'type' : 'type_string' },
            { 'name' : 'Content', 'type' : 'type_string' },
            { 'name' : 'Severity', 'type' : 'type_int' },
        ],
        'attributes' : [
            { 'name' : 'type', 'type' : 'type_string' },
        ],
        'xpath' : 'SO/SOBlock/TaskInformation/Message',
        'namespace' : 'so'
    },
    'Estimation' : {
        'children' : [
            { 'name' : 'PopulationEstimates', 'type' : 'PopulationEstimates' },
            { 'name' : 'PrecisionPopulationEstimates', 'type' : 'PrecisionPopulationEstimates' },
            { 'name' : 'IndividualEstimates', 'type' : 'IndividualEstimates' },
            { 'name' : 'Residuals', 'type' : 'Residuals' },
            { 'name' : 'Predictions', 'type' : 'Table' },
            { 'name' : 'OFMeasures', 'type' : 'OFMeasures' },
        ],
        'xpath' : 'SO/SOBlock/Estimation',
        'namespace' : 'so'
    },
    'PopulationEstimates' : {
        'children' : [
            { 'name' : 'MLE', 'type' : 'Table' },
            { 'name' : 'Bayesian', 'type' : 'Bayesian' },
            { 'name' : 'OtherMethod', 'type' : 'OtherMethod' }
        ],
        'xpath' : 'SO/SOBlock/Estimation/PopulationEstimates',
        'namespace' : 'so'
    },
    'OtherMethod' : {
        'children' : [
            { 'name' : 'Mean', 'type' : 'Table' },
            { 'name' : 'Median', 'type' : 'Table' }
        ],
        'attributes' : [
            { 'name': 'method', 'type' : 'type_string' },
        ],
        'xpath' : 'SO/SOBlock/Estimation/PopulationEstimates/OtherMethod',
        'namespace' : 'so'
    },
    'Bayesian' : {
        'children' : [
            { 'name' : 'PosteriorMean', 'type' : 'Table' },
            { 'name' : 'PosteriorMedian', 'type' : 'Table' },
            { 'name' : 'PosteriorMode', 'type' : 'Table' }
        ],
        'xpath' : 'SO/SOBlock/Estimation/PopulationEstimates/Bayesian',
        'namespace' : 'so'
    },
    'PrecisionPopulationEstimates' : {
        'children' : [
            { 'name' : 'MLE', 'type' : 'MLE' },
            { 'name' : 'Bayesian', 'type' : 'Bayesian_PPE' },
            { 'name' : 'OtherMethod', 'type' : 'OtherMethod_PPE' },
        ],
        'xpath' : 'SO/SOBlock/Estimation/PrecisionPopulationEstimates',
        'namespace' : 'so'
    },
    'OtherMethod_PPE' : {
        'children' : [
            { 'name' : 'CovarianceMatrix', 'type' : 'Matrix' },
            { 'name' : 'CorrelationMatrix', 'type' : 'Matrix' },
            { 'name' : 'StandardDeviation', 'type' : 'Table' },
            { 'name' : 'StandardError', 'type' : 'Table' },
            { 'name' : 'AsymptoticCI', 'type' : 'Table' },
            { 'name' : 'PercentilesCI', 'type' : 'Table' },
        ],
        'xpath' : 'SO/SOBlock/Estimation/PrecisionPopulationEstimates/OtherMethod',
        'namespace' : 'so'
    },
    'Bayesian_PPE' : {
        'element_name' : 'Bayesian',
        'children' : [
            { 'name' : 'StandardDeviationPosterior', 'type' : 'Table' },
            { 'name' : 'PercentilesCI', 'type' : 'Table' },
        ],
        'xpath' : 'SO/SOBlock/Estimation/PrecisionPopulationEstimates/Bayesian',
        'namespace' : 'so'
    },
    'MLE' : {
        'children' : [
            { 'name' : 'FIM', 'type' : 'Matrix' },
            { 'name' : 'CovarianceMatrix', 'type' : 'Matrix' },
            { 'name' : 'CorrelationMatrix', 'type' : 'Matrix' },
            { 'name' : 'StandardError', 'type' : 'Table' },
            { 'name' : 'RelativeStandardError', 'type' : 'Table' },
            { 'name' : 'AsymptoticCI', 'type' : 'Table' },
            { 'name' : 'ConditionNumber', 'type' : 'type_real' },
        ],
        'xpath' : 'SO/SOBlock/Estimation/PrecisionPopulationEstimates/MLE', 
        'namespace' : 'so'
    },
    'IndividualEstimates' : {
        'children' : [
            { 'name' : 'Estimates', 'type' : 'Estimates' },
            { 'name' : 'RandomEffects', 'type' : 'RandomEffects_IE' },
            { 'name' : 'EtaShrinkage', 'type' : 'Table' },
        ],
        'xpath' : 'SO/SOBlock/Estimation/IndividualEstimates',
        'namespace' : 'so'
    },
    'Estimates' : {
        'children' : [
            { 'name' : 'Mean', 'type' : 'Table' },
            { 'name' : 'Median', 'type' : 'Table' },
            { 'name' : 'Mode', 'type' : 'Table' },
            { 'name' : 'Samples', 'type' : 'Table' },
        ],
        'xpath' : 'SO/SOBlock/Estimation/IndividualEstimates/Estimates',
        'namespace' : 'so'
    },
    'RandomEffects_IE' : {
        'element_name' : 'RandomEffects',
        'children' : [
            { 'name' : 'EffectMean', 'type' : 'Table' },
            { 'name' : 'EffectMedian', 'type' : 'Table' },
            { 'name' : 'EffectMode', 'type' : 'Table' },
            { 'name' : 'Samples', 'type' : 'Table' },
        ],
        'xpath' : 'SO/SOBlock/Estimation/IndividualEstimates/RandomEffects',
        'namespace' : 'so'
    },
    'Residuals' : {
        'children' : [
            { 'name' : 'ResidualTable', 'type' : 'Table' },
            { 'name' : 'EpsShrinkage', 'type' : 'Table' }
        ],
        'xpath' : 'SO/SOBlock/Estimation/Residuals',
        'namespace' : 'so'
    },
    'OFMeasures' : {
        'children' : [
            { 'name' : 'Likelihood', 'type' : 'type_real' },
            { 'name' : 'LogLikelihood', 'type' : 'type_real' },
            { 'name' : 'Deviance', 'type' : 'type_real' },
            { 'name' : 'IndividualContribtoLL', 'type' : 'Table' },
        ],
        'xpath' : 'SO/SOBlock/Estimation/OFMeasures',
        'namespace' : 'so'
    },
    'Simulation' : {
        'children' : [
            { 'name' : 'SimulationBlock', 'type' : 'SimulationBlock', 'array' : True },
        ],
        'xpath' : 'SO/SOBlock/Simulation',
        'namespace' : 'so'
    },
    'SimulationBlock' : {
        'children' : [
            { 'name' : 'SimulatedProfiles', 'type' : 'SimulationSubType', 'array' : True },
            { 'name' : 'IndivParameters', 'type' : 'SimulationSubType', 'array' : True },
            { 'name' : 'RandomEffects', 'type' : 'SimulationSubType', 'array' : True },
            { 'name' : 'Covariates', 'type' : 'SimulationSubType', 'array' : True },
            { 'name' : 'PopulationParameters', 'type' : 'SimulationSubType', 'array' : True },
            { 'name' : 'Dosing', 'type' : 'SimulationSubType', 'array' : True },
            { 'name' : 'RawResultsFile', 'type' : 'ExternalFile' },
        ],
        'attributes' : [
            { 'name' : 'replicate', 'type' : 'type_int' },
        ],
        'xpath' : 'SO/SOBlock/Simulation/SimulationBlock',
        'namespace' : 'so'
    },
    #'SimulationSubType' : {
    #    'extends' : 'Table',
    #    'attributes' : [
    #        { 'name' : 'name', 'type' : 'type_string' },
    #        { 'name' : 'extFileNo', 'type' : 'type_int' },
    #    ],
    #    'xpath' : 'SimulationSubType',
    #    'namespace' : 'so'
    #},
    'ExternalFile' : {
        'children' : [
            { 'name' : 'Description' , 'type' : 'type_string', 'prefix' : 'ct' },
            { 'name' : 'path', 'type' : 'type_string', 'prefix' : 'ds' },
            { 'name' : 'format', 'type' : 'type_string', 'prefix' : 'ds' },
            { 'name' : 'delimiter', 'type' : 'type_string', 'prefix' : 'ds' },
            { 'name' : 'MissingData', 'type' : 'MissingData', 'array' : True, 'prefix' : 'ds' }, 
        ],
        'attributes' : [
            { 'name' : 'oid', 'type' : 'type_string' },
        ],
        'xpath' : 'ExternalFile',
        'namespace' : 'so'
    },
    'MissingData' : {
        'attributes' : [
            { 'name' : 'dataCode', 'type' : 'type_string' },
            { 'name' : 'missingDataType', 'type' : 'type_string' },
        ],
        'xpath' : 'MissingData',
        'namespace' : 'so'
    },
    'OptimalDesign' : {
        'children' : [
            { 'name' : 'OptimalDesignBlock', 'type' : 'OptimalDesignBlock', 'array' : True },
        ],
        'attributes' : [
            { 'name' : 'type', 'type' : 'type_string' },
        ],
        'xpath' : 'SO/SOBlock/OptimalDesign',
        'namespace' : 'so'
    },
    'OptimalDesignBlock' : {
        'children' : [
            { 'name' : 'FIM', 'type' : 'Matrix' },
            { 'name' : 'CovarianceMatrix', 'type' : 'Matrix' },
            { 'name' : 'ParameterPrecision', 'type' : 'Table' },
            { 'name' : 'Criteria', 'type' : 'Table' },
            { 'name' : 'Tests', 'type' : 'Table' },
            { 'name' : 'SimulatedData', 'type' : 'ExternalFile' },
            { 'name' : 'Design', 'type' : 'ExternalFile' },
        ],
        'attributes' : [
            { 'name' : 'blockNumber', 'type' : 'type_int' },
        ],
        'xpath' : 'SO/SOBlock/OptimalDesign/OptimalDesignBlock',
        'namespace' : 'so'
    },
    'ModelDiagnostic' : {
        'children' : [
            { 'name' : 'DiagnosticPlotsStructuralModel', 'type' : 'DiagnosticPlotsStructuralModel' },
            { 'name' : 'DiagnosticPlotsIndividualParams', 'type' : 'Table' },
        ],
        'xpath' : 'SO/SOBlock/ModelDiagnostic',
        'namespace' : 'so'
    },
    'DiagnosticPlotsStructuralModel' : {
        'children' : [
            { 'name' : 'IndivFits', 'type' : 'IndivFits' },
            { 'name' : 'IndivPredictionVsObserv', 'type' : 'Table' },
            { 'name' : 'VPC', 'type' : 'Table' },
        ],
        'xpath' : 'SO/SOBlock/ModelDiagnostic/DiagnosticPlotsStructuralModel',
        'namespace' : 'so'
    },
    'IndivFits' : {
        'children' : [
            { 'name' : 'ObservationTable', 'type' : 'Table' },
            { 'name' : 'PredictionTable', 'type' : 'Table' },
        ],
        'xpath' : 'SO/SOBlock/ModelDiagnostic/DiagnosticPlotsStructuralModel/IndivFits',
        'namespace' : 'so'
    },

   
    # PharmML
    'PharmML' : {
        'fixed_attributes' : [
            { 'name' : 'xmlns', 'value' : 'http://www.pharmml.org/pharmml/0.8/PharmML' },
	    { 'name' : 'xmlns:xsi', 'value' : 'http://www.w3.org/2001/XMLSchema-instance' }, 
            { 'name' : 'xsi:schemaLocation', 'value' : 'http://www.pharmml.org/pharmml/0.8/PharmML' },
            { 'name' : 'xmlns:math', 'value' : 'http://www.pharmml.org/pharmml/0.8/Maths' },
	    { 'name' : 'xmlns:ct', 'value' : 'http://www.pharmml.org/pharmml/0.8/CommonTypes' },
            { 'name' : 'xmlns:ds', 'value' : 'http://www.pharmml.org/pharmml/0.8/Dataset' },
	    { 'name' : 'xmlns:mdef', 'value' : 'http://www.pharmml.org/pharmml/0.8/ModelDefinition' },
	    { 'name' : 'xmlns:mstep', 'value' : 'http://www.pharmml.org/pharmml/0.8/ModellingSteps' },
            { 'name' : 'xmlns:design', 'value' : 'http://www.pharmml.org/pharmml/0.8/TrialDesign' },
            { 'name' : "writtenVersion", 'value' : "0.8" },
         ],
        'children' : [
            { 'name' : 'Name', 'type' : 'type_string', 'prefix' : 'ct' },
            { 'name' : 'IndependentVariable', 'type' : 'IndependentVariable', 'array' : True },
            { 'name' : 'ModelDefinition', 'type' : 'ModelDefinition' },
        ],
        'fields' : [ 'int error;' ],
        'xpath' : 'PharmML',
        'namespace' : 'pharmml'
    },
    'IndependentVariable' : {
        'attributes' : [
            { 'name' : 'id', 'type' : 'type_string' },
            { 'name' : 'symbId', 'type' : 'type_string' },
        ],
        'children' : [
            { 'name' : 'Description', 'type' : 'type_string', 'prefix' : 'ct' },
        ],
        'xpath' : 'PharmML/IndependentVariable',
        'namespace' : 'pharmml'
    },
    'ModelDefinition' : {
        'fixed_attributes' : [
            { 'name' : 'xmlns', 'value' : 'http://www.pharmml.org/pharmml/0.8/ModelDefinition' }
        ],
        'children' : [
            { 'name' : 'VariabilityModel', 'type' : 'VariabilityModel', 'array' : True },
        ],
        'xpath' : 'PharmML/ModelDefinition',
        'namespace' : 'pharmml'
    },
    'VariabilityModel' : {
        'attributes' : [
            { 'name' : 'id', 'type' : 'type_string' },
            { 'name' : 'blkId', 'type' : 'type_string' },
            { 'name' : 'type', 'type' : 'type_string' }
        ],
        'children' : [
            { 'name' : 'Description', 'type' : 'type_string', 'prefix' : 'ct' },
            { 'name' : 'Name', 'type' : 'type_string', 'prefix' : 'ct' },
            { 'name' : 'Level', 'type' : 'Level', 'array' : True },
        ],
        'xpath' : 'PharmML/ModelDefinition/VariabilityModel',
        'namespace' : 'pharmml'
    },
    'Level' : {
        'attributes' : [
            { 'name' : 'id', 'type' : 'type_string' },
            { 'name' : 'referenceLevel', 'type' : 'type_string' },
            { 'name' : 'symbId', 'type' : 'type_string' }
        ],
        'children' : [
            { 'name' : 'Description', 'type' : 'type_string', 'prefix' : 'ct' },
            { 'name' : 'Name', 'type' : 'type_string', 'prefix' : 'ct' },
            #{ 'name' : 'ParentLevel', 'type' : 'ParentLevel' },
        ],
        'xpath' : 'PharmML/ModelDefinition/VariabilityModel/Level',
        'namespace' : 'pharmml'
    },
    #'ParentLevel' : {
    #    'attributes' : [
    #        { 'name' : 'id', 'type' : 'type_string' },
    #    ],
    #    'children' : [
    #        { 'name' : 'Description', 'type' : 'type_string', 'prefix' : 'ct' },
    #        { 'name' : 'SymbRef', 'type' : 'type_string', 'prefix' : 'ct' },


    #},
}
