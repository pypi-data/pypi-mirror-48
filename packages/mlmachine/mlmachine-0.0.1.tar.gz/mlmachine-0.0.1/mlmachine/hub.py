import os
import sys
import importlib
modulePath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(modulePath) if modulePath not in sys.path else None

import seaborn as sns
sns.set_style('whitegrid')


class Machine():
    """
    Info:
        Description:
            Main class for handling several machine learning tasks, including
            data cleaning, feature encoding, exploratory data analysis, data
            prepation, model building, model tuning and model evaluation.

            Consolidates class methods from several different sub-modules.
    """
    
    # Import mlmachine modules
    
    from .explore.edaSuite import edaNumTargetNumFeat, edaCatTargetCatFeat, edaCatTargetNumFeat, edaNumTargetCatFeat, dfSideBySide
    from .explore.edaTransform import edaTransformInitial, edaTransformLog1, edaTransformBoxCox
    from .explore.edaMissing import edaMissingSummary
    
    from .features.encode import cleanLabel, Dummies, MissingDummies, OrdinalEncoder, CustomOrdinalEncoder
    from .features.importance import featureImportanceSummary
    from .features.impute import  NumericalImputer, ModeImputer, ConstantImputer, ContextImputer
    from .features.missing import missingDataDropperAll, featureDropper, missingColCompare
    from .features.outlier import OutlierIQR
    from .features.scale import Standard, Robust
    from .features.transform import skewSummary, SkewTransform, EqualBinner, CustomBinner, PercentileBinner, featureDropper
    
    from .model.tune.bayesianOptimSearch import execBayesOptimSearch, objective, unpackParams, lossPlot, paramPlot, samplePlot
    from .model.tune.powerGridSearch import PowerGridSearcher
    from .model.tune.stack import modelParamBuilder, SklearnHelper, oofGenerator, paramExtractor, modelStacker
    from .model.evaluate.crossvalidate import rmsleCV
    
    # importlib.reload(explore.edaSuite)
    # importlib.reload(explore.edaTransform)
    # importlib.reload(explore.edaMissing)
    # importlib.reload(features.encode)
    # importlib.reload(features.impute)
    # importlib.reload(features.missing)
    # importlib.reload(features.outlier)
    # importlib.reload(features.scale)
    # importlib.reload(features.transform)
    # importlib.reload(model.tune.bayesianOptimSearch)
    # importlib.reload(model.tune.powerGridSearch)
    # importlib.reload(model.tune.stack)
    # importlib.reload(model.evaluate.crossvalidate)

    def __init__(self, data, removeFeatures = [], overrideCat = None, overrideNum = None, dateFeatures = None, target = None, targetType = None):
        """
        Documentation:
            Description:
                __init__ handles ingestion of main data set, identification of select
                features to be removed (if any), identification of select features to
                be considered as categorical despite the features' data type (if any), 
                identification of select features to be considered as numerical despite 
                the features' data type (if any), identification of select features to be
                considered as date features (if any), identification of the feature 
                representing the target (if there is one) and the type of target. Returns
                data frame of independent variables, series containing dependent variable
                and a dictionary that categorizes features by data type.
            Parameters:
                data : Pandas DataFrame
                    Input data
                removeFeatures : list, default = []
                    Features to be completely removed from dataset
                overrideCat : list, default = None
                    Preidentified categorical features that would otherwise be labeled as continuous
                overrideCNum : list, default = None
                    Preidentified continuous features that would otherwise be labeled as categorical
                dateFeatures : list, default = None
                    Features comprised of date values, which will need to be handled differently
                target : list, default = None
                    Name of column containing dependent variable
                targetType : list, default = None
                    Target variable type, either 'categorical' or 'continuous'
            Attributes:
                X_ : Pandas DataFrame
                    Independent variables
                y_ : Pandas Series
                    Dependent variables
                featuresByDtype_ : dict
                    Dictionary containing two keys, continuous and categorical, each paired with a
                    value that is a list of column names that are of that feature type - continuous or categorical.
        """
        
        self.data = data
        self.removeFeatures = removeFeatures
        self.overrideCat = overrideCat
        self.overrideNum = overrideNum
        self.dateFeatures = dateFeatures
        self.target = target
        self.targetType = targetType

        # Execute method measLevel
        if self.target is not None:
            self.X_, self.y_, self.featureByDtype_ = self.measLevel()
        else:
            self.X_, self.featureByDtype_ = self.measLevel()
    
    def measLevel(self):
        """
        Documentation:
            Description:
                Isolate independent variables in X_.
                If provided, isolate dependent variable y_.
                Determine level of measurement for each feature as categorical, continuous or date.
        """
        ### Identify target from features
        if self.target is not None:
            self.y_ = self.data[self.target]
            self.cleanLabel()
            self.X_ = self.data.drop(self.removeFeatures + self.target, axis = 1)
        else:
            self.X_ = self.data.drop(self.removeFeatures, axis = 1)            
        
        ### Add categorical and continuous keys, and any associated overrides
        self.featureByDtype_ = {}
        
        # Categorical
        if self.overrideCat is None:
            self.featureByDtype_['categorical'] = []
        else:
            self.featureByDtype_['categorical'] = self.overrideCat

        # continuous
        if self.overrideNum is None:
            self.featureByDtype_['continuous'] = []
        else:
            self.featureByDtype_['continuous'] = self.overrideNum
        
        # Date
        if self.dateFeatures is None:
            self.featureByDtype_['date'] = []
        else:
            self.featureByDtype_['date'] = self.dateFeatures
        
        # Combined dictionary values for later filtering
        handled = [i for i in sum(self.featureByDtype_.values(), [])]
        
        ### Categorize remaining columns
        for c in [i for i in self.X_.columns if i not in handled]:
            
            # Identify feature type based on column data type
            if str(self.X_[c].dtype).startswith(('int','float')):
                self.featureByDtype_['continuous'].append(c)
            elif str(self.X_[c].dtype).startswith(('object')):
                self.featureByDtype_['categorical'].append(c)

        ### Return objects
        if self.target is not None:
            return self.X_, self.y_, self.featureByDtype_
        else:
            return self.X_, self.featureByDtype_

