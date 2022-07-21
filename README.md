# MLflow Pipelines Batch Scoring Template
The [MLflow Batch Scoring Pipeline](https://mlflow.org/docs/latest/pipelines.html#batch-scoring-pipeline)
is an [MLflow Pipeline](https://mlflow.org/docs/latest/pipelines.html) for applying a registered MLflow
model to a specified dataset. 

For more information about the MLflow Batch Scoring Pipeline, check out the documentation at
https://mlflow.org/docs/latest/pipelines.html#batch-scoring-pipeline. For more information about MLflow
Pipelines, see https://mlflow.org/docs/latest/pipelines.html.

## Installation instructions
1. Install MLflow Pipelines: `pip install mlflow[pipelines]`
2. Clone the MLflow Batch Scoring Pipeline template repository locally:

```
git clone https://github.com/mlflow/mlp-batch-scoring-template.git.
```

3. Enter the root directory of the MLflow Batch Scoring Pipeline template: `cd mlp-batch-scoring-template`
4. Install MLflow Batch Scoring Pipeline dependencies: `pip install -r requirements.txt`


## Development Environment -- Databricks
[Sync](https://docs.databricks.com/repos.html) this repository with
[Databricks Repos](https://docs.databricks.com/repos.html) and run the `notebooks/databricks`
notebook on a Databricks Cluster running version 11.0 or greater of the
[Databricks Runtime](https://docs.databricks.com/runtime/dbr.html) or the
[Databricks Runtime for Machine Learning](https://docs.databricks.com/runtime/mlruntime.html)
with [workspace files support enabled](https://docs.databricks.com/repos.html#work-with-non-notebook-files-in-a-databricks-repo).

**Note**: When making changes to pipelines on Databricks,
it is recommended that you either edit files on your local machine and
use [dbx](https://docs.databricks.com/dev-tools/dbx.html) to sync them to Databricks Repos, as
demonstrated [here](https://mlflow.org/docs/latest/pipelines.html#usage), or edit files in
Databricks Repos by opening separate browser tabs for each YAML file or Python code module that you
wish to modify.

For the latter approach, we recommend opening at least **3 browser tabs** to
facilitate easier development:
- One tab for modifying configurations in `pipeline.yaml` and / or `profiles/{profile}.yaml`
- One tab for modifying step function(s) defined in `steps/{step}.py`
- One tab for modifying and running the driver notebook (`notebooks/databricks`)

## Development Environment -- Local machine
### Jupyter

1. Launch the Jupyter Notebook environment via the `jupyter notebook` command.
2. Open and run the `notebooks/jupyter.ipynb` notebook in the Jupyter environment.

### Command-Line Interface (CLI)

First, enter the template root directory via `cd mlp-batch-scoring-template`. Then, try running the
following [MLflow CLI](https://mlflow.org/docs/latest/cli.html) commands to get started. Note that
the `--step` argument is optional; pipeline commands that are run without a `--step` act on
the entire pipeline.

```
export MLFLOW_PIPELINES_PROFILE=local
mlflow pipelines --help
mlflow pipelines inspect --step step_name
mlflow pipelines run --step step_name
mlflow pipelines clean --step step_name
```

