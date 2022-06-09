import aws_cdk as core
import aws_cdk.assertions as assertions

from speed_test.speed_test_stack import SpeedTestStack

# example tests. To run these tests, uncomment this file along with the example
# resource in speed_test/speed_test_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SpeedTestStack(app, "speed-test")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
