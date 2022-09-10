variable "lamdba_function_name" {
  type = string
  description = "The lambda function name"
}

variable "image_uri" {
  description = "ecr image uri"
}

variable "bucket_name" {
  type = string
  description = "The s3 bucket name"
}
