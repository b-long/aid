from prefect.run_configs import DockerRun
from prefect.storage import Docker


def create_docker_runconfig():
    docker_run = DockerRun()
    return docker_run


def get_basic_docker_storage(flow_name_for_tag: str):
    # More info: https://docs-v1.prefect.io/orchestration/flow_config/docker.html
    return Docker(
        dockerfile="Dockerfile.prefect",
        # Tag the image that we build, so we can make a
        # unique docker images per flow
        image_tag=flow_name_for_tag,
    )
