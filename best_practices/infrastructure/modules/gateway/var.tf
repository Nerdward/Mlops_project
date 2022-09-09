variable "rest_api_name" {
    type = string
    description = "Name of the API Gateway created"
}

variable "api_gateway_region" {
  type = string
  description = "The region"
}

variable "api_gateway_account_id" {
  type = string
  description = "The account ID"
}

variable "lamdba_function_name" {
  type = string
  description = "The name of the Lambda function"
}

variable "lambda_function_arn" {
  type = string
  description = "The ARN of the Lambda function"
}

variable "rest_api_stage_name" {
  type = string
  description = "The name of the API Gateway stage"
  default = "stg"
}
