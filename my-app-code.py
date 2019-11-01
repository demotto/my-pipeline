
import kfp
from kfp import components
from kfp import dsl
from kfp import gcp

from kfp.compiler import Compiler


def my_func():
    print("call my_func")


def next_func(a):
    print("next_func: " + str(a))


my_op = components.func_to_container_op(my_func)
next_op = components.func_to_container_op(next_func)


@dsl.pipeline(
    name='simple pipeline',
    description='A trainer that does end-to-end distributed training for XGBoost models.'
)
def my_pipeline():
    my_task = my_op()
    next_task = next_op("111")
    next_task.after(my_task)


if __name__ == '__main__':
    compiler = Compiler()
    compiler.compile(my_pipeline, "hallo.tar.gz")
    # client = kfp.Client()
    # kfp.Client().create_run_from_pipeline_func(my_pipeline, arguments=None)
