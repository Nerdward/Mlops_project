resource "aws_lambda_function" "lambda_function" {
  function_name = var.lamdba_function_name

  image_uri = var.image_uri
  package_type = "Image"
  role = aws_iam_role.lambda_exec.arn
  tracing_config {
    mode = "Active"
  }

  timeout = 180
}

resource "aws_cloudwatch_log_group" "lambda_log_group" {
  name = "/aws/lambda/${aws_lambda_function.lambda_function.function_name}"
  retention_in_days = 30
}
