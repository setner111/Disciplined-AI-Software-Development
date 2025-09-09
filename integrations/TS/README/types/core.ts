/*
Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
https://creativecommons.org/licenses/by-sa/4.0/
*/

export interface ContextProblem {
  description: string;
  issues: string[];
}

export interface HowThisWorks {
  description: string;
  principle: string;
}

export interface Stage {
  name: string;
  description: string;
  steps?: string[];
  fileSizeConstraint?: string;
  benefits?: string[];
  implementationFlow?: string;
  output?: string;
}

export interface FourStages {
  stage1: Stage;
  stage2: Stage;
  stage3: Stage;
  stage4: Stage;
}

export interface WhyThisWorks {
  decisionProcessing: string;
  contextManagement: string;
  empiricalValidation: string;
  systematicConstraints: string;
}

export interface Question {
  title: string;
  answer: string;
}

export interface OriginAndDevelopment {
  questions: Question[];
}

export interface PersonalPractice {
  questions: Question[];
}

export interface AIDevelopmentJourney {
  questions: Question[];
}

export interface MethodologySpecifics {
  questions: Question[];
}

export interface PracticalImplementation {
  questions: Question[];
}

export interface FAQ {
  originAndDevelopment: OriginAndDevelopment;
  personalPractice: PersonalPractice;
  aiDevelopmentJourney: AIDevelopmentJourney;
  methodologySpecifics: MethodologySpecifics;
  practicalImplementation: PracticalImplementation;
}

export interface WorkflowVisualization {
  description: string;
  note: string;
}