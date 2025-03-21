from datetime import datetime as dt
from pathlib import Path

import click
from loguru import logger

from pipelines import (
    digital_data_etl
)


@click.command(
    help="""
LLM Engineering project CLI v0.0.1. 

Main entry point for the pipeline execution. 
This entrypoint is where everything comes together.

Run the ZenML LLM Engineering project pipelines with various options.

Run a pipeline with the required parameters. This executes
all steps in the pipeline in the correct order using the orchestrator
stack component that is configured in your active ZenML stack.

Examples:
  
  \b
  # Run only the ETL pipeline
  python run.py --run-etl

"""
)
@click.option(
    "--no-cache",
    is_flag=True,
    default=False,
    help="Disable caching for the pipeline run.",
)

@click.option(
    "--run-etl",
    is_flag=True,
    default=False,
    help="Whether to run the ETL pipeline.",
)
@click.option(
    "--etl-config-filename",
    default="digital_data_etl_paul_iusztin.yaml",
    help="Filename of the ETL config file.",
)

def main(
    no_cache: bool = False,
    run_etl: bool = False,
    etl_config_filename: str = "digital_data_etl_maxime_labonne.yaml",
) -> None:
    assert (
        run_etl
    ), "Please specify an action to run."

    pipeline_args = {
        "enable_cache": not no_cache,
    }
    root_dir = Path(__file__).resolve().parent.parent

    if run_etl:
        click.echo(f"Hello run_args_etl!")
        run_args_etl = {}
        pipeline_args["config_path"] = root_dir / "configs" / etl_config_filename
        assert pipeline_args["config_path"].exists(), f"Config file not found: {pipeline_args['config_path']}"
        pipeline_args["run_name"] = f"digital_data_etl_run_{dt.now().strftime('%Y_%m_%d_%H_%M_%S')}"
        click.echo(f"pipeline_args {pipeline_args}")
        digital_data_etl.with_options(**pipeline_args)(**run_args_etl)


if __name__ == "__main__":
    main()    