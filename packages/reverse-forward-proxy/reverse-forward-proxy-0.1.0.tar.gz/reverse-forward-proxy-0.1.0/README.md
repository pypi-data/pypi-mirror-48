# reverse-forward-proxy

Reverse proxy to resources behind a forward proxy. The purpose of this is to
simplify configuration of clients or allow scaling behind load balancers that
do not support forward proxying on the back-end (e.g. HAProxy, Squid, Apache).

## Usage

```
# Required.
HTTP_PROXY=http://192.168.1.2:8080
# Optional. Defaults to $HTTP_PROXY
HTTPS_PROXY=http://192.168.1.2:8080
# Optional.
SSL_CERT_FILE=
# Optional. Enabled when set to '1'
REVERSE_FORWARD_PROXY_VERBOSE=
# Optional. Default is "localhost"
REVERSE_FORWARD_PROXY_HOST=
# Optional. Default is "8080"
REVERSE_FORWARD_PROXY_PORT=
# Optional. Default is "X-Reverse-Forward-Proxy-Target"
REVERSE_FORWARD_PROXY_TARGET_HEADER=
reverse-forward-proxy
```

Now the server will be up and listening on `http://localhost:8080` for requests.

Requests must have header `X-Reverse-Forward-Proxy-Target` set to the remote
host to connect to via the proxy.

The server will make the request via `$HTTP_PROXY` and return the response.

## Testing

```
pytest
```

```
make docker-test
docker run --rm --net=host svagi/h2load --h1 -n 100 -c5 -H "X-Reverse-Forward-Proxy-Target: http://files/" http://localhost:$(make get-port)/file.100m
```
