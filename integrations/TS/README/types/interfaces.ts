/*
Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
https://creativecommons.org/licenses/by-sa/4.0/
*/

import { ContextProblem, HowThisWorks, FourStages, WhyThisWorks, FAQ, WorkflowVisualization } from './core.js';

export interface ExampleProject {
  name: string;
  url: string;
  description: string;
  structureLink: string;
}

export interface ExampleProjects {
  projects: ExampleProject[];
  note: string;
}

export interface Setup {
  steps: string[];
}

export interface Execution {
  steps: string[];
}

export interface QualityAssurance {
  measures: string[];
}

export interface ImplementationSteps {
  setup: Setup;
  execution: Execution;
  qualityAssurance: QualityAssurance;
}

export interface ConfigurationOption {
  name: string;
  description: string;
  example: string;
}

export interface ConfigurationOptions {
  options: ConfigurationOption[];
}

export interface Output {
  features: string[];
}

export interface ProjectStateExtraction {
  description: string;
  command: string;
  configurationOptions: ConfigurationOptions;
  output: Output;
  usage: string;
  outputExamples: string;
}

export interface WhatToExpected {
  aiBehavior: string;
  developmentFlow: string;
  codeQuality: string;
}

export interface Model {
  name: string;
  link: string;
}

export interface Evaluation {
  description: string;
  analysisLink: string;
  note: string;
}

export interface Coverage {
  areas: string[];
}

export interface LLMModels {
  description: string;
  models: Model[];
  evaluation: Evaluation;
  coverage: Coverage;
}

export interface README {
  title: string;
  description: string;
  contextProblem: ContextProblem;
  howThisWorks: HowThisWorks;
  fourStages: FourStages;
  whyThisWorks: WhyThisWorks;
  exampleProjects: ExampleProjects;
  implementationSteps: ImplementationSteps;
  projectStateExtraction: ProjectStateExtraction;
  whatToExpected: WhatToExpected;
  llmModels: LLMModels;
  faq: FAQ;
  workflowVisualization: WorkflowVisualization;
}