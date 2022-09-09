variable "aws_region" {
  default = "us-east-1"
}

variable "bucket_name" {
  description = "s3 bucket"
}

variable "project_id" {
    default = "nerdward-mlops-project"
}

variable "lambda_function_local_path" {
}

variable "docker_image_local_path" {

}

variable "ecr_repo_name" {
}

variable "lambda_function_name" {
  type = string
  description = "The Lambda function name"
}

variable "rest_api_name" {
  description = " "
}
