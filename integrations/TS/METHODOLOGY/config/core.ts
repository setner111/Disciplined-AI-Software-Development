/*
Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
https://creativecommons.org/licenses/by-sa/4.0/
*/

import { CoreArchitecturalPrinciples } from '../types';

export const CORE_ARCHITECTURAL_PRINCIPLES: CoreArchitecturalPrinciples = {
  foundationalPhilosophy: {
    architecturalMinimalism: true,
    deterministicReliability: true,
    measurableValue: true,
    productionFocus: true
  },
  codeArchitecturePrinciples: {
    separationOfConcerns: {
      singleResponsibility: true,
      strictModularBoundaries: true,
      clearInterfaces: true,
      recognizeSeparationHarm: true,
      centralizedMainEntryPoints: true,
      modularProjectLayout: true
    },
    deterministicOperations: {
      synchronousBehavior: true,
      predictableOperations: true,
      longRuntimeStability: true,
      productionStability: true,
      crossPlatformConsiderations: true
    },
    performanceDrivenDecisions: {
      workloadBasedChoices: true,
      optimizeProvenBottlenecks: true,
      avoidPrematureOptimization: true,
      maintainPerformanceBaselines: true,
      regressionDetection: true
    },
    codeQualityStandards: {
      maxFileLines: 150,
      selfExplanatoryCode: true,
      avoidComments: true,
      preserveReadability: true,
      maintainMaintainability: true,
      followKISS: true,
      followDRY: true,
      reuseExistingFunctions: true
    },
    errorHandlingPhilosophy: {
      robustWithoutOverEngineering: true,
      productionReliability: true,
      avoidOverHandling: true,
      gracefulFailureModes: true,
      resourceCleanup: true
    },
    featureControl: {
      resistFeatureBloat: true,
      resistComplexityCreep: true,
      serveCoreProjectPurpose: true,
      surgicalApproach: true,
      targetExactProblem: true,
      minimalCode: true,
      multiLanguageJustified: true,
      measurableGains: true
    },
    webDevelopmentAdaptations: {
      noInlining: true,
      stylesToSeparateFiles: true,
      handlersToNamedFunctions: true,
      configurationsAsConstants: true,
      maxComponentLines: 250,
      maxModuleLines: 150,
      asyncOperationsAllowed: ["API calls", "user interactions", "data fetching"],
      errorBoundariesRequired: ["network operations", "user inputs", "third-party integrations"],
      fileColocation: ["Component.jsx", "Component.module.css", "Component.test.js"],
      componentSplittingCriteria: ["multiple purposes", "testing difficulty"],
      requestArchitecturalClarification: true
    }
  }
};