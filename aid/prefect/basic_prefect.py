import prefect
from prefect import Flow, task
from prefect.engine.results import LocalResult

from aid.env_vars import PREFECT_PROJECT_NAME
from aid.prefect.docker_utils import create_docker_runconfig, get_basic_docker_storage

my_add_result = LocalResult()


@task()
def addition_task(x, y):
    logger = prefect.context.get("logger")
    logger.info("************Performing addition************")
    return x + y


flow_name = "basic-add-flow"
with Flow(flow_name) as flow:
    res = addition_task(3, 4)
    my_add_result.write(res)


flow.storage = get_basic_docker_storage(flow_name_for_tag=flow_name)
flow.run_config = create_docker_runconfig()
# Here we use no labels, since we want this Flow to
# just run locally.  Labels are a mechanism for assigning
# a flow to a particular compute resource (agent)
basic_labels = []
flow.register(project_name=PREFECT_PROJECT_NAME, build=True, labels=basic_labels)
