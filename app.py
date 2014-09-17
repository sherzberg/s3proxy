import os
import io
import boto
from flask import Flask, send_file


conn = boto.connect_s3()
bucket_name = os.environ.get('AWS_BUCKET_NAME', '')

if conn.lookup(bucket_name) is None:
    raise Exception("No bucket named: {}".format(bucket_name))


app = Flask(__name__)


@app.route('/serve/<filename>')
def download(filename):
    bucket = conn.get_bucket(bucket_name)
    key = bucket.get_key(filename)
    b = key.get_contents_as_string()

    return send_file(
        io.BytesIO(b),
        attachment_filename=filename,
        mimetype='application/text'
    )


@app.route('/health')
def health():
    conn.get_all_buckets()
    return 'OK'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=os.environ.get('DEBUG', 'false').lower() == 'true')

