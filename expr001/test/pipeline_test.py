import kfp
from kfp import dsl
from kfp.compiler import Compiler

sb_op = kfp.components.load_component_from_url("https://raw.githubusercontent.com/demotto/my-pipeline/master/expr001/component.yaml")


@dsl.pipeline(
    name='simple pipeline',
    description='A trainer that does end-to-end distributed training for XGBoost models.'
)
def my_pipeline():
    my_task = sb_op(
        input1="xxxxxxxxxx",
        input2="oooooooooo",
        output1="/mnt/result.txt"
    )


if __name__ == '__main__':
    compiler = Compiler()
    compiler.compile(my_pipeline, "my_brick.yaml")

