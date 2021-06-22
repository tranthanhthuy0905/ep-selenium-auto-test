import subprocess

if __name__ == '__main__':
    ######Create a Bucket
    create_bucket_cmd = "python ./ep-storage_headless/buckets/bucketFlow.py"
    create_bucket_process = subprocess.Popen(create_bucket_cmd.split(), stdout=subprocess.PIPE)