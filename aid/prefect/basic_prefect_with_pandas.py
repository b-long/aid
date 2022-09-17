import prefect
from prefect import Flow, task
from prefect.engine.results import LocalResult

from aid.env_vars import PREFECT_PROJECT_NAME, FOO
from aid.etl.arbitrary_pandas import do_pandas
from aid.prefect.docker_utils import create_docker_runconfig, get_basic_docker_storage

my_pandas_result = LocalResult()


@task()
def pandas_task():
    logger = prefect.context.get("logger")
    logger.info(f"************Doing pandas thing for {FOO=}************")
    my_pandas = do_pandas()
    return my_pandas


flow_name = "basic-pandas-flow"
with Flow(flow_name) as flow:
    pandas_res = pandas_task()
    my_pandas_result.write(pandas_res)


flow.storage = get_basic_docker_storage(flow_name_for_tag=flow_name)
flow.run_config = create_docker_runconfig()


# Here we use no labels, since we want this Flow to
# just run locally.  Labels are a mechanism for assigning
# a flow to a particular compute resource (agent)
basic_labels = []
flow.register(project_name=PREFECT_PROJECT_NAME, build=True, labels=basic_labels)
