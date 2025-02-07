Feature: Python models
  Background: Project Setup
    Given the project spark
    Given the profile spark

  Scenario: Run a project with a SQL model with table materialization
    When the following shell command is invoked:
      """
      dbt run --profiles-dir $profilesDir --project-dir $baseDir --select +model_b
      """
    Then there should be no errors
    Then the following models are calculated in order:
      | model_a | model_b |

  Scenario: Run a project with a SQL model with incremental materialization
    When the following shell command is invoked:
      """
      dbt run --profiles-dir $profilesDir --project-dir $baseDir --select +model_c
      """
    Then there should be no errors
    Then the following models are calculated in order:
      | model_a | model_c |
