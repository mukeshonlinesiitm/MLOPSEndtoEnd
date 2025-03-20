import click
from datetime import datetime as dt
from pathlib import Path

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
    "--run-etl",
    is_flag=True,
    default=False,
    help="Whether to run the ETL pipeline.",
)
def main(
    run_etl: bool = False,
) -> None:
    assert (
        run_etl
    ), "Please specify an action to run."

    if run_etl:
        click.echo(f"Hello run_args_etl!")

if __name__ == "__main__":
    main()    