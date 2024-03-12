# from datetime import datetime
# from unittest.mock import MagicMock, call
#
# import pytest
# from airflow.models.dag import DAG
# from airflow.models.taskinstance import Context, TaskInstance
#
# from plugins.operators.custom_operator import CustomOperator
#
#
# def test_custom_operator_should_log_message_correctly(test_dag, spy_log):
#     operator = CustomOperator(name="example", task_id="custom", dag=test_dag)
#
#     ti = TaskInstance(task=operator, execution_date=datetime.now())
#     test_context: Context = ti.get_template_context()
#
#     mock_dag_run = MagicMock()
#     mock_dag_run.conf = {"message": "happy international women's day!"}
#     test_context["dag_run"] = mock_dag_run
#
#     operator.execute(test_context)
#
#     assert spy_log.info.call_count == 1
#     assert spy_log.info.call_args == call("message: happy international women's day!")
#
#
# @pytest.fixture
# def test_dag() -> DAG:
#     return DAG(
#         dag_id="test_dag",
#         default_args={"owner": "someone", "start_date": datetime(2022, 1, 1)},
#     )
#
#
# @pytest.fixture
# def spy_log(mocker) -> MagicMock:
#     return mocker.patch("plugins.operators.custom_operator.CustomOperator.log")
