import pytest

from airflow.models import DagBag


@pytest.fixture()
def dagbag():
    return DagBag()


def test_dag_loaded(dagbag):
    dag = dagbag.get_dag(dag_id="example_dag_daily")
    assert len(dagbag.import_errors) == 0, "No Import Failures"
    assert dag is not None
    assert len(dag.tasks) == 3
