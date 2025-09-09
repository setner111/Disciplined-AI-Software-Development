/*
Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
https://creativecommons.org/licenses/by-sa/4.0/
*/

export interface Phase0Requirements {
  benchmarkingSuite: {
    regressionDetection: boolean;
    baselineSaving: boolean;
    jsonOutput: boolean;
    timeline: boolean;
    visualPieCharts: boolean;
  };
  githubWorkflows: {
    release: boolean;
    regressionBenchmarkDetection: boolean;
  };
  centralizedEntryPoints: {
    main: boolean;
    config: boolean;
    constants: boolean;
    logging: boolean;
  };
  testSuite: {
    regressionDetection: boolean;
    baselineSaving: boolean;
    jsonOutput: boolean;
    timeline: boolean;
    visualPieCharts: boolean;
  };
  stressSuite: {
    regressionDetection: boolean;
    baselineSaving: boolean;
    jsonOutput: boolean;
    timeline: boolean;
    visualPieCharts: boolean;
  };
  inHouseDocumentationGeneration: {
    docs: boolean;
    readme: boolean;
  };
}