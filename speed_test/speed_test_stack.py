from aws_cdk import (
    CfnOutput,
    CfnParameter,
    Stack,
    aws_lambda,
    aws_dynamodb,
    aws_apigateway as apigw,
)
from constructs import Construct

class SpeedTestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create dynamoDB table
        demo_table = aws_dynamodb.Table(
            self, "demo_table",
            partition_key=aws_dynamodb.Attribute(
                name="id",
                type=aws_dynamodb.AttributeType.STRING
            )
        )

        # create lambda function
        lambda_function = aws_lambda.Function(
            self, "lambda_function",
            runtime=aws_lambda.Runtime.PYTHON_3_7,
            handler="lambda_function.lambda_handler",
            code=aws_lambda.Code.from_asset("./lambda")
        )
        lambda_function.add_environment("TABLE_NAME", demo_table.table_name)

        # grant permission to lambda to write to demo table
        demo_table.grant_write_data(lambda_function)

        # Create an API gateway REST API
        base_api = apigw.LambdaRestApi(
            self, 'ApiGW', 
            rest_api_name="MainAPI", 
            handler=lambda_function,
            )
        base_api.root.add_method("POST", target= lambda_function)

        #TODO: Figure out how to dynamically pass the API url to window_script when it deploys. Does not work now. Simply importing results in error... 
        # cfn Parameter or output? As a temporary solution I'm just hard-coding the APIGW URL it outputs in the console when I deploy.

        #api_url = base_api.url

        #print(api_url)
        #CfnOutput(self, 'api_url', value=api_url)
        #CfnParameter (self, 'api_url', typevalue=api_url)