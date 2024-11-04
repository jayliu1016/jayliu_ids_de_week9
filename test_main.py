import subprocess
import logging
import papermill as pm

logger = logging.getLogger(__name__)


def test_main_script_runs():
    # Run the main.py script as a subprocess
    try:
        result = subprocess.run(
            ["python", "main.py"], check=True, capture_output=True, text=True
        )
        logger.info("main.py ran successfully")
    except subprocess.CalledProcessError as e:
        logger.error(f"main.py encountered an error: {e.stderr}")
        raise

    # Ensure that there is output and that it does not indicate an error
    assert result.returncode == 0, "main.py script did not exit successfully"
    assert (
        "Loading dataset..." in result.stderr
    ), "Script did not log 'Loading dataset...'"


def test_colab_notebook_runs():
    # Define the notebook URL and output path
    notebook_url = (
        "https://colab.research.google.com/drive/1_4-E6Qzfre5eQdrGY8RI7-TlfcrpFIh7"
    )
    output_path = "/tmp/output_notebook.ipynb"

    try:
        # Execute the notebook
        pm.execute_notebook(notebook_url, output_path, parameters={})
        logger.info("Google Colab notebook ran successfully")
    except pm.PapermillExecutionError as e:
        logger.error(f"Google Colab notebook encountered an error: {e}")
        raise
