resource "aws_s3_bucket" "s3_bucket" {
  bucket = var.bucket_name
  # acl = "private"
  force_destroy = true
}

output "s3" {
  value = aws_s3_bucket.s3_bucket.bucket
}
