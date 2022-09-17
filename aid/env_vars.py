import os

PREFECT_PROJECT_NAME = os.environ.get("AID_PROJECT_NAME", "aid-tenant")

FOO = os.environ.get("FOO", "foo")
BAR = os.environ.get("BAR", "bar")
