from aws_cdk import (
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
        base_api = apigw.LambdaRestApi(self, 'ApiGW', rest_api_name="MainAPI", handler=lambda_function)
        #TODO: Figure out how to dynamically pass the API url to window_script. Does not work now. 
        #...either create custom domain name or something else. No idea
        api_url = base_api.url
        #See above TODO, right now you jus have to pull the url from the print statement below or the console
        #...and plug it into api_url in windows_script
        print(api_url)