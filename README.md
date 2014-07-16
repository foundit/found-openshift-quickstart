Found on OpenShift
==================

This git repository helps you get up and running quickly with hosted Elasticsearch on OpenShift.


Creating a cluster
----------------------------

1. Create an account at [Found.no](https://www.found.no/). You can start with a 14 day free trial, no creditcard required.
2. [Create a cluster](https://www.found.no/documentation/tutorials/getting-started/#create-your-first-cluster).
3. [Configure Access Control](https://www.found.no/documentation/tutorials/getting-started/#access-control)
4. Take note of the cluster's endpoint (e.g `https://abc1234-us-east-1.foundcluster.com:9243`) and the username and password from step 3.


Running on OpenShift
----------------------------

Create an account at https://www.openshift.com

Create a python application

    rhc app create estest python-2.7 \
      --from-code http://github.com/foundit/found-openshift-quickstart.git \
      --env OPENSHIFT_ES_HOST="abc123-us-east-1.foundcluster.com" \
      --env OPENSHIFT_ES_USER="user" \
      --env OPENSHIFT_ES_PASSWORD="secret"

That's it, you can now checkout your application at:

    http://estest-$yournamespace.rhcloud.com

A very simple search-API is available at `http://estest-$yournamespace.rhcloud.com/api/v1/search?query=term`.

See `wsgi/myflaskapp.py` for how it works.

