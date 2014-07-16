import os
import json

import elasticsearch
import flask

app = flask.Flask(__name__)

connection_info = {
    "host": os.environ.get("OPENSHIFT_ES_HOST"),
    "port": os.environ.get("OPENSHIFT_ES_PORT", "9243"),
    "use_ssl": True,
    "http_auth": "%s:%s" % (os.environ.get("OPENSHIFT_ES_USER", ""), os.environ.get("OPENSHIFT_ES_PASSWORD", ""))
}

client = elasticsearch.Elasticsearch(hosts=[connection_info])

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/v1/search")
def search():
    query = flask.request.args.get("query")
    search = {"query": {"match_all": {}}}
    if query:
        search["query"] = {"match": {"_all": query}}

    response = client.search(body=search)

    return flask.Response(json.dumps(response), content_type="application/json; charset=utf-8")

if __name__ == "__main__":
    app.run()

