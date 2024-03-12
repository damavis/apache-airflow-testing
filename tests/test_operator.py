import datetime
from http import HTTPStatus

import pendulum
import pytest

from airflow import DAG
from airflow.utils.state import DagRunState, TaskInstanceState
from airflow.utils.types import DagRunType

from plugins.operators.custom_operator import CustomOperator

DATA_INTERVAL_START = pendulum.datetime(2021, 9, 13, tz="UTC")
DATA_INTERVAL_END = DATA_INTERVAL_START + datetime.timedelta(days=1)

TEST_DAG_ID = "my_custom_operator_dag5"
TEST_TASK_ID = "my_custom_operator_task"


@pytest.fixture()
def dag():
    with DAG(TEST_DAG_ID, default_args={'owner': 'airflow', 'start_date': DATA_INTERVAL_START}
             ) as dag:
        CustomOperator(
            task_id=TEST_TASK_ID,
            name="Example"
        )
    return dag


def test_my_custom_operator(mocker, dag):
    fake_resp = mocker.Mock()
    fake_resp.json = mocker.Mock(return_value="response")
    fake_resp.status_code = HTTPStatus.OK
    mocker.patch("plugins.operators.custom_operator.requests.get", return_value=fake_resp)

    dagrun = dag.create_dagrun(
        state=DagRunState.RUNNING,
        execution_date=DATA_INTERVAL_START,
        start_date=DATA_INTERVAL_END,
        run_type=DagRunType.MANUAL
    )

    ti = dagrun.get_task_instance(task_id=TEST_TASK_ID)
    ti.task = dag.get_task(task_id=TEST_TASK_ID)
    ti.task.execute(ti.get_template_context())

    assert ti.state == TaskInstanceState.SUCCESS
